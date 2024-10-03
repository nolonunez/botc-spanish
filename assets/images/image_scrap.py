from bs4 import BeautifulSoup
import requests
import pandas as pd

dfl = []

def png(category):

	data = []
	df = pd.DataFrame(data, columns=["role", "image"])
	df.to_csv("./assets/images/images.csv")

	url = category
	response = requests.get(url)
	response = response.content

	soup = BeautifulSoup(response, "html.parser")
	chunk = soup.find("div", {"id": "mw-pages"})

	roles = chunk.find_all("a")

	for role in roles:

		print("Looking for the " + role["title"])
		
		role_url = "https://wiki.bloodontheclocktower.com" + role["href"]

		response = requests.get(role_url)
		response = response.content

		soup = BeautifulSoup(response, "html.parser")

		details = soup.find("div",{"id": "character-details"})
		png = details.find("img")

		role_id = png["alt"]
		role_id = role_id.replace("Icon ","").replace(" ","").replace(".png","")
		role_id = role_id.lower()

		png = "https://wiki.bloodontheclocktower.com/" + png["src"]
		
		data.append([role_id,png])

	dff = pd.DataFrame(data, columns=["role", "image"])
	dfl.append(dff)
	df = pd.concat(dfl).to_csv("./assets/images/images.csv")

	print("Images Ready")

png("https://wiki.bloodontheclocktower.com/Category:Townsfolk")
png("https://wiki.bloodontheclocktower.com/Category:Outsiders")
png("https://wiki.bloodontheclocktower.com/Category:Minions")
png("https://wiki.bloodontheclocktower.com/Category:Demons")

def png2(category):

	data = []
	df = pd.DataFrame(data, columns=["role", "image"])
	df.to_csv("./assets/images/images.csv")

	url = category
	response = requests.get(url)
	response = response.content

	soup = BeautifulSoup(response, "html.parser")
	types = ["small-6 medium-6 large-2 columns","small-6 medium-6 large-2 end columns"]
	
	for type in types:

		roles = soup.find_all("div", {"class": type})

		for role in roles:
			
			png = role.find("img")

			role_id = png["alt"]
			role_id = role_id.replace("Icon ","").replace(" ","").replace(".png","")
			role_id = role_id.lower()

			png = "https://wiki.bloodontheclocktower.com/" + png["src"]
			
			data.append([role_id,png])

	dff = pd.DataFrame(data, columns=["role", "image"])
	dfl.append(dff)
	df = pd.concat(dfl).to_csv("./assets/images/images.csv")

	print("Images Ready")

png2("https://wiki.bloodontheclocktower.com/Travellers")
png2("https://wiki.bloodontheclocktower.com/Fabled")