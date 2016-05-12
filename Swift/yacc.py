import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens

DEBUG = True

# namespace & built-in functions

variables = {}
optional = {}

global ast
ast = []

# BNF

def p_programs(p):
    '''program : program programs
    '''
    p[0] = [p[1]] + p[2]

def p_program_base(p):
    '''programs : program
    '''
    p[0] = [p[1]]

def p_program(p):
    '''program : statement
               | expression
    '''
    p[0] = p[1]

def p_print(p):
    '''statement : PRINT "(" expression ")"
    '''

    if DEBUG:
        print "Saw print: ", p[3]
    print p[3]
    p[0] = [p[1], p[3]]

def p_statement_assign_type_optional_bang(p):
    '''statement : LET IDENTIFIER ":" type "!"
                 | LET IDENTIFIER ":" type "!" "=" expression
                 | LET IDENTIFIER ":" type "!" "=" NIL
    '''
    if len(p) == 6:
        optional[p[2]] = [None, "!", False]
        if DEBUG:
            print "Saw statement assign type optional ", optional
        return p[1]
    elif len(p) == 8 and p[7] == "nil":
        optional[p[2]] = [p[7], "!", False]
        if DEBUG:
            print "Saw statement assign type optional expression ", optional
    else:
        optional[p[2]] = [p[7], "!", True]
        if DEBUG:
            print "Saw statement assign type optional expression ", optional


def p_statement_assign_type_optional(p):
    '''statement : LET IDENTIFIER ":" type "?"
                 | LET IDENTIFIER ":" type "?" "=" expression
                 | LET IDENTIFIER ":" type "?" "=" NIL
    '''
    if len(p) == 6:
        optional[p[2]] = [None, "?", False]
        if DEBUG:
            print "Saw statement assign type optional ", optional
    elif len(p) == 8 and p[7] == "nil":
        optional[p[2]] = [p[7], "?", False]
        p[0] = [p[1], [p[2],p[7],p[5],False]]
        if DEBUG:
            print "Saw statement assign type optional expression ", optional
    else:
        optional[p[2]] = [p[7], "?", True]
        p[0] = [p[1], [p[2],p[7],p[5],True]]
        if DEBUG:
            print "Saw statement assign type optional expression ", optional

def p_statement_assign_type(p):
    '''statement : LET IDENTIFIER ":" type
                 | LET IDENTIFIER ":" type "=" expression
     '''
    if len(p) == 5:
        variables[p[2]] = None
        if DEBUG:
            print "Saw statement assign type ", variables
    else:
        variables[p[2]] = p[6]
        if DEBUG:
            print "Saw statement assign type expression", variables

def p_assign_type(p):
    '''statement : IDENTIFIER "=" expression
                 | IDENTIFIER "=" NIL
    '''
    if p[1] in variables.keys():
        variables[p[1]] = p[3]
        if DEBUG:
            print "Saw id assign: ", variables
    if p[1] in optional.keys():
        optional[p[1]][0] = p[3]
        optional[p[1]][2] = True
        if DEBUG:
            print "Saw id assign: ", optional

def p_statement_assign(p):
    'statement : LET IDENTIFIER "=" expression'
    variables[p[2]] = p[4]
    if DEBUG:
        print "Saw statement assign", variables
    p[0] = [p[1], [p[2],p[4]]]
    # p[0] = p[4]

def p_statement_expr(p):
    'statement : expression'
    if DEBUG:
        print "Saw statement", p[1]
    print p[1]
    p[0] = p[1]

def p_expression_backslash(p):
    '''expression : LSTRING BSLASH expression RSTRING
    '''
    if DEBUG:
        print "backslash operator: ", p[3]
    p[0] = p[1] + str(p[3]) + p[4].replace(")",'',1)

def p_expression_backslash_question(p):
    '''expression : expression '?' '?' expression
    '''
    if p[1] in variables.keys():
        p[0] = variables[p[1]]
    elif p[1] in optional.keys():
        p[0] = optional[p[1]][0]
    else:
        p[0] = p[4]

def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression'''
    if p[2] == '+'  : p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]
    elif p[2] == '/': p[0] = p[1] / p[3]


def p_expression_str(p):
    '''expression : STRING '''
    if DEBUG:
        print "expression str: ", p[1]
    p[0] = p[1]

def p_expression_num(p):
    '''expression : INTEGER'''
    if DEBUG:
        print "expression num: ", p[1]
    p[0] = p[1]

def p_expression_id(p):
    '''expression : IDENTIFIER'''
    if p[1] in variables.keys():
        p[0] = variables[p[1]]
    elif p[1] in optional.keys():
        p[0] = optional[p[1]][0]
    else:
        print ("Undefined IDENTIFIER '%s'" % p[1])
        p[0] = 0
    # try:
    #     p[0] = variables[p[1]]
    #     p[0] = optional[p[1]][0]
    # except LookupError:
    #     print ("Undefined IDENTIFIER '%s'" % p[1])
    #     p[0] = 0

def p_type(p):
    '''type : INT
            | SSTRING
    '''

def emptyline(self):
    """Do nothing on empty input line"""
    pass# Error handling rule

# Error rule for syntax errors
def p_error(p):
    print "At line: ", p.lexer.lineno,
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

# Build the parser
# Use this if you want to build the parser using SLR instead of LALR
# yacc.yacc(method="SLR")
yacc.yacc()
