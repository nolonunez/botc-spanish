data = ""
def utf(csvfile):
    with open("./assets/es_MX/"+csvfile+".csv",encoding="UTF-8") as file:
        data = file.read().replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ñ","n").replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U").replace("ü","u").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("Ü","U")

    with open("./assets/es_MX/"+csvfile+"_bug.csv","w+",encoding="UTF-8") as file:
        file.write(data)

    print(csvfile + " ready")

utf("es_MX")
utf("jinxes")