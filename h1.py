#!/usr/bin/env python
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
__version__ = "0.1.2"
__author__ = "William L Santos"
__license__ = "Unlicense"
# Dunder signifies "double underscore" e é usado para denotar métodos especiais em Python.

import os


current_language = os.getenv("LANG")[:5] # Obtém a variável de ambiente LANG do sistema

# sets (Hash Table) - O(1) - Constante
# dicts (Hash Table) - O(1) - Constante
# Ordem de complexidade O(n) - Verifica a variável de ambiente LANG
# e define a mensagem de saudação de acordo com o idioma configurado.

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_ES": "¡Hola, Mundo!",
    "fr_FR": "Bonjour, le monde!",  
    "de_DE": "Hallo, Welt!",
    "ja_JP": "こんにちは、世界！",        
    "zh_CN": "你好，世界！",
    "ru_RU": "Привет, мир!",    
    "ar_SA": "مرحبا بالعالم!",
    "ko_KR": "안녕하세요, 세계!",   
    "hi_IN": "नमस्ते, दुनिया!",
    "tr_TR": "Merhaba, Dünya!",
    "pt_PT": "Olá, Mundo!",
    "nl_NL": "Hallo, Wereld!",
    "sv_SE": "Hej, världen!",
    "pl_PL": "Witaj, świecie!",
    "da_DK": "Hej, verden!",
    "fi_FI": "Hei, maailma!",
    "no_NO": "Hei, verden!",    
    "cs_CZ": "Ahoj, světe!",
    "hu_HU": "Helló, világ!",
    "ro_RO": "Salut, lume!",
    'bg_BG': "Здравей, свят!",  
    "el_GR": "Γειά σου, Κόσμε!",
    "th_TH": "สวัสดี, โลก!",
    "vi_VN": "Xin chào, Thế giới!",
    "id_ID": "Halo, Dunia!",
    "ms_MY": "Halo, Dunia!",
    "tl_PH": "Kamusta, Mundo!",
    "uk_UA": "Привіт, Світ!",
    "fa_IR": "سلام، دنیا!",
    "iw_IL": "שלום, עולם!",
    "sr_RS": "Здраво, Свете!",
    "sk_SK": "Ahoj, svet!",
    "lt_LT": "Sveikas, pasauli!", 
    "lv_LV": "Sveika, pasaule!", 
    "et_EE": "Tere, maailm!"


}


# Exibe a mensagem de saudação na língua configurada
# O(1) - Constante
print(msg[current_language])
