import ply.yacc as yacc
from lexer import tokens

def p_main(p):
    '''main : Statements'''
    print("Syntax is Correct.")

def p_Statements(p): 
    '''Statements : Statement Statements
                |   Statement'''

def p_Statement(p): 
    '''Statement :  assign SEMI_COLON Statements
                  | expression SEMI_COLON Statements
                  | list SEMI_COLON Statements
                  | do L_CBRACES Statements R_CBRACES while LPAREN COND RPAREN SEMI_COLON Statements
                  | until LPAREN COND RPAREN L_CBRACES Statements R_CBRACES Statements
                  | foreach DOLLAR ID LPAREN list RPAREN L_CBRACES Statements R_CBRACES Statements
                  | declaration Statements
                  | '''
    
def p_declaration(p):
    'declaration : var_list SEMI_COLON'

def p_var_list(p):
    '''var_list : DOLLAR ID
                | DOLLAR ID COMMA var_list
                | DOLLAR ID EQUAL expression
                | DOLLAR ID EQUAL expression COMMA var_list'''

def p_COND(p): 
    '''COND : DOLLAR ID rel DOLLAR ID
            | expression rel expression
            | expression rel DOLLAR ID
            | DOLLAR ID rel expression'''

def p_rel(p):
    '''rel : goe 
	   | loe 
	   | great 
	   | less 
	   | eq '''
    
def p_assign(p):
    'assign : DOLLAR ID EQUAL expression'
  
def p_expression(p):
    '''expression : expression PLUS term
		  | expression MINUS term
		  | expression TIMES term
		  | expression DIVIDE term
		  | LPAREN expression RPAREN
		  | term'''
    
def p_list(p):
    '''list : AT ID '''

def p_term(p):
    '''term : NUMBER
	      | DOLLAR ID'''			
    
def p_error(p): 
    print("Syntax error!")
    exit(1)

parser = yacc.yacc()
