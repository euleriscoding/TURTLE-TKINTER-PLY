import yacc
from lexing import tokens
#PARSER
import yacc
def p_start(p):
    '''start : function option'''
    p[0]=(p[1],p[2])

def p_function(p):
    '''
    function : forward
             | right
             | color
             | pen
    '''
    p[0]=p[1] 

def p_empty(p):
    'empty :'
    pass
 
 
def p_option(p):
    '''option : start
              | empty '''
    p[0]=p[1]

def p_forward(p):
    'forward : FORW NUMBER' 
    
    p[0]=pattern.forward(p[2])
 
def p_right(p):
    'right : RIGHT NUMBER'
    
    p[0]=pattern.right(p[2])

def p_color(p):
    'color : COLOR colors'
    
def p_colors(p):
    '''colors : BLACK 
              | BLUE
               | GREEN
              | RED '''
    if p[1] == 'S':
        p[0]=pattern.color("black")
    elif p[1] == 'M':
        p[0]=pattern.color("blue")
    elif p[1] == 'Y':
        p[0]=pattern.color("green")
    elif p[1] == 'K':
        p[0]=pattern.color("red")

def p_pen(p):
    'pen : PEN NUMBER'
    if p[2] == 1:
        p[0]=pattern.pensize(1)
    elif p[2] == 2:
        p[0]=pattern.pensize(3)
    elif p[2] == 3:
        p[0]=pattern.pensize(5)

def p_error(p):
   print("Syntax error in input!")

# Build the parser

parser=yacc.yacc(debug=True)
from lexing import data
result=parser.parse(data)

#print (result)
