from bs4 import BeautifulSoup
import requests

url ="https://www.nasa.gov/"

response= requests.get(url)
parse=BeautifulSoup(response.text,'html.parser')

img_tags=parse.find_all('img')
i=1
for img in img_tags:
    image_source_link=img['src']

    if image_source_link.startswith('http'):
        print(f"IMAGE SRC LINK : {image_source_link}")

        image_data=requests.get(image_source_link).content

        with open (f'images/image_{i}.jpg','wb') as file:
            file.write(image_data)
    i=i+1

