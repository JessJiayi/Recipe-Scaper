import requests,re
from bs4 import BeautifulSoup

input=input('What dish you want to search? ')
print("")
key=str(input).replace(' ','+')
link="https://www.allrecipes.com/search/results/?search="+key

r=requests.get(link)
c=r.content
soup=BeautifulSoup(c,"html.parser")
all=soup.find_all("div",{"class":"card__detailsContainer-left"})
for recipe in all:
    title=recipe.find_all("h3",{"class":"card__title"})[0].text.replace("\n","").replace("  ","")
    link=recipe.a['href']
    recipe_page=requests.get(link)
    recipe_content=recipe_page.content
    rsoup=BeautifulSoup(recipe_content,"html.parser")
    whole_page=rsoup.find_all("script",{"type":"application/ld+json"})
    ingredients=re.search(re.compile('recipeIngredient[^]]*[]]'),str(whole_page)).group(0).replace('recipeIngredient": [','').replace(']','')
    steps=re.search(re.compile('recipeInstructions[^]]*[]]'),str(whole_page)).group(0).replace('recipeInstructions": [','').replace(']','').replace('{','').replace('"@type": "HowToStep",','').replace('"text":','').replace('},','').replace('"','').replace('}','').replace('\n','').replace('  ','')
    print(title)
    print(ingredients)
    print(steps)
    print("")
