from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

url = ('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250')

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

html =  requests.get(url,headers=headers).content
#Header kısmını sayfa incele yapıp network kısmından aldık eger response olamaz sayfa 403 gibi hatalar verirse bunu yaparız.

soup = BeautifulSoup(html,'html.parser')
#Burda beatifulsoup ile html değişkenini html tarzında parçaladık ve artık soup üzerinden html kodlarını erişebilicez
liste = soup.find('ul',{'class' :'ipc-metadata-list'}).find_all('li',limit=10)
#burda oluşturdugumuz liste değişkenine ilk filmimizin ul içerisinde oldugu ve classının ne oldugunu belirttik find all li ise bütün li etiketlerini al demek limit verme ise kaçtane li yani film alıcaz demek 

for item in liste:                                              #for içine alarak film listesini alt alta yazdırma işlemini gerçekleştirdik
    filmadi = item.find('h3',{'class':'ipc-title__text'}).text #bu filmin adını bulur 
    puan = item.find('span',{'class':'ipc-rating-star'}).text # bu ise filmin puanlama içeriğini bulur 
    
    print(filmadi,puan)

