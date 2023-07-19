
#pip install nltk matplotlib
import nltk
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from urllib import request

def leer_url(url):
    response = request.urlopen(url)
    text = response.read().decode('utf-8')
    return text

url_usuario = input("Ingresa la URL: ")
# (campos) https://raw.githubusercontent.com/corinaspo01/tfm1/main/campos.txt?token=GHSAT0AAAAAACFGO2ZMJHFFMRMHHVZJ432EZFYBF6A
# (caeiro) https://raw.githubusercontent.com/corinaspo01/tfm1/main/caeiro.txt?token=GHSAT0AAAAAACFGO2ZN5IE3I5HGMQII4SHAZFYBFKA
# (reis) https://raw.githubusercontent.com/corinaspo01/tfm1/main/reis.txt?token=GHSAT0AAAAAACFGO2ZMULD3OPLST7OTC756ZFYBETA
texto = leer_url(url_usuario)
print(texto)

from nltk.tokenize import WordPunctTokenizer
import string

excluir = ['el', "del", "se", "es", "al", "me", "son", "»", "«", "te", 'el', "si", 'que', "ya", "lo", "ti", "no", "ni", "sí", 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'y', 'o', 'pero', 'por', 'para', 'con', 'sin', 'de', 'a', 'en', 'si', 'mi', 'mis', 'tu', 'tus', 'su', 'sus', '¡', '...', '-,', '¿']

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
word_tokens = limpiar_palabras(punctokens)

print(word_tokens)
#palabras más comunes
from nltk import FreqDist
def frecuencia_palabras(word_tokens):
    frecuencias = FreqDist(word_tokens)
    common = frecuencias.most_common(50)
    plot = frecuencias.plot(50, cumulative= False)
    return plot
frecuencia = frecuencia_palabras(word_tokens)

print(frecuencia)
from nltk import sent_tokenize
def tokenizar_frases(texto):
    tokens = sent_tokenize(texto)
    return tokens
sent_token = tokenizar_frases(texto)
print (sent_token)
# Riqueza léxica
def riqueza_lexica(word_tokens):
    Ntokens = len(word_tokens)
    Ntipos = len(set(word_tokens))
    rique = Ntipos / Ntokens
    return rique

respuesta_riqueza_lexica = riqueza_lexica(word_tokens)
print(respuesta_riqueza_lexica)
def calcular_riqueza_lexica(sent_token):
    Ntokens = len(sent_token)
    Ntipos = len(set(sent_token))
    rique = Ntipos / Ntokens
    return rique

respuesta_riqueza_lexica = calcular_riqueza_lexica(sent_token)
print(respuesta_riqueza_lexica)

import nltk
from nltk import sent_tokenize

def obtener_categorias_gramaticales(texto):
    # Tokenizar las frases
    frases = nltk.sent_tokenize(texto)

    # Inicializar una lista para almacenar las categorías gramaticales
    categorias_gramaticales = []

    # Recorrer cada frase y obtener las categorías gramaticales
    for frase in frases:
        # Tokenizar las palabras de la frase
        palabras = nltk.word_tokenize(frase)
        # Etiquetar gramaticalmente las palabras de la frase
        etiquetas = nltk.pos_tag(palabras)
        # Obtener las categorías gramaticales de las palabras en la frase
        categorias = [tag for _, tag in etiquetas]
        # Agregar las categorías gramaticales a la lista
        categorias_gramaticales.append(tuple(categorias))  # Convertir la lista en una tupla

    return categorias_gramaticales

def obtener_formaciones_sintacticas(categorias_palabras_frases):
    # Calcular las frecuencias de las formaciones sintácticas
    frecuencias = nltk.FreqDist(categorias_palabras_frases)

    # Obtener las 5 formaciones sintácticas más comunes
    formaciones_sintacticas_comunes = frecuencias.most_common(5)

    return formaciones_sintacticas_comunes

# Tu URL o texto

texto = leer_url(url_usuario)

# Obtener las categorías gramaticales de las palabras en cada frase utilizando la función
categorias_palabras_frases = obtener_categorias_gramaticales(texto)

# Obtener las formaciones sintácticas más comunes utilizando la función
formaciones_comunes = obtener_formaciones_sintacticas(categorias_palabras_frases)

# Imprimir las formaciones sintácticas más comunes
print("Formaciones sintácticas más comunes:", formaciones_comunes)

#pip install pysentimiento
from pysentimiento import create_analyzer
analyzer = create_analyzer(task="sentiment", lang="es")

analyzer.predict("Qué gran jugador es Messi")