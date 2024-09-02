from PIL import Image
import csv
import requests

with open("./assets/images/images.csv") as f:
    file = csv.reader(f)

    x = 0
    for rows in file:
        if x != 0:
            name = rows[1]
            
            img = Image.open(requests.get(rows[2], stream = True).raw)

            img.save("./assets/images/pngs/"+name+".png")
            print(name + " saved.")
        x = x + 1