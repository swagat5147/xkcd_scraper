import requests
from random import randint
random = randint(1, 2100)
i = requests.get("https://xkcd.com/"+str(random)+"/info.0.json")
if i.status_code == 200:
	image = i.json()
	url = image.get("img")
	text = image.get("alt")
	title = image.get("title")
	img = url.rsplit('/')[-1]
	img_url = requests.get(url)
	with open(img, 'wb+') as out_file:
		out_file.write(img_url.content)
print("Comic no: "+str(random))
print("Caption: "+text)

