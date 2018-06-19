from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
from tqdm import tqdm

search = input("Search Images:")
params = {"q":search}
r = requests.get("https://www.bing.com/images/search",params=params)

soup = BeautifulSoup(r.text,"html.parser")
links = soup.findAll('a',{'class':'thumb'})


for items in tqdm(links):
    img_obj = requests.get(items.attrs["href"])
    print ("Getting",items.attrs["href"])
    title = items.attrs["href"].split("/")[-1]
    img = Image.open(BytesIO(img_obj.content))
    img.save("./parsedImages/" + title,img.format)


