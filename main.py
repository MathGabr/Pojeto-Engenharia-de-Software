from pack.bib import *

while(True):
    resp=int(input(f"\nSelecione o Exercicio que deseja executar (escreva exit para sair)\nR: "))

    if resp == 1:
        num=int(input("\nInsira um número: "))
        exercicio1(num)     
