#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install beautifulsoup4


# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # Encontramos uma nova página
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")


# In[2]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages = set()
def getLinks(pageUrl):
global pages
html = urlopen("http://en.wikipedia.org"+pageUrl)
bsObj = BeautifulSoup(html)
try:
print(bsObj.h1.get_text())
print(bsObj.find(id ="mw-content-text").findAll("p")[0])
print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
except AttributeError:
print("This page is missing something! No worries though!")
for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
if 'href' in link.attrs:
if link.attrs['href'] not in pages:
#We have encountered a new page
newPage = link.attrs['href']
print("----------------\n"+newPage)
pages.add(newPage)
getLinks(newPage)
getLinks("")


# In[3]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0].get_text())
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something! No worries though!")
    
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print("----------------\n" + newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")



# In[4]:


pip install beautifulsoup4


# In[5]:


pip install scrapy


# In[1]:


I:\O meu disco\Traduções\UFMS\Nova pasta
    


# In[3]:


import scrapy

class G1Spider(scrapy.Spider):
    name = "g1_spider"
    start_urls = ['https://g1.globo.com/mundo/ucrania-russia/']

    def parse(self, response):
        # Encontra todos os links das notícias na página
        links = response.css('.feed-post-link::attr(href)').getall()

        # Filtra para obter apenas os 50 últimos links
        latest_links = links[:50]

        # Imprime os links das notícias
        for link in latest_links:
            print(link)

            


# In[4]:


scrapy runspider g1_spider.py


# In[5]:


import scrapy

class G1Spider(scrapy.Spider):
    name = "g1_spider"
    start_urls = ['https://g1.globo.com/mundo/ucrania-russia/']

    def parse(self, response):
        # Encontra todos os links das notícias na página
        links = response.css('.feed-post-link::attr(href)').getall()

        # Filtra para obter apenas os 50 últimos links
        latest_links = links[:50]

        # Imprime os links das notícias
        for link in latest_links:
            print(link)


# In[6]:


import scrapy
from scrapy_requests import requests

class CartaCapitalSpider(scrapy.Spider):
    name = "cartacapital_spider"
    start_urls = [
        "https://www.cartacapital.com.br/tag/russia/",
        "https://www.cartacapital.com.br/tag/ucrania/"
    ]
    collected_count = 0
    links = set()

    def parse(self, response):
        # Coletar links das notícias na página atual
        links = response.css('.feed-post-link::attr(href)').getall()
        for link in links:
            if link not in self.links:
                yield {'link': link}
                self.collected_count += 1
                self.links.add(link)

            if self.collected_count >= 50:
                return  # Interrompe a coleta quando atingir 50 notícias

        # Verificar se há mais páginas para carregar
        next_page = response.css('.load-more a::attr(href)').get()
        if next_page and self.collected_count < 50:
            yield requests.get(next_page, callback=self.parse)

    def closed(self, reason):
        # Função chamada ao finalizar o crawling
        with open('links_noticias.txt', 'w') as f:
            f.write('\n'.join(self.links))


# In[7]:


import scrapy
from scrapy_requests import request

class CartaCapitalSpider(scrapy.Spider):
    name = "cartacapital_spider"
    start_urls = [
        "https://www.cartacapital.com.br/tag/russia/",
        "https://www.cartacapital.com.br/tag/ucrania/"
    ]
    collected_count = 0
    links = set()

    def parse(self, response):
        # Coletar links das notícias na página atual
        links = response.css('.feed-post-link::attr(href)').getall()
        for link in links:
            if link not in self.links:
                yield {'link': link}
                self.collected_count += 1
                self.links.add(link)

            if self.collected_count >= 50:
                return  # Interrompe a coleta quando atingir 50 notícias

        # Verificar se há mais páginas para carregar
        next_page = response.css('.load-more a::attr(href)').get()
        if next_page and self.collected_count < 50:
            yield requests.get(next_page, callback=self.parse)

    def closed(self, reason):
        # Função chamada ao finalizar o crawling
        with open('links_noticias.txt', 'w') as f:
            f.write('\n'.join(self.links))


# In[8]:


import requests
from bs4 import BeautifulSoup

url = "https://www.cartacapital.com.br/tag/russia/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a", class_="post-title")

count = 0
for link in links:
    count += 1
    print(f"Link {count}: {link['href']}")
    
    if count >= 5:
        break


# In[9]:


import requests
from bs4 import BeautifulSoup

url = "https://www.cartacapital.com.br/tag/russia/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a", class_="post-title")

collected_links = []
count = 0
for link in links:
    count += 1
    collected_links.append(link["href"])
    print(f"Link {count}: {link['href']}")
    
    if count >= 5:
        break

print("\nLinks coletados:")
for link in collected_links:
    print(link)


# In[10]:


import requests
from bs4 import BeautifulSoup

url = "https://www.cartacapital.com.br/tag/russia/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a", class_="post-title")

collected_links = []
count = 0
for link in links:
    count += 1
    collected_links.append(link["href"])
    print(f"Link {count}: {link['href']}")
    
    if count >= 5:
        break

print("\nLinks coletados:")
for link in collected_links:
    print(link)


# In[11]:


import requests
from bs4 import BeautifulSoup

url = "https://www.cartacapital.com.br/tag/russia/"
collected_links = []
count = 0

while len(collected_links) < 50:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a", class_="c-post__url")

    for link in links:
        collected_links.append(link["href"])
        count += 1
        print(f"Link {count}: {link['href']}")
        
        if len(collected_links) >= 50:
            break

    next_page_link = soup.find("a", class_="pagination-next")
    if next_page_link:
        url = next_page_link["href"]
    else:
        break

print("\nLinks coletados:")
for link in collected_links:
    print(link)


# In[12]:


pip install spacy


# In[1]:


python -m spacy download pt_core_news_sm


# In[2]:


-m spacy download pt_core_news_sm


# In[1]:


python -m spacy download pt_core_news_sm


# In[2]:


import spacy

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Ler o arquivo das notícias
with open('noticias.txt', 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Lista para armazenar os sujeitos encontrados
sujeitos = []

# Percorrer as sentenças e identificar os sujeitos
for sent in doc.sents:
    for token in sent:
        if token.dep_ == 'nsubj':  # Verificar se é um sujeito
            sujeitos.append(token.text)

# Imprimir as palavras em posição de sujeito
for sujeito in sujeitos:
    print(sujeito)


# In[3]:


import spacy

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Ler o arquivo das notícias
with open('links_noticias.txt', 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Lista para armazenar os sujeitos encontrados
sujeitos = []

# Percorrer as sentenças e identificar os sujeitos
for sent in doc.sents:
    for token in sent:
        if token.dep_ == 'nsubj':  # Verificar se é um sujeito
            sujeitos.append(token.text)

# Imprimir as palavras em posição de sujeito
for sujeito in sujeitos:
    print(sujeito)


# In[4]:


import spacy

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\links_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Lista para armazenar os sujeitos encontrados
sujeitos = []

# Percorrer as sentenças e identificar os sujeitos
for sent in doc.sents:
    for token in sent:
        if token.dep_ == 'nsubj':  # Verificar se é um sujeito
            sujeitos.append(token.text)

# Imprimir as palavras em posição de sujeito
for sujeito in sujeitos:
    print(sujeito)


# In[5]:


import spacy

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\links_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Lista para armazenar os sujeitos encontrados com suas respectivas sentenças
sujeitos_sentencas = []

# Percorrer as sentenças e identificar os sujeitos
for sent in doc.sents:
    for token in sent:
        if token.dep_ == 'nsubj':  # Verificar se é um sujeito
            sujeitos_sentencas.append((token.text, sent.text))

# Imprimir as palavras em posição de sujeito e suas respectivas sentenças
for sujeito, sentenca in sujeitos_sentencas:
    print(f'Sujeito: {sujeito}')
    print(f'Sentença: {sentenca}\n')


# In[6]:


import spacy

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\links_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Lista para armazenar os sintagmas em posição de sujeito encontrados
sintagmas_sujeito = []

# Lista para armazenar as sentenças completas dos sintagmas em posição de sujeito
sentencas_sujeito = []

# Percorrer as sentenças e identificar os sintagmas em posição de sujeito
for sent in doc.sents:
    for token in sent:
        if token.dep_ == 'nsubj':  # Verificar se é um sujeito
            sintagmas_sujeito.append(token.text)
            sentencas_sujeito.append(sent.text)

# Imprimir os sintagmas em posição de sujeito e suas respectivas sentenças
for sintagma, sentenca in zip(sintagmas_sujeito, sentencas_sujeito):
    print(f'Sintagma: {sintagma}')
    print(f'Sentença: {sentenca}\n')


# In[3]:


import spacy

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\links_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Lista para armazenar os sintagmas em posição de sujeito encontrados
sintagmas_sujeito = []

# Lista para armazenar as sentenças completas dos sintagmas em posição de sujeito
sentencas_sujeito = []

# Variável para contar as sentenças com sujeito
contagem_sentencas_sujeito = 0

# Percorrer as sentenças e identificar os sintagmas em posição de sujeito
for i, sent in enumerate(doc.sents):
    has_subject = False
    for token in sent:
        if token.dep_ == 'nsubj':  # Verificar se é um sujeito
            has_subject = True
            sintagmas_sujeito.append(token.text)
            sentencas_sujeito.append(sent.text)
    if has_subject:
        contagem_sentencas_sujeito += 1

# Imprimir os sintagmas em posição de sujeito e suas respectivas sentenças
for sintagma, sentenca in zip(sintagmas_sujeito, sentencas_sujeito):
    print(f'Sintagma: {sintagma}')
    print(f'Sentença: {sentenca}\n')

# Imprimir a contagem de sentenças com sujeito
print(f"Quantidade de sentenças com sujeito: {contagem_sentencas_sujeito}")


# In[4]:


import spacy

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\links_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Lista para armazenar os sintagmas em posição de sujeito encontrados
sintagmas_sujeito = []

# Lista para armazenar as sentenças completas dos sintagmas em posição de sujeito
sentencas_sujeito = []

# Variável para contar as sentenças com sujeito
contagem_sentencas_sujeito = 0

# Lista para armazenar as sentenças passivas
sentencas_passivas = []

# Variável para contar as sentenças passivas
contagem_sentencas_passivas = 0

# Percorrer as sentenças e identificar os sintagmas em posição de sujeito e as sentenças passivas
for i, sent in enumerate(doc.sents):
    has_subject = False
    is_passive = False
    for token in sent:
        if token.dep_ == 'nsubj':  # Verificar se é um sujeito
            has_subject = True
            sintagmas_sujeito.append(token.text)
            sentencas_sujeito.append(sent.text)
        if token.dep_ == 'auxpass':  # Verificar se é uma construção passiva
            is_passive = True
    if has_subject:
        contagem_sentencas_sujeito += 1
    if is_passive:
        contagem_sentencas_passivas += 1
        sentencas_passivas.append(sent.text)

# Imprimir os sintagmas em posição de sujeito e suas respectivas sentenças
for sintagma, sentenca in zip(sintagmas_sujeito, sentencas_sujeito):
    print(f'Sintagma: {sintagma}')
    print(f'Sentença: {sentenca}\n')

# Imprimir a contagem de sentenças com sujeito
print(f"Quantidade de sentenças com sujeito: {contagem_sentencas_sujeito}")

# Imprimir as sentenças passivas
print(f"Quantidade de sentenças passivas: {contagem_sentencas_passivas}")
print("Sentenças passivas:")
for sentenca in sentencas_passivas:
    print(sentenca)

    


# In[7]:


import spacy

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\links_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Lista para armazenar os sintagmas em posição de sujeito encontrados
sintagmas_sujeito = []

# Lista para armazenar as sentenças completas dos sintagmas em posição de sujeito
sentencas_sujeito = []

# Variável para contar as sentenças com sujeito
contagem_sentencas_sujeito = 0

# Lista para armazenar as sentenças passivas
sentencas_passivas = []

# Variável para contar as sentenças passivas
contagem_sentencas_passivas = 0

# Definir a gramática para identificar as sentenças passivas
gramatica_passiva = [
    {"DEP": {"REGEX": "(nsubj)"}, "OP": "?"},
    {"DEP": "auxpass"},
    {"DEP": {"REGEX": "(past_part|advcl)"}, "OP": "?"},
    {"DEP": {"IN": ["obl", "nmod"]}, "OP": "*"}
]

# Adicionar a gramática ao pipeline do spaCy
matcher = spacy.matcher.Matcher(nlp.vocab)
matcher.add("PASSIVA", None, gramatica_passiva)

# Percorrer as sentenças e identificar os sintagmas em posição de sujeito e as sentenças passivas
for sent in doc.sents:
    has_subject = False
    is_passive = False
    for token in sent:
        if token.dep_ == 'nsubj':  # Verificar se é um sujeito
            has_subject = True
            sintagmas_sujeito.append(token.text)
            sentencas_sujeito.append(sent.text)
        if token.dep_ == 'auxpass':  # Verificar se é uma construção passiva
            is_passive = True
    if has_subject:
        contagem_sentencas_sujeito += 1
    if is_passive:
        contagem_sentencas_passivas += 1
        sentencas_passivas.append(sent.text)

# Imprimir os sintagmas em posição de sujeito e suas respectivas sentenças
for sintagma, sentenca in zip(sintagmas_sujeito, sentencas_sujeito):
    print(f'Sintagma: {sintagma}')
    print(f'Sentença: {sentenca}\n')

# Imprimir a contagem de sentenças com sujeito
print(f"Quantidade de sentenças com sujeito: {contagem_sentencas_sujeito}")

# Imprimir a contagem de sentenças passivas e as sentenças passivas encontradas
print(f"Quantidade de sentenças passivas: {contagem_sentencas_passivas}")
print("Sentenças passivas:")
for sentenca in sentencas_passivas:
    print(sentenca)


# In[8]:


import spacy

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\links_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Lista para armazenar os sintagmas em posição de sujeito encontrados
sintagmas_sujeito = []

# Lista para armazenar as sentenças completas dos sintagmas em posição de sujeito
sentencas_sujeito = []

# Variável para contar as sentenças com sujeito
contagem_sentencas_sujeito = 0

# Lista para armazenar as sentenças passivas
sentencas_passivas = []

# Variável para contar as sentenças passivas
contagem_sentencas_passivas = 0

# Definir a gramática para identificar as sentenças passivas
gramatica_passiva = [
    {"DEP": {"REGEX": "(nsubj)"}, "OP": "?"},
    {"DEP": "auxpass"},
    {"DEP": {"REGEX": "(past_part|advcl)"}, "OP": "?"},
    {"DEP": {"IN": ["obl", "nmod"]}, "OP": "*"}
]

# Adicionar a gramática ao pipeline do spaCy
matcher = spacy.matcher.Matcher(nlp.vocab)
matcher.add("PASSIVA", gramatica_passiva)

# Percorrer as sentenças e identificar os sintagmas em posição de sujeito e as sentenças passivas
for sent in doc.sents:
    has_subject = False
    is_passive = False
    for token in sent:
        if token.dep_ == 'nsubj':  # Verificar se é um sujeito
            has_subject = True
            sintagmas_sujeito.append(token.text)
            sentencas_sujeito.append(sent.text)
        if token.dep_ == 'auxpass':  # Verificar se é uma construção passiva
            is_passive = True
    if has_subject:
        contagem_sentencas_sujeito += 1
    if is_passive:
        contagem_sentencas_passivas += 1
        sentencas_passivas.append(sent.text)

# Imprimir os sintagmas em posição de sujeito e suas respectivas sentenças
for sintagma, sentenca in zip(sintagmas_sujeito, sentencas_sujeito):
    print(f'Sintagma: {sintagma}')
    print(f'Sentença: {sentenca}\n')

# Imprimir a contagem de sentenças com sujeito
print(f"Quantidade de sentenças com sujeito: {contagem_sentencas_sujeito}")

# Imprimir a contagem de sentenças passivas e as sentenças passivas encontradas
print(f"Quantidade de sentenças passivas: {contagem_sentencas_passivas}")
print("Sentenças passivas:")
for sentenca in sentencas_passivas:
    print(sentenca)


# In[9]:


import spacy

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\links_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Lista para armazenar os sintagmas em posição de sujeito encontrados
sintagmas_sujeito = []

# Lista para armazenar as sentenças completas dos sintagmas em posição de sujeito
sentencas_sujeito = []

# Variável para contar as sentenças com sujeito
contagem_sentencas_sujeito = 0

# Lista para armazenar as sentenças passivas
sentencas_passivas = []

# Variável para contar as sentenças passivas
contagem_sentencas_passivas = 0

# Definir a gramática para identificar as sentenças passivas
gramatica_passiva = [
    {"DEP": {"REGEX": "(nsubj)"}, "OP": "?"},
    {"DEP": "auxpass"},
    {"DEP": {"REGEX": "(past_part|advcl)"}, "OP": "?"},
    {"DEP": {"IN": ["obl", "nmod"]}, "OP": "*"}
]

# Adicionar a gramática ao pipeline do spaCy
matcher = nlp.add_pipe("matcher")
matcher.add("PASSIVA", None, gramatica_passiva)

# Percorrer as sentenças e identificar os sintagmas em posição de sujeito e as sentenças passivas
for sent in doc.sents:
    has_subject = False
    is_passive = False
    for token in sent:
        if token.dep_ == 'nsubj':  # Verificar se é um sujeito
            has_subject = True
            sintagmas_sujeito.append(token.text)
            sentencas_sujeito.append(sent.text)
        if token.dep_ == 'auxpass':  # Verificar se é uma construção passiva
            is_passive = True
    if has_subject:
        contagem_sentencas_sujeito += 1
    if is_passive:
        contagem_sentencas_passivas += 1
        sentencas_passivas.append(sent.text)

# Imprimir os sintagmas em posição de sujeito e suas respectivas sentenças
for sintagma, sentenca in zip(sintagmas_sujeito, sentencas_sujeito):
    print(f'Sintagma: {sintagma}')
    print(f'Sentença: {sentenca}\n')

# Imprimir a contagem de sentenças com sujeito
print(f"Quantidade de sentenças com sujeito: {contagem_sentencas_sujeito}")

# Imprimir a contagem de sentenças passivas e as sentenças passivas encontradas
print(f"Quantidade de sentenças passivas: {contagem_sentencas_passivas}")
print("Sentenças passivas:")
for sentenca in sentencas_passivas:
    print(sentenca)


# In[10]:


import spacy
from spacy.matcher import Matcher

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\links_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Lista para armazenar os sintagmas em posição de sujeito encontrados
sintagmas_sujeito = []

# Lista para armazenar as sentenças completas dos sintagmas em posição de sujeito
sentencas_sujeito = []

# Variável para contar as sentenças com sujeito
contagem_sentencas_sujeito = 0

# Lista para armazenar as sentenças passivas
sentencas_passivas = []

# Variável para contar as sentenças passivas
contagem_sentencas_passivas = 0

# Definir o padrão para identificar as sentenças passivas
padrao_passiva = [
    {"DEP": "nsubjpass", "OP": "?"},  # sujeito passivo
    {"DEP": "auxpass"},  # verbo auxiliar passivo
    {"DEP": {"IN": ["obl", "nmod"]}, "OP": "*"}  # objeto ou complemento da passiva
]

# Inicializar o matcher do spaCy
matcher = Matcher(nlp.vocab)
matcher.add("PASSIVA", [padrao_passiva])

# Percorrer as sentenças e identificar os sintagmas em posição de sujeito e as sentenças passivas
for sent in doc.sents:
    has_subject = False
    is_passive = False
    for token in sent:
        if token.dep_ == 'nsubj':  # Verificar se é um sujeito
            has_subject = True
            sintagmas_sujeito.append(token.text)
            sentencas_sujeito.append(sent.text)
        if token.dep_ == 'auxpass':  # Verificar se é uma construção passiva
            is_passive = True
    if has_subject:
        contagem_sentencas_sujeito += 1
    if is_passive:
        contagem_sentencas_passivas += 1
        sentencas_passivas.append(sent.text)

# Imprimir os sintagmas em posição de sujeito e suas respectivas sentenças
for sintagma, sentenca in zip(sintagmas_sujeito, sentencas_sujeito):
    print(f'Sintagma: {sintagma}')
    print(f'Sentença: {sentenca}\n')

# Imprimir a contagem de sentenças com sujeito
print(f"Quantidade de sentenças com sujeito: {contagem_sentencas_sujeito}")

# Imprimir a contagem de sentenças passivas
print(f"Quantidade de sentenças passivas: {contagem_sentencas_passivas}")

# Imprimir as sentenças passivas
print("Sentenças passivas:")
for sentenca in sentencas_passivas:
    print(sentenca)


# In[11]:


import spacy
import re

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\links_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Lista para armazenar as sentenças passivas
sentencas_passivas = []

# Regex para identificar as estruturas de sentenças passivas
regex_passiva = r"(?i)\b(?:s(?:o(?:u|is|mos|m)|n|eram)|fo(?:i|ras|ram)|t(?:en(?:ho|s|do)|inha(?:s?|mos|issemos?)?|ere(?:i(?:s?|mos)|is?|m)|ivessem?os?)|se(?:ja|jas|jamos|jam)|fos(?:se|ses|sem|s(?:se|mos|semos|eis)?|eram)|h(?:ouvesse|ouve(?:r(?:a(?:mos|s?|mos)?|e(?:is?|mos)|ão)|mos?|riamos?|ver(?:a(?:mos|s?|mos)?|e(?:is?|mos)|ão)|i(?:a(?:mos|s?|mos)?|e(?:is?|mos)|am)))|aja(?:mos)?|av(?:ia(?:mos|s?|mos)?|e(?:is?|mos)|am))|f(?:or(?:a(?:mos|s?|mos)?|e(?:is?|mos)|am)?|os(?:se(?:mos|s?|mos)?|s(?:e(?:mos)?|t(?:eis?|mos)|ão)|e(?:is?|mos)|am))))\b.+?\b(partic[ií]pio)\b"

# Percorrer as sentenças e identificar as sentenças passivas
for sent in doc.sents:
    if re.search(regex_passiva, sent.text):
        sentencas_passivas.append(sent.text)

# Imprimir as sentenças passivas
print("Sentenças passivas:")
for sentenca in sentencas_passivas:
    print(sentenca)


# In[12]:


import spacy
import re

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\links_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Expressão regular para identificar sentenças passivas
regex_passiva = r'\b([Ss]ou|[Éé]s|[Éé]|[Ss]omos|[Ss]ois|[Ss]ão|[Ee]ra|[Ee]ras|[Ee]ra|[Éé]ramos|[Éé]reis|[Ee]ram|[Ff]ui|[Ff]oste|[Ff]oi|[Ff]omos|[Ff]ostes|[Ff]oram|[Tt]enho sido|[Hh]ei sido|[Tt]ens sido|[Tt]em sido|[Tt]emos sido|[Hh]avemos sido|[Tt]endes sido|[Hh]aveis sido|[Tt]êm sido|[Hh]ão sido|[Ff]ora|[Ff]oras|[Ff]ora|[Ff]ôramos|[Ff]ôreis|[Ff]orem|[Tt]inha ou [Hh]avia sido|[Tt]inhas ou [Hh]avias sido|[Tt]inha ou [Hh]avia sido|[Tt]ínhamos ou [Hh]avíamos sido|[Tt]ínheis ou [Hh]avíeis sido|[Tt]inham ou [Hh]aviam sido|[Tt]erei sido|[Hh]averei sido|[Tt]erás sido|[Hh]averás sido|[Tt]erá sido|[Hh]averá sido|[Tt]eremos sido|[Hh]averemos sido|[Tt]ereis sido|[Hh]avereis sido|[Tt]erão|[Hh]averão sido|[Ss]eja|[Ss]ejas|[Ss]eja|[Ss]ejamos|[Ss]ejais|[Ss]ejam|[Ff]osse|[Ff]osses|[Ff]osse|[Ff]ôssemos|[Ff]ôsseis|[Ff]ossem|[Tt]enha sido|[Hh]aja sido|[Tt]enhas sido|[Hh]ajas sido|[Tt]enha sido|[Hh]aja sido|[Tt]enhamos sido|[Hh]ajamos sido|[Tt]enhais sido|[Hh]ajais sido|[Tt]enham sido|[Hh]ajam sido|[Tt]ivesse sido|[Hh]ouvesse sido|[Tt]ivesses sido|[Hh]ouvesses sido|[Tt]ivesse sido|[Hh]ouvesse sido|[Tt]ivéssemos sido|[Hh]ouvéssemos sido|[Tt]ivésseis sido|[Hh]ouvésseis sido|[Tt]ivessem sido|[Hh]ouvessem sido|[Ff]or|[Ff]ores|[Ff]or|[Ff]ormos|[Ff]ordes|[Ff]orem|[Tt]iver sido|[Hh]ouver sido|[Tt]iveres sido|[Hh]averes sido|[Tt]iver sido|[Hh]ouver sido|[Tt]ivermos sido|[Hh]ouvermos sido|[Tt]iverdes sido|[Hh]averdes sido|[Tt]iverem sido|[Hh]ouverem sido|[Ss]er|[Ss]er|[Ss]eres|[Ss]er|[Ss]ermos|[Ss]erdes|[Ss]erem|[Tt]er sido|[Hh]aver sido)\b.*?\bparticípio\b'

# Lista para armazenar as sentenças passivas
sentencas_passivas = []

# Percorrer as sentenças e identificar as sentenças passivas
for sent in doc.sents:
    if re.search(regex_passiva, sent.text):
        sentencas_passivas.append(sent.text)

# Imprimir as sentenças passivas
for sent in sentencas_passivas:
    print(sent)


# In[13]:


import spacy

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\links_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Função para verificar se uma oração está na voz passiva
def verificar_voz_passiva(verbos):
    for i in range(len(verbos) - 1):
        if verbos[i].lemma_ == 'ser' and verbos[i+1].is_past_participle:
            return True
    return False

# Percorrer as sentenças e identificar as orações na voz passiva
for sent in doc.sents:
    verbos = [token for token in sent if token.pos_ == 'VERB']
    if verificar_voz_passiva(verbos):
        print(sent.text)


# In[14]:


import spacy

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\links_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Função para verificar se um verbo é um particípio passado
def is_participle(verb):
    if verb.morph.get('VerbForm') == 'Part':
        return True
    return False

# Função para verificar se uma oração está na voz passiva
def verificar_voz_passiva(verbos):
    for i in range(len(verbos) - 1):
        if verbos[i].lemma_ == 'ser' and is_participle(verbos[i+1]):
            return True
    return False

# Percorrer as sentenças e identificar as orações na voz passiva
for sent in doc.sents:
    verbos = [token for token in sent if token.pos_ == 'VERB']
    if verificar_voz_passiva(verbos):
        print(sent.text)


# In[15]:


import spacy

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Sentenças de exemplo
sentencas_exemplo = [
    "que também é alimentado pelo enorme reservatório de água da barragem do Dnipro",
    "O caderno foi jogado fora pelo aluno.",
    "A cidade foi devastada pelo furacão.",
    "Ainda ontem fui tomado de risos ao ler um trechinho de crônica.",
    "Os filhotes foram descobertos pelo jardineiro.",
    "Fernando estava protegido."
]

# Função para verificar se uma sentença está na voz passiva
def verificar_voz_passiva(sentenca):
    doc = nlp(sentenca)
    verbos = [token for token in doc if token.pos_ == 'VERB']
    for i in range(len(verbos) - 1):
        if verbos[i].lemma_ == 'ser' and verbos[i+1].morph.get('VerbForm') == 'Part':
            return True
    return False

# Verificar as sentenças de exemplo
for sentenca in sentencas_exemplo:
    if verificar_voz_passiva(sentenca):
        print(f'A sentença "{sentenca}" é uma sentença na voz passiva.')
    else:
        print(f'A sentença "{sentenca}" não é uma sentença na voz passiva.')


# In[16]:


import spacy

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Sentenças de exemplo
sentencas_exemplo = [
    "que também é alimentado pelo enorme reservatório de água da barragem do Dnipro",
    "O caderno foi jogado fora pelo aluno.",
    "A cidade foi devastada pelo furacão.",
    "Ainda ontem fui tomado de risos ao ler um trechinho de crônica.",
    "Os filhotes foram descobertos pelo jardineiro.",
    "Fernando estava protegido."
]

# Etiquetas gramaticais que indicam voz passiva
VOZ_PASSIVA_TAGS = {'aux', 'auxpass'}

# Função para verificar se uma sentença está na voz passiva
def verificar_voz_passiva(sentenca):
    doc = nlp(sentenca)
    for token in doc:
        if token.dep_ == 'aux' and token.head.lemma_ == 'ser':
            return True
        elif token.dep_ == 'auxpass':
            return True
    return False

# Verificar as sentenças de exemplo
for sentenca in sentencas_exemplo:
    if verificar_voz_passiva(sentenca):
        print(f'A sentença "{sentenca}" é uma sentença na voz passiva.')
    else:
        print(f'A sentença "{sentenca}" não é uma sentença na voz passiva.')


# In[17]:


import spacy

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Sentenças de exemplo que são consideradas passivas
sentencas_passivas_exemplo = [
    "que também é alimentado pelo enorme reservatório de água da barragem do Dnipro",
    "O caderno foi jogado fora pelo aluno.",
    "A cidade foi devastada pelo furacão.",
    "Ainda ontem fui tomado de risos ao ler um trechinho de crônica.",
    "Os filhotes foram descobertos pelo jardineiro.",
    "Fernando estava protegido."
]

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\links_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Lista para armazenar as sentenças passivas encontradas
sentencas_passivas = []

# Função para verificar se uma sentença está na voz passiva
def verificar_voz_passiva(sentenca):
    doc = nlp(sentenca)
    for token in doc:
        if token.dep_ == 'aux' and token.head.lemma_ == 'ser':
            return True
        elif token.dep_ == 'auxpass':
            return True
    return False

# Verificar as sentenças de exemplo
for sentenca in sentencas_passivas_exemplo:
    if verificar_voz_passiva(sentenca):
        sentencas_passivas.append(sentenca)

# Percorrer as sentenças do texto analisado
for sent in doc.sents:
    if verificar_voz_passiva(sent.text):
        sentencas_passivas.append(sent.text)

# Imprimir as sentenças passivas encontradas e a quantidade
for sentenca in sentencas_passivas:
    print(f"A sentença '{sentenca}' é uma sentença na voz passiva.")

quantidade_sentencas_passivas = len(sentencas_passivas)
print(f"Total de sentenças na voz passiva encontradas: {quantidade_sentencas_passivas}")


# In[18]:


import spacy
from spacy import displacy

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\links_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Percorrer as sentenças do texto analisado
for sent in doc.sents:
    # Imprimir a sentença
    print(f"Sentença: {sent.text}\n")
    
    # Imprimir a árvore de dependência da sentença
    for token in sent:
        print(f"Token: {token.text}\tDependência: {token.dep_}\tDependente de: {token.head.text}\n")
    
    # Imprimir uma linha em branco para separar as sentenças
    print()
    
    # Renderizar a árvore de dependência e salvar como imagem
    svg = displacy.render(sent, style='dep', options={'compact': True})
    output_path = f'sentenca_{sent.i+1}_arvore_dependencia.svg'
    with open(output_path, 'w', encoding='utf-8') as f_out:
        f_out.write(svg)
    print(f"Arquivo salvo: {output_path}\n")


# In[19]:


import spacy

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\links_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Percorrer as sentenças do texto analisado
for sent in doc.sents:
    # Imprimir a sentença
    print(f"Sentença: {sent.text}\n")
    
    # Imprimir a árvore de dependência da sentença
    for token in sent:
        print(f"Token: {token.text}\tDependência: {token.dep_}\tDependente de: {token.head.text}\n")
    
    # Imprimir uma linha em branco para separar as sentenças
    print()


# In[20]:


---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
Cell In[19], line 10
      7 caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\linksg1_noticias.txt'
      9 # Ler o arquivo das notícias
---> 10 with open(caminho_arquivo, 'r', encoding='utf-8') as f:
     11     noticias = f.read()
     13 # Processar as notícias com o spaCy

File ~\anaconda3\lib\site-packages\IPython\core\interactiveshell.py:282, in _modified_open(file, *args, **kwargs)
    275 if file in {0, 1, 2}:
    276     raise ValueError(
    277         f"IPython won't let you open fd={file} by default "
    278         "as it is likely to crash IPython. If you know what you are doing, "
    279         "you can use builtins' open."
    280     )
--> 282 return io_open(file, *args, **kwargs)

FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Administrator\\Documents\\PythonScripts\\Mono\\links_noticias.txt'


# In[21]:


import spacy

# Carregar modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\linksg1_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Percorrer as sentenças do texto analisado
for sent in doc.sents:
    # Imprimir a sentença
    print(f"Sentença: {sent.text}\n")
    
    # Imprimir a árvore de dependência da sentença
    for token in sent:
        print(f"Token: {token.text}\tDependência: {token.dep_}\tDependente de: {token.head.text}\n")
    
    # Imprimir uma linha em branco para separar as sentenças
    print()


# In[22]:


import spacy

# Carregar o modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\linksg1_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Percorrer as sentenças e analisar os verbos
for sent in doc.sents:
    verbos = []
    locucoes = []
    
    # Identificar verbos e locuções verbais
    for token in sent:
        if token.pos_ == 'VERB':
            verbos.append(token.lemma_)
            
            if token.dep_ == 'aux':
                locucao_verbal = ' '.join([t.lemma_ for t in token.head.children])
                locucoes.append(locucao_verbal)
    
    # Imprimir os resultados
    print(f'Sentença: {sent.text}')
    print(f'Verbos: {", ".join(verbos)}')
    
    if locucoes:
        print(f'Locuções verbais: {", ".join(locucoes)}')
    
    print('---')


# In[23]:


import spacy

# Carregar o modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\links_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Percorrer as sentenças e analisar os verbos
for sent in doc.sents:
    verbos = []
    locucoes = []
    
    # Identificar verbos e locuções verbais
    for token in sent:
        if token.pos_ == 'VERB':
            verbos.append((token.lemma_, token.tag_))
            
            if token.dep_ == 'aux':
                locucao_verbal = ' '.join([t.lemma_ for t in token.head.children])
                locucoes.append(locucao_verbal)
    
    # Imprimir os resultados
    print(f'Sentença: {sent.text}')
    
    for verbo, tag in verbos:
        print(f'Verbo: {verbo}')
        print(f'Forma morfológica: {tag}')
    
    if locucoes:
        print(f'Locuções verbais: {", ".join(locucoes)}')
    
    print('---')


# In[24]:


import spacy

# Carregar o modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\linksg1_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Percorrer as sentenças e analisar os verbos
for sent in doc.sents:
    verbos = []
    locucoes = []
    
    # Identificar verbos e locuções verbais
    for token in sent:
        if token.pos_ == 'VERB':
            verbos.append((token.lemma_, token.tag_))
            
            if token.dep_ == 'aux':
                locucao_verbal = ' '.join([t.lemma_ for t in token.head.children])
                locucoes.append(locucao_verbal)
    
    # Imprimir os resultados
    print(f'Sentença: {sent.text}')
    
    for verbo, tag in verbos:
        print(f'Verbo: {verbo}')
        print(f'Forma morfológica: {tag}')
    
    if locucoes:
        print(f'Locuções verbais: {", ".join(locucoes)}')
    
    print('---')


# In[25]:


import spacy

# Carregar o modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\links_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Percorrer as sentenças e analisar os verbos
for sent in doc.sents:
    verbos = []
    
    # Identificar verbos
    for token in sent:
        if token.pos_ == 'VERB':
            verbos.append(token)
    
    # Imprimir os resultados
    print(f'Sentença: {sent.text}')
    
    for verbo in verbos:
        print(f'Verbo: {verbo.lemma_}')
        print(f'Forma morfológica: {verbo.morph}')
        print(f'Voz: {verbo.morph.get("Voice", "")}')
        print(f'Tempo: {verbo.morph.get("Tense", "")}')
        print(f'Modo: {verbo.morph.get("Mood", "")}')
        print(f'Pessoa: {verbo.morph.get("Person", "")}')
        print(f'Número: {verbo.morph.get("Number", "")}')
    
    print('---')


# In[26]:


import spacy

# Carregar o modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\linksg1_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Percorrer as sentenças e analisar os verbos
for sent in doc.sents:
    verbos = []
    
    # Identificar verbos
    for token in sent:
        if token.pos_ == 'VERB':
            verbos.append(token)
    
    # Imprimir os resultados
    print(f'Sentença: {sent.text}')
    
    for verbo in verbos:
        print(f'Verbo: {verbo.lemma_}')
        print(f'Forma morfológica: {verbo.morph}')
        print(f'Voz: {verbo.morph.get("Voice", "")}')
        print(f'Tempo: {verbo.morph.get("Tense", "")}')
        print(f'Modo: {verbo.morph.get("Mood", "")}')
        print(f'Pessoa: {verbo.morph.get("Person", "")}')
        print(f'Número: {verbo.morph.get("Number", "")}')
    
    print('---')


# In[27]:


import spacy

# Carregar o modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\linksg1_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Criar uma lista para armazenar as formas verbais únicas
formas_verbais = []

# Percorrer as sentenças e analisar os verbos
for sent in doc.sents:
    for token in sent:
        if token.pos_ == 'VERB':
            forma_verbal = token.morph.get('VerbForm')
            if forma_verbal and forma_verbal not in formas_verbais:
                formas_verbais.append(forma_verbal)

# Imprimir a lista de formas verbais encontradas
print('Formas Verbais Encontradas:')
for forma in formas_verbais:
    print(forma)


# In[28]:


import spacy

# Carregar o modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\linksg1_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Criar uma lista para armazenar as sentenças com 'Part' (particípio)
sentencas_participio = []

# Percorrer as sentenças e identificar as sentenças com particípio
for sent in doc.sents:
    verbos = [token for token in sent if token.pos_ == 'VERB']
    for verbo in verbos:
        if verbo.morph.get('VerbForm') == 'Part':
            sentencas_participio.append(sent.text)
            break  # Parar a verificação após encontrar um verbo no particípio

# Imprimir as sentenças com particípio
print('Sentenças com particípio (VerbForm=Part):')
for sentenca in sentencas_participio:
    print(sentenca)


# In[30]:


import spacy

# Carregar o modelo de língua do spaCy
nlp = spacy.load('pt_core_news_sm')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\linksg1_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
noticias = f.read()

# Processar as notícias com o spaCy
doc = nlp(noticias)

# Criar uma lista para armazenar as sentenças com 'Part' (particípio)
sentencas_participio = []

# Percorrer as sentenças e identificar as sentenças com particípio
for sent in doc.sents:
verbos = [token for token in sent if token.pos_ == 'VERB']
for verbo in verbos:
    if verbo.morph.get('VerbForm') == 'Part':
        sentencas_participio.append(sent.text)

# Imprimir as sentenças com particípio
print('Sentenças com particípio (VerbForm=Part):')
for sentenca in sentencas_participio:
print(sentenca)


# In[31]:


pip install nltk


# In[1]:


import nltk

# Baixar os pacotes do NLTK para o idioma português
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


# In[2]:


import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag

# Definir o idioma como português
nltk.download('floresta')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\linksg1_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Tokenização de sentenças
sentencas = sent_tokenize(noticias)

# Lista para armazenar as sentenças na voz passiva
sentencas_passivas = []

# Percorrer as sentenças e identificar as sentenças na voz passiva
for sentenca in sentencas:
    tokens = word_tokenize(sentenca)
    pos_tags = pos_tag(tokens, lang='por')
    # Verificar se há verbos na voz passiva
    for i in range(len(pos_tags) - 1):
        if pos_tags[i][1] == 'VBZ' and pos_tags[i + 1][1] == 'VBN':
            sentencas_passivas.append(sentenca)
            break

# Imprimir as sentenças na voz passiva
print('Sentenças na voz passiva:')
for sentenca in sentencas_passivas:
    print(sentenca)


# In[3]:


import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag

# Definir o idioma como português
nltk.download('floresta')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\linksg1_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Tokenização de sentenças
sentencas = sent_tokenize(noticias)

# Lista para armazenar as sentenças na voz passiva
sentencas_passivas = []

# Percorrer as sentenças e identificar as sentenças na voz passiva
for sentenca in sentencas:
    tokens = word_tokenize(sentenca)
    pos_tags = pos_tag(tokens, language='portuguese')
    # Verificar se há verbos na voz passiva
    for i in range(len(pos_tags) - 1):
        if pos_tags[i][1] == 'VBZ' and pos_tags[i + 1][1] == 'VBN':
            sentencas_passivas.append(sentenca)
            break

# Imprimir as sentenças na voz passiva
print('Sentenças na voz passiva:')
for sentenca in sentencas_passivas:
    print(sentenca)


# In[4]:


import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag

# Fazer o download dos dados do modelo 'floresta'
nltk.download('floresta')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\links_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Tokenização de sentenças
sentencas = sent_tokenize(noticias)

# Lista para armazenar as sentenças na voz passiva
sentencas_passivas = []

# Percorrer as sentenças e identificar as sentenças na voz passiva
for sentenca in sentencas:
    tokens = word_tokenize(sentenca)
    pos_tags = pos_tag(tokens, tagset='universal')
    # Verificar se há verbos na voz passiva
    for i in range(len(pos_tags) - 1):
        if pos_tags[i][1] == 'VERB' and pos_tags[i + 1][1] == 'VERB':
            sentencas_passivas.append(sentenca)
            break

# Imprimir as sentenças na voz passiva
print('Sentenças na voz passiva:')
for sentenca in sentencas_passivas:
    print(sentenca)


# In[5]:


import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag

# Fazer o download dos dados do modelo 'floresta'
nltk.download('floresta')

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\linksg1_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Tokenização de sentenças
sentencas = sent_tokenize(noticias)

# Lista para armazenar as sentenças na voz passiva
sentencas_passivas = []

# Percorrer as sentenças e identificar as sentenças na voz passiva
for sentenca in sentencas:
    tokens = word_tokenize(sentenca)
    pos_tags = pos_tag(tokens, tagset='universal')
    # Verificar se há verbos na voz passiva
    for i in range(len(pos_tags) - 1):
        if pos_tags[i][1] == 'VERB' and pos_tags[i + 1][1] == 'VERB':
            sentencas_passivas.append(sentenca)
            break

# Imprimir as sentenças na voz passiva
print('Sentenças na voz passiva:')
for sentenca in sentencas_passivas:
    print(sentenca)


# In[6]:


import nltk
 >>> nltk.download('universal_tagset')


# In[7]:


import nltk
nltk.download('universal_tagset')


# In[8]:


import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\links_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Tokenização de sentenças
sentencas = sent_tokenize(noticias)

# Lista para armazenar as sentenças na voz passiva
sentencas_passivas = []

# Percorrer as sentenças e identificar as sentenças na voz passiva
for sentenca in sentencas:
    tokens = word_tokenize(sentenca)
    pos_tags = pos_tag(tokens, lang='pt', tagset='mac_morpho')
    # Verificar se há verbos na voz passiva
    for i in range(len(pos_tags) - 1):
        if pos_tags[i][1] == 'V' and pos_tags[i + 1][1] == 'V':
            sentencas_passivas.append(sentenca)
            break

# Imprimir as sentenças na voz passiva
print('Sentenças na voz passiva:')
for sentenca in sentencas_passivas:
    print(sentenca)


# In[9]:


import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag

# Caminho completo para o arquivo das notícias
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\linksg1_noticias.txt'

# Ler o arquivo das notícias
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Tokenização de sentenças
sentencas = sent_tokenize(noticias)

# Lista para armazenar as sentenças na voz passiva
sentencas_passivas = []

# Percorrer as sentenças e identificar as sentenças na voz passiva
for sentenca in sentencas:
    tokens = word_tokenize(sentenca)
    pos_tags = pos_tag(tokens, lang='pt', tagset='mac_morpho')
    # Verificar se há verbos na voz passiva
    for i in range(len(pos_tags) - 1):
        if pos_tags[i][1] == 'V' and pos_tags[i + 1][1] == 'V':
            sentencas_passivas.append(sentenca)
            break

# Imprimir as sentenças na voz passiva
print('Sentenças na voz passiva:')
for sentenca in sentencas_passivas:
    print(sentenca)


# In[10]:


import nltk
from nltk.corpus import floresta
from nltk import sent_tokenize, word_tokenize, pos_tag

# Fazer o download dos recursos necessários
nltk.download('floresta')

# Caminho completo para o arquivo "linksg1_noticias.txt"
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\linksg1_noticias.txt'

# Ler o conteúdo do arquivo
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Tokenização de sentenças
sentencas = sent_tokenize(noticias)

# Lista para armazenar os verbos em voz passiva
verbos_passivos = []

# Percorrer as sentenças e identificar os verbos em voz passiva
for sentenca in sentencas:
    tokens = word_tokenize(sentenca)
    pos_tags = pos_tag(tokens)
    # Verificar se há verbos na voz passiva
    for i in range(len(pos_tags) - 1):
        if pos_tags[i][1] == 'V' and pos_tags[i + 1][1] == 'P':
            verbos_passivos.append(pos_tags[i][0])
            break

# Imprimir os verbos em voz passiva encontrados
print('Verbos em voz passiva:')
for verbo in verbos_passivos:
    print(verbo)


# In[11]:


import nltk
from nltk.corpus import floresta
from nltk import sent_tokenize, word_tokenize

# Fazer o download dos recursos necessários
nltk.download('floresta')

# Carregar as sentenças anotadas da floresta
sentencas_floresta = floresta.tagged_sents()

# Caminho completo para o arquivo "linksg1_noticias.txt"
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\linksg1_noticias.txt'

# Ler o conteúdo do arquivo
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Tokenização de sentenças
sentencas = sent_tokenize(noticias)

# Lista para armazenar os verbos em voz passiva
verbos_passivos = []

# Percorrer as sentenças e identificar os verbos em voz passiva
for sentenca in sentencas:
    tokens = word_tokenize(sentenca)
    # Procurar os verbos na voz passiva na floresta
    for sent_floresta in sentencas_floresta:
        if len(sent_floresta) == len(tokens):
            match = True
            for i in range(len(sent_floresta)):
                if sent_floresta[i][0].lower() != tokens[i].lower() or sent_floresta[i][1] != 'V' or sent_floresta[i][3] != 'p':
                    match = False
                    break
            if match:
                verbos_passivos.extend([token for token, _, _, _ in sent_floresta])

# Imprimir os verbos em voz passiva encontrados
print('Verbos em voz passiva:')
for verbo in verbos_passivos:
    print(verbo)


# In[1]:


import nltk
from nltk.corpus import floresta
from nltk import sent_tokenize, word_tokenize

# Fazer o download dos recursos necessários
nltk.download('floresta')

# Carregar as sentenças anotadas da floresta
sentencas_floresta = floresta.tagged_sents()

# Caminho completo para o arquivo "linksg1_noticias.txt"
caminho_arquivo = r'C:\Users\Administrator\Documents\PythonScripts\Mono\linksg1_noticias.txt'

# Ler o conteúdo do arquivo
with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    noticias = f.read()

# Tokenização de sentenças
sentencas = sent_tokenize(noticias)

# Lista para armazenar os verbos em voz passiva
verbos_passivos = []

# Percorrer as sentenças e identificar os verbos em voz passiva
for sentenca in sentencas:
    tokens = word_tokenize(sentenca)
    # Procurar os verbos na voz passiva na floresta
    for sent_floresta in sentencas_floresta:
        if len(sent_floresta) == len(tokens):
            match = True
            for i in range(len(sent_floresta)):
                if sent_floresta[i][0].lower() != tokens[i].lower() or sent_floresta[i][1] != 'V' or sent_floresta[i][3] != 'p':
                    match = False
                    break
            if match:
                verbos_passivos.extend([token for token, _, _, _ in sent_floresta])
                break  # Para a comparação após encontrar um match

    if len(verbos_passivos) >= 50:
        break  # Parar a busca após encontrar 50 verbos

# Imprimir os verbos em voz passiva encontrados
print('Verbos em voz passiva:')
for verbo in verbos_passivos[:50]:
    print(verbo)


# In[ ]:


import requests
from datetime import date

# Parâmetros da API
params = {
    'q': 'Russia',
    'from': '2023-05-28',  # Atualize a data de início desejada
    'sortBy': 'popularity',
    'apiKey': '5ddb2a29303d46f1bc6299bdbabff90e'
}

# URL da API
url = 'https://newsapi.org/v2/everything'

# Fazer a solicitação HTTP
response = requests.get(url, params=params)
data = response.json()

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Lista para armazenar os textos das notícias
    textos_noticias = []

    # Percorrer as notícias retornadas pela API
    for article in data['articles']:
        # Obter o conteúdo da notícia
        content = article.get('content')
        if content:
            textos_noticias.append(content)

        # Verificar se já coletamos textos de 250 notícias
        if len(textos_noticias) >= 250:
            break

    # Salvar os textos das notícias em um arquivo de texto
    with open('noticias.txt', 'w', encoding='utf-8') as file:
        for texto in textos_noticias:
            file.write(texto + '\n')

    print('Notícias coletadas e salvas em noticias.txt.')
else:
    print('Erro ao fazer a solicitação HTTP:', response.status_code)


# In[1]:


import requests
from datetime import date

# Parâmetros da API
params = {
    'q': 'Russia',
    'from': '2023-05-28',  # Atualize a data de início desejada
    'sortBy': 'popularity',
    'apiKey': '5ddb2a29303d46f1bc6299bdbabff90e'
}

# URL da API
url = 'https://newsapi.org/v2/everything'

# Fazer a solicitação HTTP
response = requests.get(url, params=params)
data = response.json()

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Lista para armazenar os textos das notícias
    textos_noticias = []

    # Percorrer as notícias retornadas pela API
    for article in data['articles']:
        # Obter o conteúdo da notícia
        content = article.get('content')
        if content:
            textos_noticias.append(content)

        # Verificar se já coletamos textos de 250 notícias
        if len(textos_noticias) >= 250:
            break

    # Salvar os textos das notícias em um arquivo de texto
    with open('noticias.txt', 'w', encoding='utf-8') as file:
        for texto in textos_noticias:
            file.write(texto + '\n')

    print('Notícias coletadas e salvas em noticias.txt.')
else:
    print('Erro ao fazer a solicitação HTTP:', response.status_code)


# In[3]:


import requests

# Parâmetros da API
params = {
    'q': 'Russia',
    'from': '2023-05-28',
    'sortBy': 'popularity',
    'apiKey': '5ddb2a29303d46f1bc6299bdbabff90e'
}

# URL da API
url = 'https://newsapi.org/v2/everything'

# Fazer a solicitação HTTP
response = requests.get(url, params=params)
data = response.json()

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Lista para armazenar os textos das notícias
    textos_noticias = []
    urls_noticias = []

    # Percorrer as notícias retornadas pela API
    for article in data['articles']:
        # Obter o conteúdo da notícia
        content = article.get('content')
        url = article.get('url')
        if content and url:
            textos_noticias.append(content)
            urls_noticias.append(url)

        # Verificar se já coletamos textos de 250 notícias
        if len(textos_noticias) >= 250:
            break

    # Salvar os textos das notícias em um arquivo de texto
    with open('noticias.txt', 'w', encoding='utf-8') as file:
        for texto in textos_noticias:
            file.write(texto + '\n')

    print('Notícias coletadas e salvas em noticias.txt.')
    
    print('URLs das notícias:')
    for url in urls_noticias:
        print(url)
else:
    print('Erro ao fazer a solicitação HTTP:', response.status_code)


# In[ ]:


import requests
from bs4 import BeautifulSoup
import random

# URL base
base_url = 'https://www.bbc.com/news/world-60525350'

# Lista para armazenar as URLs das notícias coletadas
urls_noticias = []

# Realizar a coleta de 100 notícias aleatórias
while len(urls_noticias) < 100:
    # Gerar uma data aleatória no formato YYYY-MM-DD
    data = f'{random.randint(2015, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}'
    
    # Montar a URL com a data aleatória
    url = f'{base_url}/{data}'
    
    # Fazer a solicitação HTTP
    response = requests.get(url)
    
    # Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Parsear o conteúdo HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrar os links das notícias na página
        links = soup.find_all('a', class_='gs-c-promo-heading')
        
        # Extrair as URLs das notícias
        for link in links:
            url_noticia = link['href']
            
            # Verificar se a URL é válida (começa com '/news/')
            if url_noticia.startswith('/news/'):
                # Montar a URL completa da notícia
                url_noticia = f'https://www.bbc.com{url_noticia}'
                
                # Adicionar a URL à lista de notícias coletadas
                urls_noticias.append(url_noticia)
                
                # Verificar se já coletamos as 100 notícias
                if len(urls_noticias) >= 100:
                    break
        
    else:
        print('Erro ao fazer a solicitação HTTP:', response.status_code)
    
# Imprimir as URLs das notícias coletadas
for url in urls_noticias:
    print(url)


# In[1]:


import requests
from bs4 import BeautifulSoup

# URL da página principal de notícias da BBC
url = 'https://www.bbc.com/news'

# Fazer a solicitação HTTP
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Parsear o conteúdo HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar os links das notícias na página
    links = soup.find_all('a', class_='gs-c-promo-heading')

    # Lista para armazenar as URLs das notícias
    urls_noticias = []

    # Extrair as URLs das notícias
    for link in links:
        url_noticia = link['href']

        # Verificar se a URL é válida (começa com '/news/')
        if url_noticia.startswith('/news/'):
            # Montar a URL completa da notícia
            url_noticia = f'https://www.bbc.com{url_noticia}'

            # Adicionar a URL à lista de notícias
            urls_noticias.append(url_noticia)

            # Verificar se já coletamos as 100 notícias
            if len(urls_noticias) >= 100:
                break

    # Imprimir as URLs das notícias coletadas
    for url in urls_noticias:
        print(url)

else:
    print('Erro ao fazer a solicitação HTTP:', response.status_code)


# In[2]:


import requests
from bs4 import BeautifulSoup

# URL da página principal de notícias da BBC
url = 'https://www.bbc.com/news/world-60525350'

# Fazer a solicitação HTTP
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Parsear o conteúdo HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar os links das notícias na página
    links = soup.find_all('a', class_='gs-c-promo-heading')

    # Lista para armazenar as URLs das notícias
    urls_noticias = []

    # Extrair as URLs das notícias
    for link in links:
        url_noticia = link['href']

        # Verificar se a URL é válida (começa com '/news/')
        if url_noticia.startswith('/news/'):
            # Montar a URL completa da notícia
            url_noticia = f'https://www.bbc.com{url_noticia}'

            # Adicionar a URL à lista de notícias
            urls_noticias.append(url_noticia)

            # Verificar se já coletamos as 100 notícias
            if len(urls_noticias) >= 100:
                break

    # Imprimir as URLs das notícias coletadas
    for url in urls_noticias:
        print(url)

else:
    print('Erro ao fazer a solicitação HTTP:', response.status_code)


# In[3]:


import requests
from bs4 import BeautifulSoup

# URL da página principal de notícias da BBC
url = 'https://www.bbc.com/news/world-60525350'

# Número máximo de URLs a serem coletadas
limite_urls = 100

# Lista para armazenar as URLs das notícias
urls_noticias = []

# Variável para controlar o número de URLs coletadas
contador_urls = 0

while contador_urls < limite_urls:
    # Fazer a solicitação HTTP
    response = requests.get(url)

    # Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Parsear o conteúdo HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar os links das notícias na página
        links = soup.find_all('a', class_='gs-c-promo-heading')

        # Extrair as URLs das notícias
        for link in links:
            url_noticia = link['href']

            # Verificar se a URL é válida (começa com '/news/')
            if url_noticia.startswith('/news/'):
                # Montar a URL completa da notícia
                url_noticia = f'https://www.bbc.com{url_noticia}'

                # Adicionar a URL à lista de notícias
                urls_noticias.append(url_noticia)
                contador_urls += 1

                # Verificar se já coletamos as 100 notícias
                if contador_urls >= limite_urls:
                    break

        # Verificar se já coletamos as 100 notícias
        if contador_urls >= limite_urls:
            break

        # Obter a URL da próxima página
        next_page_link = soup.find('a', class_='gs-c-pagination-next')

        # Verificar se há uma próxima página
        if next_page_link:
            url = f"https://www.bbc.com{next_page_link['href']}"
        else:
            break

    else:
        print('Erro ao fazer a solicitação HTTP:', response.status_code)
        break

# Imprimir as URLs das notícias coletadas
for url in urls_noticias:
    print(url)


# In[4]:


import requests
from bs4 import BeautifulSoup

# URL da página principal de notícias da BBC
url = 'https://www.bbc.com/news/world-60525350'

# Número máximo de URLs a serem coletadas
limite_urls = 100

# Lista para armazenar as URLs das notícias
urls_noticias = []

# Variável para controlar o número de URLs coletadas
contador_urls = 0

while contador_urls < limite_urls:
    # Fazer a solicitação HTTP
    response = requests.get(url)

    # Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Parsear o conteúdo HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar os links das notícias na página
        links = soup.find_all('a', class_='gs-c-promo-heading')

        # Extrair as URLs das notícias
        for link in links:
            url_noticia = link['href']

            # Verificar se a URL é válida (começa com '/news/')
            if url_noticia.startswith('/news/'):
                # Montar a URL completa da notícia
                url_noticia = f'https://www.bbc.com{url_noticia}'

                # Adicionar a URL à lista de notícias
                urls_noticias.append(url_noticia)
                contador_urls += 1

                # Verificar se já coletamos as 100 notícias
                if contador_urls >= limite_urls:
                    break

        # Verificar se já coletamos as 100 notícias
        if contador_urls >= limite_urls:
            break

        # Verificar se há uma próxima página
        next_page_link = soup.find('a', class_='gs-c-pagination-next')

        if next_page_link:
            # Obter a URL da próxima página
            url = f"https://www.bbc.com{next_page_link['href']}"
        else:
            break

    else:
        print('Erro ao fazer a solicitação HTTP:', response.status_code)
        break

# Imprimir as URLs das notícias coletadas
for url in urls_noticias:
    print(url)


# In[5]:


import requests
from bs4 import BeautifulSoup

# URL da página principal de notícias da BBC
    url = 'https://www.bbc.com/news/world-60525350'

# Número máximo de URLs a serem coletadas
limite_urls = 100

# Lista para armazenar as URLs das notícias
urls_noticias = []

# Variável para controlar o número de URLs coletadas
contador_urls = 0

while contador_urls < limite_urls:
    # Fazer a solicitação HTTP
    response = requests.get(url)

    # Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Parsear o conteúdo HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar os links das notícias na página
        links = soup.find_all('a', class_='gs-c-promo-heading')

        # Extrair as URLs das notícias
        for link in links:
            url_noticia = link['href']

            # Verificar se a URL é válida (começa com '/news/')
            if url_noticia.startswith('/news/'):
                # Montar a URL completa da notícia
                url_noticia = f'https://www.bbc.com{url_noticia}'

                # Adicionar a URL à lista de notícias
                urls_noticias.append(url_noticia)
                contador_urls += 1

                # Verificar se já coletamos as 100 notícias
                if contador_urls >= limite_urls:
                    break

        # Verificar se já coletamos as 100 notícias
        if contador_urls >= limite_urls:
            break

        # Verificar se há uma próxima página
        next_page_link = soup.find('a', class_='lx-pagination__next')

        if next_page_link:
            # Obter a URL da próxima página
            url = f"https://www.bbc.com{next_page_link['href']}"
        else:
            break

    else:
        print('Erro ao fazer a solicitação HTTP:', response.status_code)
        break

# Imprimir as URLs das notícias coletadas
for url in urls_noticias:
    print(url)


# In[7]:


import requests
from bs4 import BeautifulSoup

# Função para coletar o texto completo de uma URL
def coletar_texto(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find('article')
        if article:
            paragraphs = article.find_all('p')
            texto = '\n'.join(p.get_text() for p in paragraphs)
            return texto
    return None

# Lista de URLs das notícias
urls_noticias = [
    'https://www.bbc.com/news/world-europe-66024526',
    'https://www.bbc.com/news/world-europe-66024526',
    'https://www.bbc.com/news/world-europe-66021601',
    'https://www.bbc.com/news/world-europe-66012906',
    'https://www.bbc.com/news/world-europe-66006880',
    'https://www.bbc.com/news/world-europe-66013532',
    'https://www.bbc.com/news/world-europe-66014651',
    'https://www.bbc.com/news/world-europe-66007609',
    'https://www.bbc.com/news/world-europe-66024526',
    'https://www.bbc.com/news/world-europe-66021601',
    'https://www.bbc.com/news/world-europe-66012906',
    'https://www.bbc.com/news/world-europe-66006880',
    'https://www.bbc.com/news/world-europe-66013532',
    'https://www.bbc.com/news/world-europe-66014651',
    'https://www.bbc.com/news/world-europe-66007609',
    'https://www.bbc.com/news/world-europe-66021601',
    'https://www.bbc.com/news/world-europe-66012906',
    'https://www.bbc.com/news/world-europe-66006880',
    'https://www.bbc.com/news/world-europe-66013532',
    'https://www.bbc.com/news/world-europe-66014651',
    'https://www.bbc.com/news/world-europe-66007609',
    'https://www.bbc.com/news/world-europe-65976256',
    'https://www.bbc.com/news/world-europe-60573261',
    'https://www.bbc.com/news/world-europe-66015624',
    'https://www.bbc.com/news/world-europe-60506682',
    'https://www.bbc.com/news/world-europe-65973624',
    'https://www.bbc.com/news/world-europe-65932700',
    'https://www.bbc.com/news/world-europe-65897919',
    'https://www.bbc.com/news/world-europe-65894743',
    'https://www.bbc.com/news/world-europe-65867990'
]

# Coletar o texto completo de cada URL e salvar em um arquivo de texto
with open("noticias.txt", "w", encoding="utf-8") as file:
    for url in urls_noticias:
        texto_noticia = coletar_texto(url)
        if texto_noticia:
            file.write(texto_noticia + '\n\n')

print("Texto das notícias coletado e salvo em noticias.txt.")



# In[8]:


import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag

# Função para identificar os sujeitos em uma sentença
def identificar_sujeitos(sentenca):
    sujeitos = []
    # Realizar a tokenização das palavras da sentença
    tokens = word_tokenize(sentenca)
    # Realizar a marcação de POS (Part-of-Speech) das palavras
    pos_tags = pos_tag(tokens)
    # Identificar os sujeitos na sentença
    for (palavra, pos) in pos_tags:
        if pos.startswith('NN') or pos.startswith('PRP'):
            sujeitos.append(palavra)
    return sujeitos

# Ler o conteúdo do arquivo de texto
with open('noticias.txt', 'r', encoding='utf-8') as file:
    texto = file.read()

# Tokenizar o texto em sentenças
sentencas = sent_tokenize(texto)

# Lista para armazenar os sujeitos encontrados
sujeitos = []

# Identificar os sujeitos em cada sentença
for sentenca in sentencas:
    sujeitos_sentenca = identificar_sujeitos(sentenca)
    sujeitos.extend(sujeitos_sentenca)

# Calcular a frequência dos sujeitos
frequencia_sujeitos = nltk.FreqDist(sujeitos)

# Imprimir os sujeitos e suas frequências
for sujeito, frequencia in frequencia_sujeitos.most_common():
    print(f'{sujeito}: {frequencia}')


# In[1]:


import spacy

# Carregar o modelo de idioma em inglês
nlp = spacy.load("en_core_web_sm")

# Lista de palavras-chave para os sujeitos
sujeitos = [
    "Wagner", "Putin", "Russia", "Prigozhin", "Ukraine", "President", "president",
    "rebellion", "Moscow", "Belarus", "Vladimir", "Kremlin", "US", "fighters",
    "army", "Russian", "Bakhmut", "mercenaries", "Russians", "military",
    "soldiers", "Group", "Biden", "justice", "government", "leadership",
    "Zelensky", "resistance"
]

# Ler o arquivo "noticias.txt" e obter o texto completo
with open("noticias.txt", "r", encoding="utf-8") as file:
    texto = file.read()

# Processar o texto com o modelo do spaCy
doc = nlp(texto)

# Lista para armazenar as orações com contexto ampliado e o sujeito destacado
oracoes_contexto_ampliado = []

# Iterar sobre as sentenças e verificar se contêm algum dos sujeitos
for sentenca in doc.sents:
    for sujeito in sujeitos:
        if sujeito in sentenca.text:
            sujeito_destacado = sentenca.text.replace(sujeito, f"**{sujeito}**")
            oracoes_contexto_ampliado.append(sujeito_destacado)

# Salvar as orações com contexto ampliado em um arquivo de texto
with open("oracoes_contexto_ampliado.txt", "w", encoding="utf-8") as file:
    for oracao in oracoes_contexto_ampliado:
        file.write(oracao)
        file.write("\n---\n")


# In[2]:


import spacy
from spacy import displacy
import io
import sys

# Carregar o modelo de idioma em inglês
nlp = spacy.load("en_core_web_sm")

# Ler o arquivo "oracoes_contexto_ampliado.txt" e obter as orações em contexto ampliado
with open("oracoes_contexto_ampliado.txt", "r", encoding="utf-8") as file:
    texto = file.read()

# Processar o texto com o modelo do spaCy
doc = nlp(texto)

# Criar o arquivo "arvores_dependencia.txt" para salvar as representações gráficas das árvores de dependência
with open("arvores_dependencia.txt", "w", encoding="utf-8") as file:
    for sentenca in doc.sents:
        # Verificar se a sentença contém um sujeito em negrito
        sujeito_negrito = False
        for token in sentenca:
            if token.dep_ == "nsubj" and token.ent_type_ == "sujeito_destacado":
                sujeito_negrito = True
                break

        # Se a sentença contém um sujeito em negrito, prosseguir com a análise
        if sujeito_negrito:
            # Obter as frases na oração atual
            frases = list(sentenca.noun_chunks) + list(sentenca.subtree)

            # Redirecionar a saída padrão para capturar a representação gráfica
            stdout_saved = sys.stdout
            sys.stdout = io.StringIO()

            # Renderizar a árvore de dependência
            displacy.render(sentenca, style="dep", options={"compact": True, "color": "blue"})

            # Obter a representação gráfica da árvore de dependência
            arvore_dependencia = sys.stdout.getvalue()

            # Restaurar a saída padrão
            sys.stdout = stdout_saved

            # Salvar a representação gráfica da árvore de dependência junto com as frases no arquivo "arvores_dependencia.txt"
            file.write(sentenca.text)
            file.write("\n")
            file.write(arvore_dependencia)
            file.write("\n---\n")
            file.write("Frases:\n")
            for frase in frases:
                file.write(f"{frase.text}\n")
            file.write("\n===\n")


# In[3]:


import spacy

# Carregar o modelo de idioma em inglês
nlp = spacy.load("en_core_web_sm")

# Ler o arquivo "oracoes_contexto_ampliado.txt" e obter as orações em contexto ampliado
with open("oracoes_contexto_ampliado.txt", "r", encoding="utf-8") as file:
    texto = file.read()

# Processar o texto com o modelo do spaCy
doc = nlp(texto)

# Lista para armazenar as informações das orações com auxpass
oracoes_auxpass = []

# Iterar pelas sentenças do documento
for sentenca in doc.sents:
    # Verificar se a sentença contém a relação de dependência "auxpass"
    if any(token.dep_ == "auxpass" for token in sentenca):
        # Extrair informações relevantes da sentença
        sujeito = ""
        verbo_principal = ""
        argumentos = []
        
        # Iterar pelos tokens da sentença
        for token in sentenca:
            # Verificar se o token é o sujeito
            if token.dep_ == "nsubj":
                sujeito = token.text
            # Verificar se o token é o verbo principal
            if token.dep_ == "ROOT":
                verbo_principal = token.text
            # Verificar se o token é um argumento
            if token.dep_ != "punct" and token.dep_ != "auxpass" and token.dep_ != "ROOT" and token.dep_ != "nsubj":
                argumentos.append(token.text)
        
        # Adicionar as informações à lista de orações com auxpass
        oracoes_auxpass.append((sentenca.text, sujeito, verbo_principal, argumentos))

# Imprimir a lista de informações das orações com auxpass
for oracao in oracoes_auxpass:
    oracao_completa, sujeito, verbo_principal, argumentos = oracao
    print("Oração completa:", oracao_completa)
    print("Sujeito:", sujeito)
    print("Verbo Principal:", verbo_principal)
    print("Argumentos:", argumentos)
    print("=====")

    


# In[ ]:





# In[5]:


import spacy

# Carregar o modelo de idioma em inglês
nlp = spacy.load("en_core_web_sm")

# Ler o arquivo "oracoes_contexto_ampliado.txt" e obter as orações em contexto ampliado
with open("oracoes_contexto_ampliado.txt", "r", encoding="utf-8") as file:
    texto = file.read()

# Processar o texto com o modelo do spaCy
doc = nlp(texto)

# Listas para armazenar as orações passivas e não passivas
passivas = []
nao_passivas = []

# Iterar pelas sentenças do documento
for sentenca in doc.sents:
    # Verificar se a sentença contém uma construção de voz passiva
    if any(token.dep_ == "auxpass" or token.dep_ == "nsubjpass" for token in sentenca):
        # Adicionar a sentença à lista de orações passivas
        passivas.append(sentenca.text)
    else:
        # Adicionar a sentença à lista de orações não passivas
        nao_passivas.append(sentenca.text)

# Listas para armazenar as get-passives e be-passives
get_passives = []
be_passives = []

# Separar as passivas em get-passives e be-passives
for oracao in passivas:
    # Processar a oração com o modelo do spaCy
    doc_oracao = nlp(oracao)
    # Verificar se a oração é uma get-passive (contém o verbo "get")
    if any(token.lemma_ == "get" for token in doc_oracao):
        get_passives.append(oracao)
    # Verificar se a oração é uma be-passive (contém o verbo "be")
    elif any(token.lemma_ == "be" for token in doc_oracao):
        be_passives.append(oracao)

# Criar o arquivo "passivas.txt" e escrever as orações passivas encontradas
with open("passivas.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(passivas))

# Criar o arquivo "nao_passivas.txt" e escrever as orações não passivas encontradas
with open("nao_passivas.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(nao_passivas))

# Criar o arquivo "get_passives.txt" e escrever as get-passives encontradas
with open("get_passives.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(get_passives))

# Criar o arquivo "be_passives.txt" e escrever as be-passives encontradas
with open("be_passives.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(be_passives))


# In[8]:


import spacy

# Carregar o modelo de idioma em inglês
nlp = spacy.load("en_core_web_sm")

# Ler o arquivo "oracoes_contexto_ampliado.txt" e obter as orações em contexto ampliado
with open("oracoes_contexto_ampliado.txt", "r", encoding="utf-8") as file:
    texto = file.read()

# Processar o texto com o modelo do spaCy
doc = nlp(texto)

# Listas para armazenar as orações passivas e não passivas
passivas = []
nao_passivas = []

# Iterar pelas sentenças do documento
for sentenca in doc.sents:
    # Verificar se a sentença contém uma construção de voz passiva
    if any(token.dep_ == "auxpass" or token.dep_ == "nsubjpass" for token in sentenca):
        # Adicionar a sentença à lista de orações passivas
        passivas.append(sentenca.text)
    else:
        # Adicionar a sentença à lista de orações não passivas
        nao_passivas.append(sentenca.text)

# Criar o arquivo "passivas.txt" e escrever as orações passivas encontradas
with open("passivas.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(passivas))

# Criar o arquivo "nao_passivas.txt" e escrever as orações não passivas encontradas
with open("nao_passivas.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(nao_passivas))

# Criar o arquivo "verbos_passados.txt" e escrever as estruturas passivas encontradas
with open("verbos_passados.txt", "w", encoding="utf-8") as file:
    for oracao in passivas:
        doc_oracao = nlp(oracao)
        verbos_passados = [
            token.text for token in doc_oracao if token.dep_ == "auxpass" or token.dep_ == "nsubjpass"
        ]
        # Obter o VP posposto ao Verbal Phrase passivo
        vp_posposto = ""
        for token in doc_oracao:
            if token.head.text in verbos_passados and token.dep_ == "pobj":
                vp_posposto = token.text
                break
        file.write(" ".join(verbos_passados))
        if vp_posposto:
            file.write(" " + vp_posposto)
        file.write("\n")


# In[9]:


import spacy

# Carregar o modelo de idioma em inglês
nlp = spacy.load("en_core_web_sm")

# Ler o arquivo "oracoes_contexto_ampliado.txt" e obter as orações em contexto ampliado
with open("oracoes_contexto_ampliado.txt", "r", encoding="utf-8") as file:
    texto = file.read()

# Processar o texto com o modelo do spaCy
doc = nlp(texto)

# Conjunto para armazenar as orações passivas únicas
passivas_unicas = set()

# Iterar pelas sentenças do documento
for sentenca in doc.sents:
    # Verificar se a sentença contém uma construção de voz passiva
    if any(token.dep_ == "auxpass" or token.dep_ == "nsubjpass" for token in sentenca):
        # Obter a oração em formato de texto
        oracao_texto = sentenca.text.strip()
        # Adicionar a oração ao conjunto de orações passivas únicas
        passivas_unicas.add(oracao_texto)

# Criar o arquivo "passivas.txt" e escrever as orações passivas encontradas
with open("passivas.txt", "w", encoding="utf-8") as file:
    for oracao in passivas_unicas:
        doc_oracao = nlp(oracao)
        tokens_destacados = []
        for token in doc_oracao:
            if token.dep_ == "auxpass" or token.dep_ == "nsubjpass":
                tokens_destacados.append(f"**{token.text}**")
            else:
                tokens_destacados.append(token.text)
        oracao_destacada = " ".join(tokens_destacados)
        file.write(oracao_destacada + "\n")


# In[20]:


# Ler o arquivo "oracoes_contexto_ampliado.txt" e obter as orações em contexto ampliado
with open("oracoes_contexto_ampliado.txt", "r", encoding="utf-8") as file:
    oracoes_ampliadas = file.readlines()

# Ler o arquivo "passivas.txt" e obter as orações passivas
with open("passivas.txt", "r", encoding="utf-8") as file:
    oracoes_passivas = file.readlines()

# Converter as orações em conjuntos para facilitar a comparação
oracoes_ampliadas = set(oracoes_ampliadas)
oracoes_passivas = set(oracoes_passivas)

# Obter as orações distintas
oracoes_distintas = oracoes_ampliadas - oracoes_passivas

# Criar o arquivo "oracoes_distintas.txt" e escrever as orações distintas
with open("oracoes_distintas.txt", "w", encoding="utf-8") as file:
    for oracao in oracoes_distintas:
        file.write(oracao)


# In[25]:


import spacy
from collections import Counter

# Carregar o modelo de idioma em inglês
nlp = spacy.load("en_core_web_sm")

# Ler o arquivo "passivas.txt"
with open("passivas.txt", "r", encoding="utf-8") as file:
    passivas = file.readlines()

# Processar as orações com o modelo do spaCy e extrair os sujeitos da voz passiva
sujeitos = []
for linha in passivas:
    oracao = linha.strip()
    doc = nlp(oracao)
    for token in doc:
        if token.dep_ == "nsubj":
            sujeitos.append(token.text)

# Contar a frequência dos sujeitos
frequencia_sujeitos = Counter(sujeitos)

# Imprimir a lista de frequência dos sujeitos
for sujeito, frequencia in frequencia_sujeitos.items():
    print(sujeito, frequencia)


# In[26]:


import spacy
from collections import Counter

# Carregar o modelo de idioma em inglês
nlp = spacy.load("en_core_web_sm")

# Lista dos sujeitos de interesse
sujeitos_interesse = ["chief", "Prigozhin", "Putin", "leader", "rebellion", "Russian", "Russians", "Russia",
                      "Ukraine", "Kremlin", "troops", "residents", "governor", "Wagner", "soldiers", "US",
                      "Pentagon", "invasion", "Bakhmut", "fighters", "Zelensky", "civilians", "president",
                      "government", "Kyiv", "forces"]

# Ler o arquivo "passivas.txt"
with open("passivas.txt", "r", encoding="utf-8") as file:
    passivas = file.readlines()

# Processar as orações com o modelo do spaCy e extrair os sujeitos da voz passiva
sujeitos = []
for linha in passivas:
    oracao = linha.strip()
    doc = nlp(oracao)
    for token in doc:
        if token.dep_ == "nsubj" and token.text in sujeitos_interesse:
            sujeitos.append(token.text)

# Contar a frequência dos sujeitos
frequencia_sujeitos = Counter(sujeitos)

# Imprimir a lista de frequência dos sujeitos
for sujeito in sujeitos_interesse:
    frequencia = frequencia_sujeitos[sujeito]
    print(sujeito, frequencia)


# In[27]:


import spacy
from collections import Counter
import matplotlib.pyplot as plt

# Carregar o modelo de idioma em inglês
nlp = spacy.load("en_core_web_sm")

# Lista dos sujeitos de interesse
sujeitos_interesse = ["chief", "Prigozhin", "Putin", "leader", "rebellion", "Russian", "Russians", "Russia",
                      "Ukraine", "Kremlin", "troops", "residents", "governor", "Wagner", "soldiers", "US",
                      "Pentagon", "invasion", "Bakhmut", "fighters", "Zelensky", "civilians", "president",
                      "government", "Kyiv", "forces"]

# Ler o arquivo "passivas.txt"
with open("passivas.txt", "r", encoding="utf-8") as file:
    passivas = file.readlines()

# Processar as orações com o modelo do spaCy e extrair os sujeitos da voz passiva
sujeitos = []
for linha in passivas:
    oracao = linha.strip()
    doc = nlp(oracao)
    for token in doc:
        if token.dep_ == "nsubj" and token.text in sujeitos_interesse:
            sujeitos.append(token.text)

# Contar a frequência dos sujeitos
frequencia_sujeitos = Counter(sujeitos)

# Obter as palavras e as frequências
palavras = list(frequencia_sujeitos.keys())
frequencias = list(frequencia_sujeitos.values())

# Plotar o gráfico de barras
plt.bar(palavras, frequencias)
plt.xlabel('Sujeitos')
plt.ylabel('Frequência')
plt.title('Frequência dos Sujeitos em Passivas')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# In[28]:


import spacy
from collections import defaultdict

# Carregar o modelo de idioma em inglês
nlp = spacy.load("en_core_web_sm")

# Definir as palavras-chave para categorização
anti_russia_keywords = ["Putin", "Russian", "Russians", "Russia", "invasion", "Kremlin"]
anti_ukraine_keywords = ["Kyiv", "Ukraine", "Pentagon", "Zelensky", "US"]

# Ler o arquivo "passivas.txt"
with open("passivas.txt", "r", encoding="utf-8") as file:
    passivas = file.readlines()

# Dicionários para armazenar as orações por categoria
anti_russia_oracoes = defaultdict(list)
anti_ukraine_oracoes = defaultdict(list)
outros_oracoes = defaultdict(list)

# Processar as orações com o modelo do spaCy e classificar os sujeitos
for linha in passivas:
    oracao = linha.strip()
    doc = nlp(oracao)
    sujeito = ""
    for token in doc:
        if token.dep_ == "nsubj":
            sujeito = token.text
            break
    if sujeito:
        if any(keyword in oracao for keyword in anti_russia_keywords):
            anti_russia_oracoes[sujeito].append(oracao)
        elif any(keyword in oracao for keyword in anti_ukraine_keywords):
            anti_ukraine_oracoes[sujeito].append(oracao)
        else:
            outros_oracoes[sujeito].append(oracao)

# Escrever as orações classificadas em um arquivo de texto
with open("oracoes_classificadas.txt", "w", encoding="utf-8") as file:
    for sujeito, oracoes in anti_russia_oracoes.items():
        file.write(f"Anti-Rússia\n")
        file.write(f"Sujeito: {sujeito}\n")
        file.write("\n".join(oracoes))
        file.write("\n\n")
    for sujeito, oracoes in anti_ukraine_oracoes.items():
        file.write(f"Anti-Ucrânia\n")
        file.write(f"Sujeito: {sujeito}\n")
        file.write("\n".join(oracoes))
        file.write("\n\n")
    for sujeito, oracoes in outros_oracoes.items():
        file.write(f"Outros\n")
        file.write(f"Sujeito: {sujeito}\n")
        file.write("\n".join(oracoes))
        file.write("\n\n")


# In[29]:


import spacy
from collections import Counter

# Carregar o modelo de idioma em inglês
nlp = spacy.load("en_core_web_sm")

# Ler o arquivo "ativas.txt"
with open("ativas.txt", "r", encoding="utf-8") as file:
    ativas = file.readlines()

# Processar as orações com o modelo do spaCy e extrair os sujeitos da voz ativa
sujeitos = []
for linha in ativas:
    oracao = linha.strip()
    doc = nlp(oracao)
    for token in doc:
        if token.dep_ == "nsubj":
            sujeitos.append(token.text)

# Contar a frequência dos sujeitos
frequencia_sujeitos = Counter(sujeitos)

# Imprimir a lista de frequência dos sujeitos
for sujeito, frequencia in frequencia_sujeitos.items():
    print(sujeito, frequencia)


# In[33]:


import spacy
from collections import Counter

# Carregar o modelo de idioma em inglês
nlp = spacy.load("en_core_web_sm")

# Ler o arquivo "ativas.txt"
with open("ativas.txt", "r", encoding="utf-8") as file:
    ativas = file.readlines()

# Processar as orações com o modelo do spaCy e extrair os sujeitos da voz ativa
sujeitos = []
palavras_interesse = ["Putin", "Russian", "Russians", "Russia", "invasion", "Kremlin", "Kyiv", "Ukraine", "Pentagon", "Zelensky", "US"]

for linha in ativas:
    oracao = linha.strip()
    doc = nlp(oracao)
    for token in doc:
        if token.dep_ == "nsubj" and token.text in palavras_interesse:
            sujeitos.append(token.text)

# Contar a frequência dos sujeitos
frequencia_sujeitos = Counter(sujeitos)

# Imprimir a lista de frequência dos sujeitos
for sujeito in palavras_interesse:
    frequencia = frequencia_sujeitos[sujeito]
    print(sujeito, frequencia)


# In[34]:


import spacy
from collections import Counter
import matplotlib.pyplot as plt

# Carregar o modelo de idioma em inglês
nlp = spacy.load("en_core_web_sm")

# Ler o arquivo "ativas.txt"
with open("ativas.txt", "r", encoding="utf-8") as file:
    ativas = file.readlines()

# Processar as orações com o modelo do spaCy e extrair os sujeitos da voz ativa
sujeitos = []
palavras_interesse = ["Putin", "Russian", "Russians", "Russia", "invasion", "Kremlin", "Kyiv", "Ukraine", "Pentagon", "Zelensky", "US"]

for linha in ativas:
    oracao = linha.strip()
    doc = nlp(oracao)
    for token in doc:
        if token.dep_ == "nsubj" and token.text in palavras_interesse:
            sujeitos.append(token.text)

# Contar a frequência dos sujeitos
frequencia_sujeitos = Counter(sujeitos)

# Obter os sujeitos e frequências como listas separadas
sujeitos_lista = list(frequencia_sujeitos.keys())
frequencias_lista = list(frequencia_sujeitos.values())

# Criar o gráfico de barras
plt.bar(sujeitos_lista, frequencias_lista)
plt.xlabel("Sujeitos")
plt.ylabel("Frequência")
plt.title("Frequência dos Sujeitos em Ativas.txt")
plt.xticks(rotation=90)

# Exibir o gráfico
plt.show()


# In[35]:


# Frequência dos sujeitos em ativas.txt
frequencia_ativas = {
    "Putin": 122,
    "Zelensky": 17,
    "Russia": 73,
    "Ukraine": 24
}

# Frequência dos sujeitos em passivas.txt
frequencia_passivas = {
    "Putin": 36,
    "Zelensky": 3,
    "Russia": 18,
    "Ukraine": 8
}

# Total da frequência em ativas.txt
total_frequencia_ativas = sum(frequencia_ativas.values())

# Total da frequência em passivas.txt
total_frequencia_passivas = sum(frequencia_passivas.values())

# Proporção entre o total da frequência em ativas.txt e passivas.txt
proporcao_total = total_frequencia_ativas / total_frequencia_passivas

# Proporção entre a frequência de "Putin" em ativas.txt e passivas.txt
proporcao_putin = frequencia_ativas["Putin"] / frequencia_passivas["Putin"]

# Proporção entre a frequência de "Zelensky" em ativas.txt e passivas.txt
proporcao_zelensky = frequencia_ativas["Zelensky"] / frequencia_passivas["Zelensky"]

# Proporção entre a frequência de "Russia" em ativas.txt e passivas.txt
proporcao_russia = frequencia_ativas["Russia"] / frequencia_passivas["Russia"]

# Proporção entre a frequência de "Putin" e "Zelensky" em ativas.txt
proporcao_putin_zelensky_ativas = frequencia_ativas["Putin"] / frequencia_ativas["Zelensky"]

# Proporção entre a frequência de "Putin" e "Zelensky" em passivas.txt
proporcao_putin_zelensky_passivas = frequencia_passivas["Putin"] / frequencia_passivas["Zelensky"]

# Proporção entre a frequência de "Russia" e "Ukraine" em ativas.txt
proporcao_russia_ukraine_ativas = frequencia_ativas["Russia"] / frequencia_ativas["Ukraine"]

# Proporção entre a frequência de "Russia" e "Ukraine" em passivas.txt
proporcao_russia_ukraine_passivas = frequencia_passivas["Russia"] / frequencia_passivas["Ukraine"]

# Imprimir as proporções calculadas
print("Proporção entre o total da frequência em ativas.txt e passivas.txt:", proporcao_total)
print("Proporção entre a frequência de 'Putin' em ativas.txt e passivas.txt:", proporcao_putin)
print("Proporção entre a frequência de 'Zelensky' em ativas.txt e passivas.txt:", proporcao_zelensky)
print("Proporção entre a frequência de 'Russia' em ativas.txt e passivas.txt:", proporcao_russia)
print("Proporção entre a frequência de 'Putin' e 'Zelensky' em ativas.txt:", proporcao_putin_zelensky_ativas)
print("Proporção entre a frequência de 'Putin' e 'Zelensky' em passivas.txt:", proporcao_putin_zelensky_passivas)
print("Proporção entre a frequência de 'Russia' e 'Ukraine' em ativas.txt:", proporcao_russia_ukraine_ativas)
print("Proporção entre a frequência de 'Russia' e 'Ukraine' em passivas.txt:", proporcao_russia_ukraine_passivas)


# In[36]:


# Frequência de 'Russia' em ativas.txt
frequencia_russia_ativas = frequencia_ativas['Russia']

# Frequência de 'Russia' em passivas.txt
frequencia_russia_passivas = frequencia_passivas['Russia']

# Proporção entre a frequência de 'Russia' em ativas.txt e passivas.txt
proporcao_russia_ativas_passivas = frequencia_russia_ativas / frequencia_russia_passivas

# Frequência de 'Ukraine' em ativas.txt
frequencia_ukraine_ativas = frequencia_ativas['Ukraine']

# Frequência de 'Ukraine' em passivas.txt
frequencia_ukraine_passivas = frequencia_passivas['Ukraine']

# Proporção entre a frequência de 'Ukraine' em ativas.txt e passivas.txt
proporcao_ukraine_ativas_passivas = frequencia_ukraine_ativas / frequencia_ukraine_passivas

# Imprimir as proporções calculadas
print("Proporção entre a frequência de 'Russia' em ativas.txt e passivas.txt:", proporcao_russia_ativas_passivas)
print("Proporção entre a frequência de 'Ukraine' em ativas.txt e passivas.txt:", proporcao_ukraine_ativas_passivas)



# In[37]:


import matplotlib.pyplot as plt

# Dados das proporções
proporcoes_russia = [proporcao_russia_ativas_passivas, proporcao_russia_passivas_ativas]
proporcoes_ukraine = [proporcao_ukraine_ativas_passivas, proporcao_ukraine_passivas_ativas]

# Labels das proporções
labels = ['Russia em Ativas', 'Russia em Passivas', 'Ukraine em Ativas', 'Ukraine em Passivas']

# Criar o gráfico
fig, ax = plt.subplots()

# Plotar os pontos no gráfico
ax.scatter(proporcoes_russia, range(2), color='red', label='Russia')
ax.scatter(proporcoes_ukraine, range(2), color='blue', label='Ukraine')

# Adicionar as linhas verticais
ax.vlines(proporcoes_russia, ymin=-0.2, ymax=0.2, colors='red', lw=2)
ax.vlines(proporcoes_ukraine, ymin=0.8, ymax=1.2, colors='blue', lw=2)

# Definir os limites do eixo x
ax.set_xlim(0, max(proporcoes_russia + proporcoes_ukraine) + 0.1)

# Definir os rótulos do eixo y
ax.set_yticks(range(2))
ax.set_yticklabels(['Ativas', 'Passivas'])

# Adicionar o título e legenda
plt.title('Proporções de Frequência em Ativas.txt e Passivas.txt')
plt.legend(loc='lower right')

# Mostrar o gráfico
plt.show()


# In[38]:


# Frequência dos sujeitos em ativas.txt
frequencia_ativas = {
    "Putin": 122,
    "Zelensky": 17,
    "Russia": 73,
    "Ukraine": 24
}

# Frequência dos sujeitos em passivas.txt
frequencia_passivas = {
    "Putin": 36,
    "Zelensky": 3,
    "Russia": 18,
    "Ukraine": 8
}

# Total da frequência em ativas.txt
total_frequencia_ativas = sum(frequencia_ativas.values())

# Total da frequência em passivas.txt
total_frequencia_passivas = sum(frequencia_passivas.values())

# Proporção entre o total da frequência em ativas.txt e passivas.txt
proporcao_total = total_frequencia_ativas / total_frequencia_passivas

# Proporção entre a frequência de "Putin" em ativas.txt e passivas.txt
proporcao_putin = frequencia_ativas["Putin"] / frequencia_passivas["Putin"]

# Proporção entre a frequência de "Zelensky" em ativas.txt e passivas.txt
proporcao_zelensky = frequencia_ativas["Zelensky"] / frequencia_passivas["Zelensky"]

# Proporção entre a frequência de "Russia" em ativas.txt e passivas.txt
proporcao_russia = frequencia_ativas["Russia"] / frequencia_passivas["Russia"]

# Proporção entre a frequência de "Putin" e "Zelensky" em ativas.txt
proporcao_putin_zelensky_ativas = frequencia_ativas["Putin"] / frequencia_ativas["Zelensky"]

# Proporção entre a frequência de "Putin" e "Zelensky" em passivas.txt
proporcao_putin_zelensky_passivas = frequencia_passivas["Putin"] / frequencia_passivas["Zelensky"]

# Proporção entre a frequência de "Russia" e "Ukraine" em ativas.txt
proporcao_russia_ukraine_ativas = frequencia_ativas["Russia"] / frequencia_ativas["Ukraine"]

# Proporção entre a frequência de "Russia" e "Ukraine" em passivas.txt
proporcao_russia_ukraine_passivas = frequencia_passivas["Russia"] / frequencia_passivas["Ukraine"]


# In[39]:


# Frequência dos sujeitos em ativas.txt
frequencia_ativas = {
    "Putin": 122,
    "Zelensky": 17,
    "Russia": 73,
    "Ukraine": 24
}

# Frequência dos sujeitos em passivas.txt
frequencia_passivas = {
    "Putin": 36,
    "Zelensky": 3,
    "Russia": 18,
    "Ukraine": 8
}

# Total da frequência em ativas.txt
total_frequencia_ativas = sum(frequencia_ativas.values())

# Total da frequência em passivas.txt
total_frequencia_passivas = sum(frequencia_passivas.values())

# Proporção entre o total da frequência em ativas.txt e passivas.txt
proporcao_total = total_frequencia_ativas / total_frequencia_passivas

# Proporção entre a frequência de "Putin" em ativas.txt e passivas.txt
proporcao_putin = frequencia_ativas["Putin"] / frequencia_passivas["Putin"]

# Proporção entre a frequência de "Zelensky" em ativas.txt e passivas.txt
proporcao_zelensky = frequencia_ativas["Zelensky"] / frequencia_passivas["Zelensky"]

# Proporção entre a frequência de "Russia" em ativas.txt e passivas.txt
proporcao_russia = frequencia_ativas["Russia"] / frequencia_passivas["Russia"]

# Proporção entre a frequência de "Putin" e "Zelensky" em ativas.txt
proporcao_putin_zelensky_ativas = frequencia_ativas["Putin"] / frequencia_ativas["Zelensky"]

# Proporção entre a frequência de "Putin" e "Zelensky" em passivas.txt
proporcao_putin_zelensky_passivas = frequencia_passivas["Putin"] / frequencia_passivas["Zelensky"]

# Proporção entre a frequência de "Russia" e "Ukraine" em ativas.txt
proporcao_russia_ukraine_ativas = frequencia_ativas["Russia"] / frequencia_ativas["Ukraine"]

# Proporção entre a frequência de "Russia" e "Ukraine" em passivas.txt
proporcao_russia_ukraine_passivas = frequencia_passivas["Russia"] / frequencia_passivas["Ukraine"]

# Frequência dos sujeitos em ativas.txt
frequencia_ativas = {
    "Putin": 122,
    "Zelensky": 17,
    "Russia": 73,
    "Ukraine": 24
}

# Frequência dos sujeitos em passivas.txt
frequencia_passivas = {
    "Putin": 36,
    "Zelensky": 3,
    "Russia": 18,
    "Ukraine": 8
}

# Total da frequência em ativas.txt
total_frequencia_ativas = sum(frequencia_ativas.values())

# Total da frequência em passivas.txt
total_frequencia_passivas = sum(frequencia_passivas.values())

# Proporção entre o total da frequência em ativas.txt e passivas.txt
proporcao_total = total_frequencia_ativas / total_frequencia_passivas

# Proporção entre a frequência de "Putin" em ativas.txt e passivas.txt
proporcao_putin = frequencia_ativas["Putin"] / frequencia_passivas["Putin"]

# Proporção entre a frequência de "Zelensky" em ativas.txt e passivas.txt
proporcao_zelensky = frequencia_ativas["Zelensky"] / frequencia_passivas["Zelensky"]

# Proporção entre a frequência de "Russia" em ativas.txt e passivas.txt
proporcao_russia = frequencia_ativas["Russia"] / frequencia_passivas["Russia"]

# Proporção entre a frequência de "Putin" e "Zelensky" em ativas.txt
proporcao_putin_zelensky_ativas = frequencia_ativas["Putin"] / frequencia_ativas["Zelensky"]

# Proporção entre a frequência de "Putin" e "Zelensky" em passivas.txt
proporcao_putin_zelensky_passivas = frequencia_passivas["Putin"] / frequencia_passivas["Zelensky"]

# Proporção entre a frequência de "Russia" e "Ukraine" em ativas.txt
proporcao_russia_ukraine_ativas = frequencia_ativas["Russia"] / frequencia_ativas["Ukraine"]

# Proporção entre a frequência de "Russia" e "Ukraine" em passivas.txt
proporcao_russia_ukraine_passivas = frequencia_passivas["Russia"] / frequencia_passivas["Ukraine"]

import matplotlib.pyplot as plt

# Dados das proporções
proporcoes_russia = [proporcao_russia_ativas_passivas, proporcao_russia_passivas_ativas]
proporcoes_ukraine = [proporcao_ukraine_ativas_passivas, proporcao_ukraine_passivas_ativas]

# Labels das proporções
labels = ['Russia em Ativas', 'Russia em Passivas', 'Ukraine em Ativas', 'Ukraine em Passivas']

# Criar o gráfico
fig, ax = plt.subplots()

# Plotar os pontos no gráfico
ax.scatter(proporcoes_russia, range(2), color='red', label='Russia')
ax.scatter(proporcoes_ukraine, range(2), color='blue', label='Ukraine')

# Adicionar as linhas verticais
ax.vlines(proporcoes_russia, ymin=-0.2, ymax=0.2, colors='red', lw=2)
ax.vlines(proporcoes_ukraine, ymin=0.8, ymax=1.2, colors='blue', lw=2)

# Definir os limites do eixo x
ax.set_xlim(0, max(proporcoes_russia + proporcoes_ukraine) + 0.1)

# Definir os rótulos do eixo y
ax.set_yticks(range(2))
ax.set_yticklabels(['Ativas', 'Passivas'])

# Adicionar o título e legenda
plt.title('Proporções de Frequência em Ativas.txt e Passivas.txt')
plt.legend(loc='lower right')

# Mostrar o gráfico
plt.show()


# In[40]:


import matplotlib.pyplot as plt

# Dados das proporções
proporcoes_russia = [proporcao_russia, 1/proporcao_russia]
proporcoes_ukraine = [proporcao_ukraine, 1/proporcao_ukraine]

# Labels das proporções
labels = ['Russia em Ativas', 'Russia em Passivas', 'Ukraine em Ativas', 'Ukraine em Passivas']

# Criar o gráfico
fig, ax = plt.subplots()

# Plotar os pontos no gráfico
ax.scatter(proporcoes_russia, range(2), color='red', label='Russia')
ax.scatter(proporcoes_ukraine, range(2), color='blue', label='Ukraine')

# Adicionar as linhas verticais
ax.vlines(proporcoes_russia, ymin=-0.2, ymax=0.2, colors='red', lw=2)
ax.vlines(proporcoes_ukraine, ymin=0.8, ymax=1.2, colors='blue', lw=2)

# Definir os limites do eixo x
ax.set_xlim(0, max(proporcoes_russia + proporcoes_ukraine) + 0.1)

# Definir os rótulos do eixo y
ax.set_yticks(range(2))
ax.set_yticklabels(['Ativas', 'Passivas'])

# Adicionar o título e legenda
plt.title('Proporções de Frequência em Ativas.txt e Passivas.txt')
plt.legend(loc='lower right')

# Mostrar o gráfico
plt.show()


# In[41]:


import matplotlib.pyplot as plt

# Dados das proporções
proporcoes_russia = [proporcao_russia, 1/proporcao_russia]
proporcoes_ukraine = [proporcao_russia_ukraine_ativas, 1/proporcao_russia_ukraine_ativas]

# Labels das proporções
labels = ['Russia em Ativas', 'Russia em Passivas', 'Ukraine em Ativas', 'Ukraine em Passivas']

# Criar o gráfico
fig, ax = plt.subplots()

# Plotar os pontos no gráfico
ax.scatter(proporcoes_russia, range(2), color='red', label='Russia')
ax.scatter(proporcoes_ukraine, range(2), color='blue', label='Ukraine')

# Adicionar as linhas verticais
ax.vlines(proporcoes_russia, ymin=-0.2, ymax=0.2, colors='red', lw=2)
ax.vlines(proporcoes_ukraine, ymin=0.8, ymax=1.2, colors='blue', lw=2)

# Definir os limites do eixo x
ax.set_xlim(0, max(proporcoes_russia + proporcoes_ukraine) + 0.1)

# Definir os rótulos do eixo y
ax.set_yticks(range(2))
ax.set_yticklabels(['Ativas', 'Passivas'])

# Adicionar o título e legenda
plt.title('Proporções de Frequência em Ativas.txt e Passivas.txt')
plt.legend(loc='lower right')

# Mostrar o gráfico
plt.show()


# In[42]:


import matplotlib.pyplot as plt
from collections import defaultdict

# Palavras-chave para filtrar os sujeitos
palavras_chave = ["Putin", "Russian", "Russians", "Russia", "invasion", "Kremlin", "Kyiv", "Ukraine", "Pentagon", "Zelensky", "US"]

# Dicionários para armazenar as frequências
frequencias_contra_ucrania = defaultdict(int)
frequencias_contra_russia = defaultdict(int)
frequencias_ativas = defaultdict(int)

# Ler o arquivo "ativas.txt"
with open("ativas.txt", "r", encoding="utf-8") as file:
    ativas = file.readlines()

# Filtrar as orações ativas com sujeitos nas palavras-chave
ativas_filtradas = [oracao.strip() for oracao in ativas if any(palavra in oracao for palavra in palavras_chave)]

# Contar a frequência de cada forma nas orações ativas filtradas
for oracao in ativas_filtradas:
    if "contra-Ucrânia" in oracao:
        frequencias_contra_ucrania["ativas"] += 1
    elif "contra-Rússia" in oracao:
        frequencias_contra_russia["ativas"] += 1
    else:
        frequencias_ativas["ativas"] += 1

# Ler o arquivo "passivas.txt"
with open("passivas.txt", "r", encoding="utf-8") as file:
    passivas = file.readlines()

# Filtrar as orações passivas com sujeitos nas palavras-chave
passivas_filtradas = [oracao.strip() for oracao in passivas if any(palavra in oracao for palavra in palavras_chave)]

# Contar a frequência de cada forma nas orações passivas filtradas
for oracao in passivas_filtradas:
    if "contra-Ucrânia" in oracao:
        frequencias_contra_ucrania["passivas"] += 1
    elif "contra-Rússia" in oracao:
        frequencias_contra_russia["passivas"] += 1
    else:
        frequencias_ativas["passivas"] += 1

# Calcular as probabilidades de escolha para cada forma
total_frequencias = sum(frequencias_contra_ucrania.values()) + sum(frequencias_contra_russia.values()) + sum(frequencias_ativas.values())
prob_contra_ucrania = frequencias_contra_ucrania["ativas"] + frequencias_contra_ucrania["passivas"] / total_frequencias
prob_contra_russia = frequencias_contra_russia["ativas"] + frequencias_contra_russia["passivas"] / total_frequencias
prob_ativas = frequencias_ativas["ativas"] + frequencias_ativas["passivas"] / total_frequencias

# Plotar histograma das probabilidades
formas = ["as contra-Ucrânia", "as contra-Rússia", "ativas"]
probabilidades = [prob_contra_ucrania, prob_contra_russia, prob_ativas]

plt.bar(formas, probabilidades)
plt.xlabel('Formas')
plt.ylabel('Probabilidades')
plt.title('Probabilidade de escolha entre as formas')
plt.show()


# In[43]:


import matplotlib.pyplot as plt

# Palavras-chave para filtrar os sujeitos
palavras_chave = ["Putin", "Russian", "Russians", "Russia", "invasion", "Kremlin", "Kyiv", "Ukraine", "Pentagon", "Zelensky", "US"]

# Dicionários para armazenar as frequências
frequencias_contra_ucrania = 0
frequencias_contra_russia = 0
frequencias_ativas = 0

# Ler o arquivo "ativas.txt"
with open("ativas.txt", "r", encoding="utf-8") as file:
    ativas = file.readlines()

# Filtrar as orações ativas com sujeitos nas palavras-chave
ativas_filtradas = [oracao.strip() for oracao in ativas if any(palavra in oracao for palavra in palavras_chave)]

# Contar a frequência de cada forma nas orações ativas filtradas
for oracao in ativas_filtradas:
    if "contra-Ucrânia" in oracao:
        frequencias_contra_ucrania += 1
    elif "contra-Rússia" in oracao:
        frequencias_contra_russia += 1
    else:
        frequencias_ativas += 1

# Calcular as probabilidades de escolha para cada forma
total_frequencias = frequencias_contra_ucrania + frequencias_contra_russia + frequencias_ativas
prob_contra_ucrania = frequencias_contra_ucrania / total_frequencias
prob_contra_russia = frequencias_contra_russia / total_frequencias
prob_ativas = frequencias_ativas / total_frequencias

# Plotar histograma das probabilidades
formas = ["as contra-Ucrânia", "as contra-Rússia", "ativas"]
probabilidades = [prob_contra_ucrania, prob_contra_russia, prob_ativas]

plt.bar(formas, probabilidades)
plt.xlabel('Formas')
plt.ylabel('Probabilidades')
plt.title('Probabilidade de escolha entre as formas')
plt.show()


# In[44]:


import matplotlib.pyplot as plt

# Palavras-chave para filtrar os sujeitos
palavras_chave = ["Putin", "Russian", "Russians", "Russia", "invasion", "Kremlin", "Kyiv", "Ukraine", "Pentagon", "Zelensky", "US"]

# Dicionários para armazenar as frequências
frequencias_contra_ucrania = 0
frequencias_contra_russia = 0
frequencias_ativas = 0

# Ler o arquivo "ativas.txt"
with open("ativas.txt", "r", encoding="utf-8") as file:
    ativas = file.readlines()

# Filtrar as orações ativas com sujeitos nas palavras-chave
ativas_filtradas = [oracao.strip() for oracao in ativas if any(palavra in oracao.split() for palavra in palavras_chave)]

# Contar a frequência de cada forma nas orações ativas filtradas
for oracao in ativas_filtradas:
    if "as contra-Ucrânia" in oracao:
        frequencias_contra_ucrania += 1
    elif "as contra-Rússia" in oracao:
        frequencias_contra_russia += 1
    else:
        frequencias_ativas += 1

# Calcular as probabilidades de escolha para cada forma
total_frequencias = frequencias_contra_ucrania + frequencias_contra_russia + frequencias_ativas
prob_contra_ucrania = frequencias_contra_ucrania / total_frequencias
prob_contra_russia = frequencias_contra_russia / total_frequencias
prob_ativas = frequencias_ativas / total_frequencias

# Plotar histograma das probabilidades
formas = ["as contra-Ucrânia", "as contra-Rússia", "ativas"]
probabilidades = [prob_contra_ucrania, prob_contra_russia, prob_ativas]

plt.bar(formas, probabilidades)
plt.xlabel('Formas')
plt.ylabel('Probabilidades')
plt.title('Probabilidade de escolha entre as formas')
plt.show()


# In[45]:


import matplotlib.pyplot as plt

# Frequência dos sujeitos em ativas.txt
frequencia_ativas = {
    "Putin": 122,
    "Zelensky": 17,
    "Russia": 73,
    "Ukraine": 24
}

# Frequência dos sujeitos em passivas.txt
frequencia_passivas = {
    "Putin": 36,
    "Zelensky": 3,
    "Russia": 18,
    "Ukraine": 8
}

# Cálculo das frequências totais
frequencia_total = {}
for sujeito, frequencia in frequencia_ativas.items():
    frequencia_total[sujeito] = frequencia + frequencia_passivas[sujeito]

# Cálculo da frequência total da macrocategoria "contra-Russia"
frequencia_contra_russia = frequencia_passivas["Putin"] + frequencia_passivas["Russia"]

# Cálculo da frequência total da macrocategoria "contra-Ucrania"
frequencia_contra_ucrania = frequencia_passivas["Zelensky"] + frequencia_passivas["Ukraine"]

# Cálculo da frequência total de todas as categorias
frequencia_total_todas_categorias = sum(frequencia_total.values()) + frequencia_contra_russia + frequencia_contra_ucrania

# Cálculo das probabilidades
prob_sujeitos = {sujeito: frequencia / frequencia_total_todas_categorias for sujeito, frequencia in frequencia_total.items()}
prob_contra_russia = frequencia_contra_russia / frequencia_total_todas_categorias
prob_contra_ucrania = frequencia_contra_ucrania / frequencia_total_todas_categorias

# Plotagem do histograma das probabilidades
categorias = ["Putin", "Zelensky", "Russia", "Ukraine", "contra-Russia", "contra-Ucrania"]
probabilidades = [prob_sujeitos[sujeito] for sujeito in ["Putin", "Zelensky", "Russia", "Ukraine"]] + [prob_contra_russia, prob_contra_ucrania]

plt.bar(categorias, probabilidades)
plt.xlabel('Categorias')
plt.ylabel('Probabilidades')
plt.title('Probabilidade de escolha das categorias')
plt.show()


# In[46]:


import matplotlib.pyplot as plt

# Frequência dos sujeitos em ativas.txt
frequencia_ativas = {
    "Ativa": 236
}

# Frequência dos sujeitos em passivas.txt
frequencia_passivas = {
    "Putin": 36,
    "Zelensky": 3,
    "Russia": 18,
    "Ukraine": 8
}

# Cálculo das frequências totais
frequencia_total = {
    "Ativa": frequencia_ativas["Ativa"],
    "contra-Russia": frequencia_passivas["Putin"] + frequencia_passivas["Russia"],
    "contra-Ucrania": frequencia_passivas["Zelensky"] + frequencia_passivas["Ukraine"]
}

# Cálculo da frequência total de todas as categorias
frequencia_total_todas_categorias = sum(frequencia_total.values())

# Cálculo das probabilidades
prob_ativa = frequencia_total["Ativa"] / frequencia_total_todas_categorias
prob_contra_russia = frequencia_total["contra-Russia"] / frequencia_total_todas_categorias
prob_contra_ucrania = frequencia_total["contra-Ucrania"] / frequencia_total_todas_categorias

# Plotagem do histograma das probabilidades
categorias = ["Ativa", "contra-Russia", "contra-Ucrania"]
probabilidades = [prob_ativa, prob_contra_russia, prob_contra_ucrania]

plt.bar(categorias, probabilidades)
plt.xlabel('Categorias')
plt.ylabel('Probabilidades')
plt.title('Probabilidade de escolha das categorias')
plt.show()


# In[47]:


import matplotlib.pyplot as plt

# Frequência dos sujeitos em ativas.txt
frequencia_ativas = {
    "Putin": 122,
    "Zelensky": 17,
    "Russia": 73,
    "Ukraine": 24
}

# Frequência dos sujeitos em passivas.txt
frequencia_passivas = {
    "Putin": 36,
    "Zelensky": 3,
    "Russia": 18,
    "Ukraine": 8
}

# Cálculo das frequências totais
frequencia_total_russia = frequencia_ativas["Putin"] + frequencia_passivas["Putin"] + frequencia_passivas["Russia"]
frequencia_total_ucrania = frequencia_ativas["Zelensky"] + frequencia_ativas["Ukraine"] + frequencia_passivas["Zelensky"] + frequencia_passivas["Ukraine"]

# Cálculo das probabilidades
prob_ativas_russia = (frequencia_ativas["Putin"] + frequencia_ativas["Russia"]) / frequencia_total_russia
prob_contra_russia = (frequencia_passivas["Putin"] + frequencia_passivas["Russia"]) / frequencia_total_russia

prob_ativas_ucrania = (frequencia_ativas["Zelensky"] + frequencia_ativas["Ukraine"]) / frequencia_total_ucrania
prob_contra_ucrania = (frequencia_passivas["Zelensky"] + frequencia_passivas["Ukraine"]) / frequencia_total_ucrania

# Plotagem do histograma das probabilidades
categorias = ["Ativas (Russia)", "Contra-Russia", "Ativas (Ucrânia)", "Contra-Ucrânia"]
probabilidades = [prob_ativas_russia, prob_contra_russia, prob_ativas_ucrania, prob_contra_ucrania]

plt.bar(categorias, probabilidades)
plt.xlabel('Categorias')
plt.ylabel('Probabilidades')
plt.title('Probabilidade de escolha das categorias')
plt.show()


# In[48]:


from sympy import symbols, Eq, solve

# Variáveis simbólicas
P_Ativas_Russia, P_Contra_Russia, P_Ativas_Ucrania, P_Contra_Ucrania = symbols('P_Ativas_Russia P_Contra_Russia P_Ativas_Ucrania P_Contra_Ucrania')

# Equação para a relação Ativas Russia e Contra-Russia
eq1 = Eq(P_Ativas_Russia + P_Contra_Russia, 1)
eq2 = Eq(P_Ativas_Russia, (frequencia_ativas["Putin"] + frequencia_ativas["Russia"]) / frequencia_total_russia)
eq3 = Eq(P_Contra_Russia, (frequencia_passivas["Putin"] + frequencia_passivas["Russia"]) / frequencia_total_russia)

# Equação para a relação Ativas Ucrania e Contra-Ucrania
eq4 = Eq(P_Ativas_Ucrania + P_Contra_Ucrania, 1)
eq5 = Eq(P_Ativas_Ucrania, (frequencia_ativas["Zelensky"] + frequencia_ativas["Ukraine"]) / frequencia_total_ucrania)
eq6 = Eq(P_Contra_Ucrania, (frequencia_passivas["Zelensky"] + frequencia_passivas["Ukraine"]) / frequencia_total_ucrania)

# Resolver as equações
solucao = solve((eq1, eq2, eq3, eq4, eq5, eq6), (P_Ativas_Russia, P_Contra_Russia, P_Ativas_Ucrania, P_Contra_Ucrania))

# Obter as fórmulas
formula_Ativas_Russia = solucao[P_Ativas_Russia]
formula_Contra_Russia = solucao[P_Contra_Russia]
formula_Ativas_Ucrania = solucao[P_Ativas_Ucrania]
formula_Contra_Ucrania = solucao[P_Contra_Ucrania]

print("Fórmula para a relação Ativas Russia e Contra-Russia:")
print(formula_Ativas_Russia)
print(formula_Contra_Russia)

print("\nFórmula para a relação Ativas Ucrania e Contra-Ucrania:")
print(formula_Ativas_Ucrania)
print(formula_Contra_Ucrania)


# In[49]:


from sympy import symbols, Eq, solve

# Variáveis simbólicas
P_Ativas_Russia, P_Contra_Russia, P_Ativas_Ucrania, P_Contra_Ucrania = symbols('P_Ativas_Russia P_Contra_Russia P_Ativas_Ucrania P_Contra_Ucrania')

# Equação para a relação Ativas Russia e Contra-Russia
eq1 = Eq(P_Ativas_Russia + P_Contra_Russia, 1)
eq2 = Eq(P_Ativas_Russia, (frequencia_ativas["Putin"] + frequencia_ativas["Russia"]) / frequencia_total_russia)
eq3 = Eq(P_Contra_Russia, (frequencia_passivas["Putin"] + frequencia_passivas["Russia"]) / frequencia_total_russia)

# Equação para a relação Ativas Ucrania e Contra-Ucrania
eq4 = Eq(P_Ativas_Ucrania + P_Contra_Ucrania, 1)
eq5 = Eq(P_Ativas_Ucrania, (frequencia_ativas["Zelensky"] + frequencia_ativas["Ukraine"]) / frequencia_total_ucrania)
eq6 = Eq(P_Contra_Ucrania, (frequencia_passivas["Zelensky"] + frequencia_passivas["Ukraine"]) / frequencia_total_ucrania)

# Resolver as equações
solucao = solve((eq1, eq2, eq3, eq4, eq5, eq6), (P_Ativas_Russia, P_Contra_Russia, P_Ativas_Ucrania, P_Contra_Ucrania))

# Obter as fórmulas
formula_Ativas_Russia = solucao[P_Ativas_Russia].rhs
formula_Contra_Russia = solucao[P_Contra_Russia].rhs
formula_Ativas_Ucrania = solucao[P_Ativas_Ucrania].rhs
formula_Contra_Ucrania = solucao[P_Contra_Ucrania].rhs

print("Fórmula para a relação Ativas Russia e Contra-Russia:")
print(formula_Ativas_Russia)
print(formula_Contra_Russia)

print("\nFórmula para a relação Ativas Ucrania e Contra-Ucrania:")
print(formula_Ativas_Ucrania)
print(formula_Contra_Ucrania)


# In[50]:


ipi install sympy


# In[51]:


pip install sympy


# In[1]:


from sympy import symbols, Eq, solve

# Variáveis simbólicas
P_Ativas_Russia, P_Contra_Russia, P_Ativas_Ucrania, P_Contra_Ucrania = symbols('P_Ativas_Russia P_Contra_Russia P_Ativas_Ucrania P_Contra_Ucrania')

# Equação para a relação Ativas Russia e Contra-Russia
eq1 = Eq(P_Ativas_Russia + P_Contra_Russia, 1)
eq2 = Eq(P_Ativas_Russia, (frequencia_ativas["Putin"] + frequencia_ativas["Russia"]) / frequencia_total_russia)
eq3 = Eq(P_Contra_Russia, (frequencia_passivas["Putin"] + frequencia_passivas["Russia"]) / frequencia_total_russia)

# Equação para a relação Ativas Ucrania e Contra-Ucrania
eq4 = Eq(P_Ativas_Ucrania + P_Contra_Ucrania, 1)
eq5 = Eq(P_Ativas_Ucrania, (frequencia_ativas["Zelensky"] + frequencia_ativas["Ukraine"]) / frequencia_total_ucrania)
eq6 = Eq(P_Contra_Ucrania, (frequencia_passivas["Zelensky"] + frequencia_passivas["Ukraine"]) / frequencia_total_ucrania)

# Resolver as equações
solucao = solve((eq1, eq2, eq3, eq4, eq5, eq6), (P_Ativas_Russia, P_Contra_Russia, P_Ativas_Ucrania, P_Contra_Ucrania))

# Obter as fórmulas
formula_Ativas_Russia = solucao[P_Ativas_Russia].rhs
formula_Contra_Russia = solucao[P_Contra_Russia].rhs
formula_Ativas_Ucrania = solucao[P_Ativas_Ucrania].rhs
formula_Contra_Ucrania = solucao[P_Contra_Ucrania].rhs

print("Fórmula para a relação Ativas Russia e Contra-Russia:")
print(formula_Ativas_Russia)
print(formula_Contra_Russia)

print("\nFórmula para a relação Ativas Ucrania e Contra-Ucrania:")
print(formula_Ativas_Ucrania)
print(formula_Contra_Ucrania)


# In[2]:


from sympy import symbols, Eq, solve

# Variáveis simbólicas
P_Ativas_Russia, P_Contra_Russia, P_Ativas_Ucrania, P_Contra_Ucrania = symbols('P_Ativas_Russia P_Contra_Russia P_Ativas_Ucrania P_Contra_Ucrania')

# Frequências dos sujeitos em ativas.txt
frequencia_ativas = {
    "Putin": 122,
    "Zelensky": 17,
    "Russia": 73,
    "Ukraine": 24
}

# Frequências dos sujeitos em passivas.txt
frequencia_passivas = {
    "Putin": 36,
    "Zelensky": 3,
    "Russia": 18,
    "Ukraine": 8
}

# Frequência total de Ativas Russia
frequencia_total_russia = frequencia_ativas["Putin"] + frequencia_ativas["Russia"]

# Frequência total de Ativas Ucrania
frequencia_total_ucrania = frequencia_ativas["Zelensky"] + frequencia_ativas["Ukraine"]

# Equação para a relação Ativas Russia e Contra-Russia
eq1 = Eq(P_Ativas_Russia + P_Contra_Russia, 1)
eq2 = Eq(P_Ativas_Russia, frequencia_ativas["Russia"] / frequencia_total_russia)
eq3 = Eq(P_Contra_Russia, (frequencia_passivas["Putin"] + frequencia_passivas["Russia"]) / frequencia_total_russia)

# Equação para a relação Ativas Ucrania e Contra-Ucrania
eq4 = Eq(P_Ativas_Ucrania + P_Contra_Ucrania, 1)
eq5 = Eq(P_Ativas_Ucrania, frequencia_ativas["Ukraine"] / frequencia_total_ucrania)
eq6 = Eq(P_Contra_Ucrania, (frequencia_passivas["Zelensky"] + frequencia_passivas["Ukraine"]) / frequencia_total_ucrania)

# Resolver as equações
solucao = solve((eq1, eq2, eq3, eq4, eq5, eq6), (P_Ativas_Russia, P_Contra_Russia, P_Ativas_Ucrania, P_Contra_Ucrania))

# Obter as fórmulas
formula_Ativas_Russia = solucao[P_Ativas_Russia].rhs
formula_Contra_Russia = solucao[P_Contra_Russia].rhs
formula_Ativas_Ucrania = solucao[P_Ativas_Ucrania].rhs
formula_Contra_Ucrania = solucao[P_Contra_Ucrania].rhs

print("Fórmula para a relação Ativas Russia e Contra-Russia:")
print(formula_Ativas_Russia)
print(formula_Contra_Russia)

print("\nFórmula para a relação Ativas Ucrania e Contra-Ucrania:")
print(formula_Ativas_Ucrania)
print(formula_Contra_Ucrania)


# In[3]:


from sympy import symbols, Eq, solve

# Variáveis simbólicas
P_Ativas_Russia, P_Contra_Russia, P_Ativas_Ucrania, P_Contra_Ucrania = symbols('P_Ativas_Russia P_Contra_Russia P_Ativas_Ucrania P_Contra_Ucrania')

# Frequências dos sujeitos em ativas.txt
frequencia_ativas = {
    "Putin": 122,
    "Zelensky": 17,
    "Russia": 73,
    "Ukraine": 24
}

# Frequências dos sujeitos em passivas.txt
frequencia_passivas = {
    "Putin": 36,
    "Zelensky": 3,
    "Russia": 18,
    "Ukraine": 8
}

# Frequência total de Ativas Russia
frequencia_total_russia = frequencia_ativas["Putin"] + frequencia_ativas["Russia"]

# Frequência total de Ativas Ucrania
frequencia_total_ucrania = frequencia_ativas["Zelensky"] + frequencia_ativas["Ukraine"]

# Equação para a relação Ativas Russia e Contra-Russia
eq1 = Eq(P_Ativas_Russia + P_Contra_Russia, 1)
eq2 = Eq(P_Ativas_Russia, frequencia_ativas["Russia"] / frequencia_total_russia)
eq3 = Eq(P_Contra_Russia, (frequencia_passivas["Putin"] + frequencia_passivas["Russia"]) / frequencia_total_russia)

# Equação para a relação Ativas Ucrania e Contra-Ucrania
eq4 = Eq(P_Ativas_Ucrania + P_Contra_Ucrania, 1)
eq5 = Eq(P_Ativas_Ucrania, frequencia_ativas["Ukraine"] / frequencia_total_ucrania)
eq6 = Eq(P_Contra_Ucrania, (frequencia_passivas["Zelensky"] + frequencia_passivas["Ukraine"]) / frequencia_total_ucrania)

# Resolver as equações
solucao = solve((eq1, eq2, eq3, eq4, eq5, eq6), (P_Ativas_Russia, P_Contra_Russia, P_Ativas_Ucrania, P_Contra_Ucrania))

# Obter as fórmulas
formula_Ativas_Russia = solucao[0][P_Ativas_Russia]
formula_Contra_Russia = solucao[0][P_Contra_Russia]
formula_Ativas_Ucrania = solucao[0][P_Ativas_Ucrania]
formula_Contra_Ucrania = solucao[0][P_Contra_Ucrania]

print("Fórmula para a relação Ativas Russia e Contra-Russia:")
print(formula_Ativas_Russia)
print(formula_Contra_Russia)

print("\nFórmula para a relação Ativas Ucrania e Contra-Ucrania:")
print(formula_Ativas_Ucrania)
print(formula_Contra_Ucrania)


# In[4]:


from sympy import symbols, Eq, solve

# Variáveis simbólicas
P_Ativas_Russia, P_Contra_Russia, P_Ativas_Ucrania, P_Contra_Ucrania = symbols('P_Ativas_Russia P_Contra_Russia P_Ativas_Ucrania P_Contra_Ucrania')

# Frequências dos sujeitos em ativas.txt
frequencia_ativas = {
    "Putin": 122,
    "Zelensky": 17,
    "Russia": 73,
    "Ukraine": 24
}

# Frequências dos sujeitos em passivas.txt
frequencia_passivas = {
    "Putin": 36,
    "Zelensky": 3,
    "Russia": 18,
    "Ukraine": 8
}

# Frequência total de Ativas Russia
frequencia_total_russia = frequencia_ativas["Putin"] + frequencia_ativas["Russia"]

# Frequência total de Ativas Ucrania
frequencia_total_ucrania = frequencia_ativas["Zelensky"] + frequencia_ativas["Ukraine"]

# Equação para a relação Ativas Russia e Contra-Russia
eq1 = Eq(P_Ativas_Russia + P_Contra_Russia, 1)
eq2 = Eq(P_Ativas_Russia, frequencia_ativas["Russia"] / frequencia_total_russia)
eq3 = Eq(P_Contra_Russia, (frequencia_passivas["Putin"] + frequencia_passivas["Russia"]) / frequencia_total_russia)

# Equação para a relação Ativas Ucrania e Contra-Ucrania
eq4 = Eq(P_Ativas_Ucrania + P_Contra_Ucrania, 1)
eq5 = Eq(P_Ativas_Ucrania, frequencia_ativas["Ukraine"] / frequencia_total_ucrania)
eq6 = Eq(P_Contra_Ucrania, (frequencia_passivas["Zelensky"] + frequencia_passivas["Ukraine"]) / frequencia_total_ucrania)

# Resolver as equações
solucao = solve((eq1, eq2, eq3, eq4, eq5, eq6), (P_Ativas_Russia, P_Contra_Russia, P_Ativas_Ucrania, P_Contra_Ucrania))

if solucao:
    # Obter as fórmulas
    formula_Ativas_Russia = solucao[0][P_Ativas_Russia]
    formula_Contra_Russia = solucao[0][P_Contra_Russia]
    formula_Ativas_Ucrania = solucao[0][P_Ativas_Ucrania]
    formula_Contra_Ucrania = solucao[0][P_Contra_Ucrania]

    print("Fórmula para a relação Ativas Russia e Contra-Russia:")
    print(formula_Ativas_Russia)
    print(formula_Contra_Russia)

    print("\nFórmula para a relação Ativas Ucrania e Contra-Ucrania:")
    print(formula_Ativas_Ucrania)
    print(formula_Contra_Ucrania)
else:
    print("Não foi possível encontrar uma solução para as equações.")


# In[ ]:




