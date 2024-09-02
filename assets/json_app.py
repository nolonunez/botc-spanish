import json
import csv
from assets.pdf_app import pdf_script

def script(name,author,logo,background,roles,pdf,lang):

    print('Generando archivo .json\n')
    lang_pack = "./assets/"+lang+"/database_bug.csv"
    lang_pack_jinx = "./assets/"+lang+"/jinxes_bug.csv"

    credentials = {
    "id":"_meta",
    "name": name,
    }  

    #list for exporting json in amy order
    import assets.amy
    amys = assets.amy.amy

    if logo != "":
        credentials["logo"] = logo

    if author != "":
        credentials["author"] = author
    
    
    from assets.base_scripts import tb,snv,bmr
    
    if background != "":
        credentials["background"] = background
    elif roles == tb:
        credentials["background"] = 'https://botc.app/assets/background5-B3ODOfpI.webp'
    elif roles == bmr:
        credentials["background"] = 'https://botc.app/assets/background5-BcRG2zhb.webp'
    elif roles == snv:
        credentials["background"] = 'https://botc.app/assets/background5-CWiuwbQc.webp'
    
    else:
        credentials["background"] = 'https://botc.app/assets/background1-C0iW8pNy.webp'

    script = [credentials]
    
    #to count if every role was added
    n = 0
    n2 = len(roles)
    town = []
    outs = []
    minion = []
    demons = []
    travels = []
    fableds = []
    #for characters not in travel or fabled
    norm = []
    #jinxes
    ji = 0

    for amy in amys:

        if amy in roles:
            
            #dictionary that stores one role
            roles_dic = {}

            obj_list = ["id","name","edition","team","firstNight","firstNightReminder","otherNight","otherNightReminder","reminders","remindersGlobal","ability","setup","special","jinxes"]

            x = 0
            while x < 14:
                with open(lang_pack, encoding="utf-8") as file:
                    csv_reader = csv.reader(file)

                    for row in csv_reader:
                        try:
                            if row[0] == amy:
                                
                                obj_name = obj_list[x]
                                
                                #if not in the base three, they're experimental
                                if x == 2 and row[x] == "":
                                    roles_dic[obj_name] = "experimental"
                                
                                elif x == 3:
                                    roles_dic[obj_name] = row[x]
                                    if row[x] == "townsfolk":
                                        town.append(row[0])
                                        norm.append(row[0])
                                    elif row[x] == "outsider":
                                        outs.append(row[0])
                                        norm.append(row[0])
                                    elif row[x] == "minion":
                                        minion.append(row[0])
                                        norm.append(row[0])
                                    elif row[x] == "demon":
                                        demons.append(row[0])
                                        norm.append(row[0])
                                    elif row[x] == "traveler":
                                        travels.append(row[0])
                                    elif row[x] == "fabled":
                                        fableds.append(row[0])
                                
                                #firstNight and otherNight must be int in the official app
                                elif x == 4 or x == 6:
                                    roles_dic[obj_name] = int(row[x])

                                #reminders must be a list within the object
                                elif x == 8 or x == 9:
                                    if row[x] != "":
                                        rem = row[x].split(",")
                                        roles_dic[obj_name] = rem
                                    else:
                                        continue
                                
                                #setup is a boolean
                                elif x == 11:
                                    if row[x] != "":
                                        roles_dic["setup"] = True
                                    else:
                                        roles_dic["setup"] = False

                                    print(roles_dic["name"] + " listo.")
                                    n = n + 1    
                                  
                                #special abilities
                                elif x == 12:

                                    char = row[0]
                                                                                                          
                                    fs = open("./assets/special.json")
                                    special_data = json.load(fs)

                                    for i in special_data:
                                        if i == char:
                                            roles_dic["special"] = special_data[char]

                                    fs.close()
                                
                                elif x == 13:
                                    
                                    char = row[0]
                                    jinx_list = []
                                    with open(lang_pack_jinx, encoding="utf-8") as fj:
                                        jinxes = csv.reader(fj)
                                        for row_jinx in jinxes:
                                            try:
                                                if row_jinx[0]== char:
                                                    jinx_doc = {'id':'','reason':''}

                                                    if row_jinx[1] in roles:
                                                        jinx_doc['id'] = row_jinx[1] + '_es'
                                                        jinx_doc['reason'] = row_jinx[2]
                                                    
                                                        jinx_list.append(jinx_doc)
                                                        ji = ji + 1
                                            except:
                                                continue
                                    if jinx_list:
                                        roles_dic['jinxes'] = jinx_list
                                    fj.close()

                                else:
                                    roles_dic[obj_name] = row[x]
                        except:
                            continue
                x = x + 1
            
            with open('./assets/images/images.csv') as file:
                    csv_reader2 = csv.reader(file)

                    for row in csv_reader2:
                        try:
                            if row[1] == amy:
                                if row[1] in fableds:
                                    roles_dic["image"] = row[2]
                                elif row[1] in norm:

                                    img = row[2]+",https://raw.githubusercontent.com/nolonunez/botc-spanish/main/assets/images/pngs/otherteam/"+row[1]+".png"
                                    img = img.split(",")

                                    roles_dic["image"] = img
                                
                                elif row[1] in travels:
                                    
                                    img = row[2]+",https://raw.githubusercontent.com/nolonunez/botc-spanish/main/assets/images/pngs/otherteam/"+row[1]+"1.png"
                                    img = img+",https://raw.githubusercontent.com/nolonunez/botc-spanish/main/assets/images/pngs/otherteam/"+row[1]+"2.png"
                                    img = img.split(",")

                                    roles_dic["image"] = img 
                        except:
                            continue

            roles_dic["id"] = amy + '_es'
            
            script.append(roles_dic)

    #path to folder depending on the script
    from assets.base_scripts import tb,snv,bmr
    path = ""

    if roles == tb or roles == snv or roles == bmr:
        path = lang + "/base_three/"
    
    elif len(town) + len(outs) + len(minion) + len(demons) > 12:
        path = lang + "/custom/"
    else:
        path = lang + "/teensy/"

    with open("./botc_scripts/" + path + name.replace(" ","_") + ".json", "w+") as f:
        json.dump(script, f)  
    f.close()

    print("\nSe agregaron " + str(n) + " de " + str(n2) + " roles en total.")
    print("La distribución es " + str(len(town)) + "/" + str(len(outs)) + "/" + str(len(minion)) + "/" + str(len(demons)) + ".")
    print("Se añadieron " + str(ji) + " jinxes.")
    print( name + ".json está listo.")

    if pdf == "Y":
        pdf_script(name,author,roles,lang)