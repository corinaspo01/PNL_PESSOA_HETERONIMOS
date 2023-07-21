#pip install nltk matplotlib
import nltk
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from urllib import request


def leer_url(url):
    response = request.urlopen(url)
    text = response.read().decode('utf-8')
    return text

url_usuario = input("Ingresa la URL: ") #raw de txt en github
texto = leer_url(url_usuario)
print(texto)

#TOKENIZACIÓN Y LIMPIEZA

from nltk import sent_tokenize
from nltk import WordPunctTokenizer
import string
def token_simple (texto):
    frases = sent_tokenize(texto)
    tokenizer = WordPunctTokenizer()
    tokenst = tokenizer.tokenize(texto)
    return tokenst
def limpiar_palabras(tokens):
    # Eliminar signos de puntuación y convertir a minúsculas
    tokens_limpio = [token.lower() for token in tokens if token not in string.punctuation]
    return tokens_limpio

# Tokenizar el texto
tokenizertext = token_simple(texto)

# Limpiar los tokens y excluir palabras no deseadas
tokenss = limpiar_palabras(tokenizertext)

print(tokenss)
#LIMPIEZA DE TOKENS (PALABRAS)

excluir = ['el', 'como', "cuando", 'más',"eso", "le", 'qué', "sólo", "porque", 'i', "del", "se", "es", "al", "me", "son", "»", "«", "te", 'el', "si", 'que', "ya", "lo", "ti", "no", "ni", "sí", 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'y', 'o', 'pero', 'por', 'para', 'con', 'sin', 'de', 'a', 'en', 'si', 'mi', 'mis', 'tu', 'tus', 'su', 'sus', '¡', '...', '-,', '¿']

def punc_pal(texto):
    tokenizer = WordPunctTokenizer()
    tokens = tokenizer.tokenize(texto)
    return tokens

def limpiar_palabras(tokens):
    # Eliminar signos de puntuación y convertir a minúsculas
    tokens_limpio = [token.lower() for token in tokens if token not in string.punctuation]
    # Filtrar palabras no deseadas
    tokens_filtrados = [token for token in tokens_limpio if token not in excluir]
    return tokens_filtrados

# Tokenizar el texto
punctokens = punc_pal(texto)

# Limpiar los tokens y excluir palabras no deseadas
tokens_limpios = limpiar_palabras(punctokens)

print(tokens_limpios)
#PALABRAS MÁS USADAS

from nltk import FreqDist
def frecuencia_palabras(tokens_limpios):
    frecuencias = FreqDist(tokens_limpios)
    common = frecuencias.most_common(50)
    
    # Obtener solo las palabras más comunes en una lista
    palabras_comunes = [palabra for palabra, frecuencia in common]

    # Imprimir la lista de palabras más comunes
    print("Palabras más comunes:")
    print(palabras_comunes)

    # Imprimir el gráfico de frecuencia
    frecuencias.plot(50, cumulative=False)

frecuencia_palabras(tokens_limpios)
# RIQUEZA LÉXICA

def riqueza_lexica(tokenss):
    Ntokens = len(tokenss)
    Ntipos = len(set(tokenss))
    rique = Ntipos / Ntokens
    return rique

respuesta_riqueza_lexica = riqueza_lexica(tokenss)
print(respuesta_riqueza_lexica)
# RIQUEZA LÉXICA 2

def riqueza_lexica(tokens_limpios):
    Ntokens = len(tokens_limpios)
    Ntipos = len(set(tokens_limpios))
    rique = Ntipos / Ntokens
    return rique

respuesta_riqueza_lexica = riqueza_lexica(tokens_limpios)
print(respuesta_riqueza_lexica)
#CATEGORÍA GRAMATICAL MÁS COMÚN

import nltk
def obtener_categorias_mas_utilizadas(tokenss, top_n=10):
    pos_tags = nltk.pos_tag(tokenss)
    tags_only = [tag for _, tag in pos_tags]
    frecuencias = nltk.FreqDist(tags_only)
    common_tags = frecuencias.most_common(top_n)
    return common_tags

categorias_mas_utilizadas = obtener_categorias_mas_utilizadas(tokenss)

print("Categorías gramaticales más utilizadas:")
for tag, count in categorias_mas_utilizadas:
    print(f"{tag}: {count}")
#TOKENIZAR FRASES


from nltk import sent_tokenize
def tokenizar_frases(texto):
    tokens = sent_tokenize(texto)
    return tokens
sent_token = tokenizar_frases(texto)
print (sent_token)
#FORMACIONES SINTACTICAS EN CATEGORÍA GRAMATICAL


def obtener_formaciones_sintacticas_mas_frecuentes(sent_token, top_n=10):
    formaciones_sintacticas = []
    for sentence in sent_token:
        word_tokens = limpiar_palabras(punc_pal(sentence))
        pos_tags = nltk.pos_tag(word_tokens)
        formations = ' '.join(tag for _, tag in pos_tags[:3])
        formaciones_sintacticas.append(formations)

    frecuencias = nltk.FreqDist(formaciones_sintacticas)
    common_formaciones = frecuencias.most_common(top_n)
    return common_formaciones

sent_token = tokenizar_frases(texto)
formaciones_sintacticas_mas_frecuentes = obtener_formaciones_sintacticas_mas_frecuentes(sent_token)

print("Formaciones sintácticas expresadas en categorías gramaticales más frecuentes:")
for formation, count in formaciones_sintacticas_mas_frecuentes:
    print(f"{formation}: {count}")
#TEMPORAL 

#oraciones más largas que contienen sustantivos (NN) en una secuencia
def identificar_oraciones_con_formacion(sent_token):
    oraciones_con_formacion = []
    for sentence in sent_token:
        word_tokens = limpiar_palabras(punc_pal(sentence))
        pos_tags = nltk.pos_tag(word_tokens)
        formaciones = [tag for _, tag in pos_tags]
        if len(formaciones) >= 3:
            for i in range(len(formaciones) - 2):
                if formaciones[i] == 'NN' and formaciones[i + 1] == 'NN' and formaciones[i + 2] == 'NN':
                    oraciones_con_formacion.append(sentence)
                    break

    return oraciones_con_formacion

sent_token = tokenizar_frases(texto)
oraciones_con_formacion = identificar_oraciones_con_formacion(sent_token)

# Obtener las oraciones más comunes que contienen la formación "NN NN NN"
def obtener_oraciones_mas_comunes(oraciones, top_n=10):
    frecuencias = nltk.FreqDist(oraciones)
    oraciones_comunes = frecuencias.most_common(top_n)
    return oraciones_comunes

oraciones_mas_comunes = obtener_oraciones_mas_comunes(oraciones_con_formacion)

print("Oraciones más comunes con la formación 'NN NN NN':")
for oracion, count in oraciones_mas_comunes:
    print(f"{oracion}: {count}")
from nltk import Text
textoS = Text(tokenss)
#palabras que tienden a aparecer juntas con una frecuencia inusualmente alta 
textoS.collocations()
from nltk import Text
textoL = Text(tokens_limpios)
#palabras que tienden a aparecer juntas con una frecuencia inusualmente alta 
textoL.collocations()
textoS.concordance('yo')
textoL.similar('yo')
textoL.common_contexts(['yo', 'estar'])
textoL.common_contexts(['yo', 'existir']) 
der_flor = set([tok for tok in tokenss if 'flor' in tok])

for der in der_flor:
    print(textoS.concordance(der))

textoS.dispersion_plot(list(der_flor))
#pip install pysentimiento
#pip install --upgrade pysentimiento
#pip install transformers[torch]
from pysentimiento import create_analyzer

analyzer = create_analyzer(task="sentiment", lang="es")

analyzer.predict(tokenss)


emotion_analyzer = create_analyzer(task="emotion", lang="es")

emotion_analyzer.predict(tokenss)

hate_speech_analyzer = create_analyzer(task="hate_speech", lang="es")

hate_speech_analyzer.predict(tokenss)