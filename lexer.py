import ply.lex as lex

tokens = ('NUMBER','EQUAL','PLUS','MINUS','TIMES','DIVIDE','LPAREN','RPAREN','foreach','do','while','until',
          'ID','L_CBRACES','R_CBRACES','SEMI_COLON','DOLLAR','AT','loe','goe','eq','great','less','COMMA')

reserved={'do':'do','while':'while','foreach':'foreach','until':'until'}

t_ignore = ' \t\n' 
t_SEMI_COLON=r'\;'
t_DOLLAR = r'\$'
t_AT = r'\@'
t_L_CBRACES=r'\{'
t_R_CBRACES=r'\}'
t_LPAREN=r'\('
t_RPAREN=r'\)'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_loe = r'<='
t_goe = r'>='
t_eq = r'=='
t_great = r'>'
t_less = r'<'
t_NUMBER = r'\d+'
t_COMMA = r','
t_EQUAL = r'='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID') 
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t): 
    print(f"Illegal character'{t.value[0]}'")
    t.lexer.skip(1)

lexer=lex.lex()