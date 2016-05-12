#------------------------------------------------------------
# lex.py
#
# tokenizer
# ------------------------------------------------------------

import ply.lex as lex

# List of token names.   
tokens = ('LET', 'PRINT', 'SSTRING', 'INT', 'INTEGER', 'STRING', 'IDENTIFIER', 'LSTRING', 'RSTRING', 'BSLASH', 'NIL')
literals =  ['=', '+', '-', '/', '*', ':', ',', '(', ')', '[', ']', '{', '}', '!', '?']

# Reserved words
reserved = {
    'LET' : 'let',
    'PRINT' : 'print',
    'INT' : 'int',
    'NIL' : 'nil'
}

# t_BSLASH = r'\\'
def t_BSLASH(t):
    r'\\[(]'
    return t

def t_SSTRING(t):
    r'String'
    return t

# Regular expression rules for simple tokens

def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)    
    except ValueError:
        print "Line %d: Number %s is too large!" % (t.lineno,t.value)
        t.value = 0
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reserved:
        t.type = t.value.upper()
        print 'Identifier', t
    return t

def t_STRING(t):
    r'"[a-zA-Z0-9_+\*\- :,.]*"'
    t.type = reserved.get(t.value,'STRING')    # Check for reserved words
    return t

def t_LSTRING(t):
    r'"[a-zA-Z0-9_+\*\- :,.]*'
    return t

def t_RSTRING(t):
    r'[)][a-zA-Z0-9_+\*\- :,.]*"'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lex.lex()

if __name__ == '__main__':
    lex.runmain()
