import requests
from bs4 import BeautifulSoup

#you need the imports too

print_progress = False

def search(query, resultcount=0):
  global print_progress
  response = requests.get(f"https://www.google.com/search?q={query}&start=0")

  soup = BeautifulSoup(response.content, 'html.parser')
  results = []

  links = soup.find_all(href=True)
  
  for tag in links:
    if tag.find("h3") != None:
      url = tag["href"][7:]
      url = url[0:url.find("&")]
      if url[0] == "/":
        url = "https:/" + url
      results.append(url)

  if print_progress == True:
    print(f'Googled "{query}"')
  return results
