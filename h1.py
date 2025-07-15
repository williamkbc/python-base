#!/usr/bin/env python3
"""H1 Multi Language Hello World.
Este programa imprime uma mensagem de saudação em várias línguas.
Dependendo da lingua configurada no sistema, 
o programa exibe a mensagem correspondente.
Se a lingua não for reconhecida, o programa exibe a mensagem em inglês.

Como Usar:

Tenha a variável de ambiente LANG configurada com o idioma desejado.
Exemplo:

    export LANG=pt_BR

Execução:
    python3 h1.py
    ou
    ./hello.py
Requisitos:
    - Python 3.x instalado
"""
__version__ = "0.0.1"
__author__ = "William L Santos"
__license__ = "Unlicense"
# Dunder signifies "double underscore" e é usado para denotar métodos especiais em Python.

import os


current_language = os.getenv("LANG")[:5] # Obtém a variável de ambiente LANG do sistema

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_ES":
    msg = "¡Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, le monde!"
elif current_language == "de_DE":
    msg = "Hallo, Welt!"
elif current_language == "ja_JP":
    msg = "こんにちは、世界！"
elif current_language == "zh_CN":
    msg = "你好，世界！"
elif current_language == "ru_RU":
    msg = "Привет, мир!"
elif current_language == "ar_SA":
    msg = "مرحبا بالعالم!"
elif current_language == "ko_KR":
    msg = "안녕하세요, 세계!"
elif current_language == "hi_IN":
    msg = "नमस्ते, दुनिया!"
elif current_language == "tr_TR":
    msg = "Merhaba, Dünya!"

print(msg)
