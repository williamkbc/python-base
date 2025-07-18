#!/usr/bin/env python
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala 
que frequenta cada uma das atividades.
"""
__version__ = "0.1.1"
__author__ = "Will"

sala1 = ["Erik", "Maia", "João", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["João", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês", aula_ingles),
    ("Música", aula_musica),
    ("Dança", aula_danca),
]

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades:


    print(f"Alunos da Atividade: {nome_atividade}\n")
    print("-" * 40)

    # sala1 que tem interseção com atividade
    atividade_sala1 = set(sala1) & set(atividade)
    # sala que tem interseção com atividade
    atividade_sala2 = set(sala2).intersection(set(atividade))


   # for aluno in atividade:
   #     if aluno in sala1:
   #         atividade_sala1.append(aluno)
   #     elif aluno in sala2:
   #         atividade_sala2.append(aluno)
    print(f"{nome_atividade} sala 1 ", atividade_sala1)
    print(f"{nome_atividade} sala 2 ", atividade_sala2)
    print()
    print("#" * 40)
    print()