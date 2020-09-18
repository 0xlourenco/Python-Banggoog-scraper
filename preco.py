from bs4 import BeautifulSoup
import requests

def go():
	url='https://www.banggood.com/search/arduino.html?from=nav'
	r=requests.get(url)
	print(r.status_code)
	soup=BeautifulSoup(r.text, 'lxml')
	contentor=soup.find(class_='search-main')
	preco=contentor.find_all(class_='price notranslate')
	nome=contentor.find_all(class_='title')
	disconto=contentor.find_all('span', class_='price-old notranslate')
	m=contentor.find_all(class_='price-old-box')
	

	print('')
	fu=len(preco)
	for i in range(fu):
		print(i, '[*]Nome do artigo := ',nome[i].get_text())
		print( 'Preço atual: ',preco[i].get_text())
		print('')
		
	




go()
