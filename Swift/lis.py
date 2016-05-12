from __future__ import division

def parse(program):
    result = yacc.parse(program)
    if result != None:
        return result

Symbol = str          # A Lisp Symbol is implemented as a Python str
List   = list         # A Lisp List is implemented as a Python list
Number = (int, float) # A Lisp Number is implemented as a Python int or float

################ Environments


def standard_env():
    "An environment with some Scheme standard procedures."
    import math, operator as op
    env = Env()
    env.update(vars(math)) # sin, cos, sqrt, pi, ...
    env.update({
        '+':op.add,
        '-':op.sub,
        '*':op.mul,
        '/':op.div,
        '>':op.gt,
        '<':op.lt,
        '>=':op.ge,
        '<=':op.le,
        '=':op.eq,
    })
    return env

class Env(dict):
    "An environment: a dict of {'var':val} pairs, with an outer Env."
    def __init__(self, parms=(), args=(), outer=None):
        self.update(zip(parms, args))
        self.outer = outer
    def find(self, var):
        "Find the innermost Env where var appears."
        return self if (var in self) else self.outer.find(var)

global_env = standard_env()

################ Procedures

class Procedure(object):
    "A user-defined Scheme procedure."
    def __init__(self, parms, body, env):
        self.parms, self.body, self.env = parms, body, env
    def __call__(self, *args):
        return eval(self.body, Env(self.parms, args, self.env))

################ eval

toReturn = None
constants = {}
optional = {}
# variables = {}

def eval(x, env=global_env):
    "Evaluate an expression in an environment."
    if isinstance(x, Symbol) and (x in env):      # variable reference
        return env.find(x)[x]
    # elif isinstance(x, Symbol) and '"' not in x:
    #     try:
    #         if x in constants.keys():
    #             return constants[x]
    #         else:
    #             raise Exception("use of unresolved identifier %s" % x)
    #     except Exception as e:
    #         raise e
    elif not isinstance(x, List):  # constant literal
        return x

    elif x[0] == 'if':             # (if test conseq alt)
        (_, test, conseq, alt) = x
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)

    elif x[0] == 'let':
        (_, constant_value) = x
        const = constant_value[0]
        val = eval(constant_value[1], env)
        if const in constants.keys() or const in optional.keys():
            raise Exception("constant already declared")
                # print "%s already declared"
        elif len(constant_value) == 2:
            constants[const] = val
            print "constants:", constants
        else:
            optional[const] = [val, constant_value[2], constant_value[3]]
            print "optional:", optional
    elif x[0] == 'print':
        arg = eval(x[1], env)
        print arg
        return arg


    elif x[0] == 'exec':
        proc = eval(x[0], env)
        import re
        exec(proc(re.sub(r"^'|'$", '', x[1])))
        return toReturn
    else:                          # (proc arg...)
        proc = eval(x[0], env)
        args = [eval(exp, env) for exp in x[1:]]
        return proc(*args)
