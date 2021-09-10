# reserverd word
reserved_words = {
    'or':       'res_or',
    'and':      'res_and',
    'not':      'res_not'
}


# name of tokens
tokens = [
    'tk_uneq',
    'tk_eq',
    'tk_gteq',
    'tk_gt',
    'tk_lseq',
    'tk_ls',
    'tk_add',
    'tk_sub',
    'tk_mult',
    'tk_div',
    'tk_par_o',
    'tk_par_c',
    'tk_id'
] + list(reserved_words.values())


#definition of tokens
t_tk_uneq       = r'!='
t_tk_eq       = r'=='
t_tk_gteq       = r'>='
t_tk_gt         = r'>'
t_tk_lseq       = r'<='
t_tk_ls         = r'<'
t_tk_add        = r'\+'
t_tk_sub        = r'-'
t_tk_mult       = r'\*'
t_tk_div        = r'/'
t_tk_par_o      = r'\('
t_tk_par_c      = r'\)'
#t_tk_id         = r'[A-Za-z][A-Za-z0-9_]*'

#definition of tokens most complex

def t_tk_id(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    t.type = reserved_words.get(t.value.lower(), "tk_id")
    t.value = t.value.lower()
    return t

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
    
#methods
temp = 0
def new_temp() -> str:
    global temp
    temp += 1
    return f't{temp}'

label = 0
def new_label() -> str:
    global label
    label += 1
    return f'L{label}'


def get_labels(list_label) -> str:

    labels = ""

    for item in list_label:
        if item == list_label[-1]:
            labels += item
            continue
        labels += f'{item},'

    return labels


#Definition Grammar

start = 'S'

##-------------Production S-------------##
def p_S(t):
    'S : L'

    t[0] = t[1]

##-------------Production L-------------##
def p_L_or(t):
    'L : L res_or A'

    t[0] = {'c3d': f"{t[1]['c3d']}\n\t{get_labels(t[1]['LF'])}:\n\t{t[3]['c3d']}", 'LV': t[1]['LV'] + t[3]['LV'], 'LF': t[3]['LF']}

def p_L_A(t):
    'L : A'

    t[0] = t[1]


##-------------Production A-------------##
def p_A_and(t):
    'A : A res_and N'
    
    t[0] = {'c3d': f"{t[1]['c3d']}\n\t{get_labels(t[1]['LV'])}:\n\t{t[3]['c3d']}", 'LV': t[3]['LV'], 'LF': t[1]['LF'] + t[3]['LF']}

def p_A_N(t):
    'A : N'

    t[0] = t[1]

##-------------Production N-------------##
def p_N_not(t):
    'N : res_not R'

    t[0] = {'c3d': t[2]['c3d'], 'LV': t[2]['LF'], 'LF': t[2]['LV']}

def p_N_R(t):
    'N : R'

    t[0] = t[1]

##-------------Production R-------------##
def p_R(t):
    '''R : R tk_eq E
         | R tk_uneq E
         | R tk_gteq E
         | R tk_gt E
         | R tk_lseq E
         | R tk_ls E '''
    
    ltrue = new_label()
    lfalse = new_label()

    if t[2] == '==':
        t[0] = {'c3d': f"{t[1]['c3d']}{t[3]['c3d']}if {t[1]['tmp']} {t[2]} {t[3]['tmp']} goto {ltrue}\n\tgoto {lfalse}", 'LV': [ltrue], 'LF': [lfalse]}
    elif t[2] == '!=':
        t[0] = {'c3d': f"{t[1]['c3d']}{t[3]['c3d']}if {t[1]['tmp']} {t[2]} {t[3]['tmp']} goto {ltrue}\n\tgoto {lfalse}", 'LV': [ltrue], 'LF': [lfalse]}
    elif t[2] == '>=':
        t[0] = {'c3d': f"{t[1]['c3d']}{t[3]['c3d']}if {t[1]['tmp']} {t[2]} {t[3]['tmp']} goto {ltrue}\n\tgoto {lfalse}", 'LV': [ltrue], 'LF': [lfalse]}
    elif t[2] == '>':
        t[0] = {'c3d': f"{t[1]['c3d']}{t[3]['c3d']}if {t[1]['tmp']} {t[2]} {t[3]['tmp']} goto {ltrue}\n\tgoto {lfalse}", 'LV': [ltrue], 'LF': [lfalse]}
    elif t[2] == '<=':
        t[0] = {'c3d': f"{t[1]['c3d']}{t[3]['c3d']}if {t[1]['tmp']} {t[2]} {t[3]['tmp']} goto {ltrue}\n\tgoto {lfalse}", 'LV': [ltrue], 'LF': [lfalse]}
    elif t[2] == '<':
        t[0] = {'c3d': f"{t[1]['c3d']}{t[3]['c3d']}if {t[1]['tmp']} {t[2]} {t[3]['tmp']} goto {ltrue}\n\tgoto {lfalse}", 'LV': [ltrue], 'LF': [lfalse]}

def p_R_E(t):
    'R : E'

    t[0] = t[1]

##-------------Production E-------------##
def p_E_add(t):
    'E : E tk_add T'

    temp =  new_temp()
    t[0] = {'tmp': temp, 'c3d': f"{t[1]['c3d']}{t[3]['c3d']}{temp} = {t[1]['tmp']} + {t[3]['tmp']}\n\t"}

def p_E_sub(t):
    'E : E tk_sub T'

    temp =  new_temp()
    t[0] = {'tmp': temp, 'c3d': f"{t[1]['c3d']}{t[3]['c3d']}{temp} = {t[1]['tmp']} - {t[3]['tmp']}\n\t"}

def p_E_T(t):
    'E : T'

    t[0] = t[1]

##-------------Production T-------------##
def p_T_mult(t):
    'T : T tk_mult F'

    temp =  new_temp()
    t[0] = {'tmp': temp, 'c3d': f"{t[1]['c3d']}{t[3]['c3d']}{temp} = {t[1]['tmp']} * {t[3]['tmp']}\n\t"}

def p_T_div(t):
    'T : T tk_div F'

    temp =  new_temp()
    t[0] = {'tmp': temp, 'c3d': f"{t[1]['c3d']}{t[3]['c3d']}{temp} = {t[1]['tmp']} / {t[3]['tmp']}\n\t"}

def p_T_F(t):
    'T : F'

    t[0] = t[1]

##-------------Production F-------------##
def p_F_agroup(t):
    'F : tk_par_o L tk_par_c'

    t[0] = t[2]

def p_F_id(t):
    'F : tk_id'

    t[0] = {'tmp': t[1], 'c3d': '' }


from os import read
import ply.lex as lex
import ply.yacc as yacc

lexer = lex.lex()
parser = yacc.yacc()

# print('Input:\nvar1 + var2 < var3 - var4\n')
# output = parser.parse('var1 > var2 and var3 > var4 or not var5 > var6')
# print(f"Out:\n{output['c3d']}\n{get_labels(output['LV'])} - {get_labels(output['LF'])}")

with open('inputs.txt', 'r') as inputs:
    readme = '''>## Elian Saúl Estrada Urbina
>### 201806838

# Code intermide generator of aritmethic expression
'''
    count = 1
    while True:
        line = inputs.readline().replace('\n', '')

        if line != '':
            result = parser.parse(line)
            readme += f'{count}. ### Input:\n\t```python=\n\t{line}\n\t```\n'
            readme += f"\t### Output:\n\t```python=\n\t{result['c3d']}"
            if result.get('LV', None) != None:
                readme += f"\n\n\tLV: {get_labels(result['LV'])}\n\tLF: {get_labels(result['LF'])}\n\t"

            readme += "```\n"
            temp = 0
            label = 0
            count += 1
            continue
        break

with open('README.md', 'w') as file:
    file.write(readme)