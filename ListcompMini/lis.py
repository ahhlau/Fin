################ Lispy: Scheme Interpreter in Python

## (c) Peter Norvig, 2010-14; See http://norvig.com/lispy.html

################ Types

from __future__ import division

Symbol = str          # A Lisp Symbol is implemented as a Python str
List   = list         # A Lisp List is implemented as a Python list
Number = (int, float) # A Lisp Number is implemented as a Python int or float

################ Parsing: parse, tokenize, and read_from_tokens

# def parse(program):
#     "Read a Scheme expression from a string."
#     return read_from_tokens(tokenize(program))
#
# def tokenize(s):
#     "Convert a string into a list of tokens."
#     return s.replace('(',' ( ').replace(')',' ) ').split()
#
# def read_from_tokens(tokens):
#     "Read an expression from a sequence of tokens."
#     if len(tokens) == 0:
#         raise SyntaxError('unexpected EOF while reading')
#     token = tokens.pop(0)
#     if '(' == token:
#         L = []
#         while tokens[0] != ')':
#             L.append(read_from_tokens(tokens))
#         tokens.pop(0) # pop off ')'
#         return L
#     elif ')' == token:
#         raise SyntaxError('unexpected )')
#     else:
#         return atom(token)
#
# def atom(token):
#     "Numbers become numbers; every other token is a symbol."
#     try: return int(token)
#     except ValueError:
#         try: return float(token)
#         except ValueError:
#             return Symbol(token)

################ Environments

def standard_env():
    "An environment with some Scheme standard procedures."
    import math, operator as op
    env = Env()
    env.update(vars(math)) # sin, cos, sqrt, pi, ...
    env.update({
        '+':op.add, '-':op.sub, '*':op.mul, '/':op.div, 
        '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq, 
        'abs':     abs,
        'append':  op.add,  
        'apply':   apply,
        'begin':   lambda *x: x[-1],
        'car':     lambda x: x[0],
        'cdr':     lambda x: x[1:], 
        'cons':    lambda x,y: [x] + y,
        'eq?':     op.is_, 
        'equal?':  op.eq, 
        'length':  len, 
        'list':    lambda *x: list(x), 
        'list?':   lambda x: isinstance(x,list),
        'exec':    lambda x: eval(compile(x,'None','single')),
        'map':     map,
        #pokedex = database of pokemon (list)
        #strengths = database of strengths of pokemon types (list)
        #strongtype = the type the pokemon are strong against (quoted List)
        #pokemontype = the type of the pokemon that are strong against strongtype
        'FindStrongPokemon' : lambda pokedex, strengths, strongType: [[pokemontype, sorted([p[1] for p in pokedex if p[2] == pokemontype or p[3] == pokemontype])] for pokemontype in sorted({s[0] for s in strengths if s[1] == strongType[0] or s[2] == strongType[0] or s[3] == strongType[0] or s[4] == strongType[0]})],
        'max':     max,
        'min':     min,
        'not':     op.not_,
        'null?':   lambda x: x == [], 
        'number?': lambda x: isinstance(x, Number),   
        'procedure?': callable,
        'round':   round,
        'symbol?': lambda x: isinstance(x, Symbol),
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

def eval(x, env=global_env):
    "Evaluate an expression in an environment."
    if isinstance(x, Symbol):      # variable reference
        # print "debug: ", x
        return env.find(x)[x]
    elif not isinstance(x, List):  # constant literal
        return x                
    elif x[0] == 'quote':          # (quote exp)
        (_, exp) = x
        return exp
    elif x[0] == 'if':             # (if test conseq alt)
        (_, test, conseq, alt) = x
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)
    elif x[0] == 'lambda':         # (lambda (var...) body)
        (_, parms, body) = x
        return Procedure(parms, body, env)
    #loads a file 'filename' into a list and returns a list
    elif x[0] == 'ListLoader':
        filename = x[1:][0]
        filename = filename.strip("'")
        import ListMaker
        output = ListMaker.make(filename)
        return output
    elif x[0] == 'exec':
        proc = eval(x[0], env)
        import re
        exec(proc(re.sub(r"^'|'$", '', x[1])))
        return toReturn
    else:                          # (proc arg...)
        proc = eval(x[0], env)
        args = [eval(exp, env) for exp in x[1:]]
        return proc(*args)
