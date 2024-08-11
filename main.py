from lexer import lexer
from parser import parser

file_name=r'.\sample.txt'

with open(file_name,'r')as file:
    data=file.read()

parser.parse(data)