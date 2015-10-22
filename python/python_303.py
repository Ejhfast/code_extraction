# Equation parsing in Python
import compiler
eq= "sin(x)*x**2"
ast= compiler.parse( eq )
