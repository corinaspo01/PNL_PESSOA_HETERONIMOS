import nltk
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

from urllib import request
url = 'file:///C:/Users/Usuario/TFM/campos.txt'
response = request.urlopen(url)
campos = response.read().decode('utf-8')
print(campos)

#tokenizar frases
from nltk import sent_tokenize
frasescampos = sent_tokenize(campos)
print (frasescampos)

#obtener las oraciones más comunes
from nltk import FreqDist
frecuencias = FreqDist(frasescampos)
print(frecuencias.most_common(50))
frecuencias.plot(50, cumulative= False)

#generada
# Etiquetado gramatical y obtención de formaciones sintácticas
formaciones_sintacticas = []
# Recorrer cada frase y obtener las etiquetas gramaticales
for frase in frasescampos:
    # Tokenizar las palabras de la frase
    palabras = nltk.word_tokenize(frase)
    # Etiquetar gramaticalmente las palabras de la frase
    etiquetas = nltk.pos_tag(palabras)
    # Obtener la secuencia de etiquetas gramaticales
    secuencia_etiquetas = [tag for _, tag in etiquetas]
    # Agregar la secuencia de etiquetas gramaticales a la lista
    formaciones_sintacticas.append(tuple(secuencia_etiquetas))
# Calcular las frecuencias de las formaciones sintácticas
frecuencias = nltk.FreqDist(formaciones_sintacticas)
# Obtener la formación sintáctica más común
formacion_sintactica_comun = frecuencias.most_common(5)
print("Formación sintáctica más común:", formacion_sintactica_comun)

#tokenizar palabras
from nltk import WordPunctTokenizer
tokenizer = WordPunctTokenizer()
palabrascampos = tokenizer.tokenize(campos)
print(palabrascampos)

#riqueza lexica
Ntokens = len(palabrascampos)
Ntipos = len(set(palabrascampos))
print(Ntipos/Ntokens)

#palabras más comunes
from nltk import FreqDist
frecuencias = FreqDist(palabrascampos)
print(frecuencias.most_common(50))
frecuencias.plot(50, cumulative= False)

#tomada de taller
#limpieza de palabras
palabrascampos = [tok.lower() for tok in palabrascampos if tok.isalpha()==True]
print(len(set(palabrascampos))/ len(palabrascampos))
from nltk.corpus import stopwords
stop_es = stopwords.words('spanish')
TOKENS = [t for t in palabrascampos if not t in stop_es ]
print(len(set(TOKENS))/len(TOKENS))
FRECUENCIAS = FreqDist(TOKENS)
FRECUENCIAS.plot(50, cumulative=False)

pos_tags = nltk.pos_tag(palabrascampos)
etiquetas_gramaticales = [tag for _, tag in etiquetas]
# Obtener la formación sintáctica más común
categoria_gramatical_comun = nltk.FreqDist(etiquetas_gramaticales).most_common(5)
print("Caategoría gramatical común:", categoria_gramatical_comun)

from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
sentimientoscampos = sia.polarity_scores(campos)
print (sentimientoscampos)