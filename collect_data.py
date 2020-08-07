from bs4 import BeautifulSoup
import requests
import pandas as pd


config = {
  "START": 801,
  "COUNT": 200,
}

url = f'https://www.imdb.com/search/title/?title_type=feature,tv_series&count={config["COUNT"]}&start={config["START"]}&ref_=adv_nxt'

html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')

data = {'names': [],
        'rates': [],
        'director': [],
        'actors': []}

movie_list = soup.select('div[class="lister-list"] div[class="lister-item mode-advanced"]')

for movie in movie_list:
  name = movie.h3.a.text
  
  try:
    rate = float(movie.select('div[class="inline-block ratings-imdb-rating"] strong')[0].text)
  except:
    rate = ''

  staff_li = movie.select('p')[2]
  staff_li = staff_li.text.replace('\n', '').split('|')


  director = ""
  actor = ""

  for staff in staff_li:
    if "Director:" in staff:
      director = staff.replace("Director:", "").strip()
    if "Stars:" in staff:
      actor = staff.replace("Stars:", "").strip()

  data["names"].append(name)
  data["rates"].append(rate)
  data["director"].append(director)
  data["actors"].append(actor)


df = pd.DataFrame(data)

df.to_csv(f'{config["START"]}to{config["START"] + config["COUNT"]}_movies.csv', index=False)