import urllib.parse
import requests

# Fråga användaren efter URL att analysera
url = input("Skriv in URL: ")

# Hämta webbsidan
response = requests.get(url)

# Analysera URL:n för att hitta alla sub-sidor
parsed_url = urllib.parse.urlparse(url)
base_url = parsed_url.scheme + "://" + parsed_url.netloc
subpages = set()

for link in response.text.split('href="')[1:]:
    subpage = link.split('"', 1)[0]
    if subpage.startswith('/') or subpage.startswith(base_url):
        subpages.add(subpage)

# Skriv ut alla sub-sidor som hittades
print(f"Sub-sidor på {url}:")
for subpage in subpages:
    print(subpage)
    