import json
import csv

def script(name,author,logo,background,roles):

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

    for amy in amys:

        if amy in roles:
            
            #dictionary that stores one role
            roles_dic = {}

            obj_list = ["id","name","edition","team","firstNight","firstNightReminder","otherNight","otherNightReminder","reminders","remindersGlobal","ability","setup","special","jinxes"]

            x = 0
            while x < 13:
                with open('./assets/es_MX.csv') as file:
                    csv_reader = csv.reader(file)

                    for row in csv_reader:
                        try:
                            if row[0] == amy:
                                
                                obj_name = obj_list[x]
                                
                                #if not in the base three, they're experimental
                                if x == 2 and row[x] == "":
                                    roles_dic[obj_name] = "experimental"
                                
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
                                  
                                #special abilities
                                elif x == 12:

                                    char = row[0]
                                                                                                          
                                    fs = open('./assets/special.json')
                                    special_data = json.load(fs)

                                    for i in special_data:
                                        if i == char:
                                            roles_dic["special"] = special_data[char]

                                    fs.close()
                                
                                else:
                                    roles_dic[obj_name] = row[x]
                                
                        except:
                            continue
                x = x + 1

            #this doesn't include the alignment changed images, as I can't find them in the internet
            with open('./assets/images.csv') as file:
                    csv_reader2 = csv.reader(file)
                    for row in csv_reader2:
                        try:
                            if row[1] == amy:

                                roles_dic["image"] = row[2]
                        except:
                            continue

            roles_dic["id"] = amy + '_es'
            
            script.append(roles_dic)

    #path to folder depending on the script
    from assets.base_scripts import tb,snv,bmr
    path = ""

    if roles == tb or roles == snv or roles == bmr:
        path = "base_three/"
    
    elif len(roles) > 12:
        path = "custom/"
    else:
        path = "teensy/"

    with open("./botc_scripts/" + path + name.replace(" ","_") + ".json", "w+") as f:
        json.dump(script, f)  
    f.close()

    print( name + " está listo.")