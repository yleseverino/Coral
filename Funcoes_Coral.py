from bs4 import BeautifulSoup
import tts
from requests import get


def noticias():
	site = get('https://news.google.com/news/rss?ned=pt_br&gl=BR&hl=pt')
	noticias = BeautifulSoup(site.text, 'html.parser')
	for item in noticias.findAll('item')[:2]:
		mensagem = str(item.title.text)
		tts.cria_audio(mensagem)


def iot_setup(modulo, acao, mode):
	if modulo == "rele":
		from IOT_Types import type_rele
		return type_rele(acao, mode)




