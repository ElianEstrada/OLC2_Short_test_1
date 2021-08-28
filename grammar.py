
# name of tokens
tokens = [
    'tk_add',
    'tk_sub',
    'tk_mult',
    'tk_div',
    'tk_par_o',
    'tk_par_c',
    'tk_assign',
    'tk_id'
]


#definition of tokens
t_tk_add        = r'\+'
t_tk_sub        = r'-'
t_tk_mult       = r'\*'
t_tk_div        = r'/'
t_tk_par_o      = r'\('
t_tk_par_c      = r'\)'
t_tk_assign     = r'='
t_tk_id         = r'[A-Za-z][A-Za-z0-9_]*'

#definition of tokens most complex

# def t_tk_id(t):
#     r'[A-Za-z][A-Za-z0-9_]*'

#     return t

#ignorated character
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print(f'The character: {t.value[0]} is not defined in the alphabet')
    t.lexer.skip(1)

# import ply.lex as lex
# lexer = lex.lex()
    

#Definition Grammar

start = 'S'

##-------------Production S-------------##
def p_S(t):
    'S : E'

    t[0] = print(t[1])

##-------------Production E-------------##
def p_E_add(t):
    'E : E tk_add T'

    t[0] = t[1]

def p_E_sub(t):
    'E : E tk_sub T'

    t[0] = t[1]

def p_E_T(t):
    'E : T'

    t[0] = t[1]

##-------------Production T-------------##
def p_T_mult(t):
    'T : T tk_mult F'

    t[0] = t[1]

def p_T_div(t):
    'T : T tk_div F'

    t[0] = t[1]

def p_T_F(t):
    'T : F'

    t[0] = t[1]

##-------------Production F-------------##
def p_F_agroup(t):
    'F : tk_par_o E tk_par_c'

    t[0] = t[2]

def p_F_id(t):
    'F : tk_id'

    t[0] = t[1]


import ply.lex as lex
import ply.yacc as yacc

lexer = lex.lex()
parser = yacc.yacc()

print(parser.parse('var1 + var2'))

