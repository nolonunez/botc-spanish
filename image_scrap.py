from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bso
import requests
import pandas as pd

dfl = []

def png(edition):

	data = []
	df = pd.DataFrame(data, columns=["role", "image"])
	df.to_csv("images.csv")

	url = edition
	response = requests.get(url)
	response = response.content

	soup = BeautifulSoup(response, "html.parser")
	roles = soup.find_all("div", {"class": "small-6 medium-6 large-2 columns"})

	for role in roles:

		png = role.find("img", {"class": "thumbimage"})
		role_id = png["alt"]

		png = "https://wiki.bloodontheclocktower.com/" + png["src"]
		role_id = role_id.replace("Icon ","").replace(" ","").replace(".png","")

		data.append([role_id,png])

	dff = pd.DataFrame(data, columns=["role", "image"])
	dfl.append(dff)
	print(dff)
	df = pd.concat(dfl).to_csv("images.csv")

png("https://wiki.bloodontheclocktower.com/Trouble_Brewing")
