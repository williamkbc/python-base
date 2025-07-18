#!/usr/bin/env python3

"""Envia emails para clientes.

Este programa lê um arquivo de clientes e envia um email para cada um deles.
O arquivo deve conter o nome e o email de cada cliente, separados por vírgula.
"""
__version__ = "0.1.1"

import sys
import os


arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo de clientes")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]


path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)


clientes = []
for line in open(filepath):
    name, email = line.split(",")
    # TODO: substituir por envio de email 
    print(f"Enviando email para: {email}")
    print()
    print(
        open(templatepath).read() 
        %{
            "nome": name,
            "produtos": "caneta",
            "texto": "Escrever melhor",
            "link": "http://www.acaneta.com.br",
            "quantidade": 1,
            "preco": 50.5,
            
        }
    )
    print("-" * 40)