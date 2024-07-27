import json
import csv

def script(name,author,logo,background,roles):

    credentials = {
    "id":"_meta",
    "name": name,
    }  

    #list for exporting json in amy order
    import amy
    amys = amy.amy

    if logo != "":
        credentials["logo"] = logo

    if author != "":
        credentials["author"] = author
    
    if background != "":
        credentials["background"] = background

    script = [credentials]

    for amy in amys:

        if amy in roles:
            
            #dictionary that stores one role
            roles_dic = {}

            obj_list = ["id","name","edition","team","firstNight","firstNightReminder","otherNight","otherNightReminder","reminders","remindersGlobal","ability","setup","special","jinxes"]

            x = 0
            while x < 12:
                with open('es_MX.csv') as file:
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

                                elif x == 11:
                                    if row[x] != "":
                                        roles_dic["setup"] = True
                                    else:
                                        roles_dic["setup"] = False    
                                
                                else:
                                    roles_dic[obj_name] = row[x]
                                
                                if x == 12 or x == 13:
                                    roles_dic[obj_name] = ""
                                
                        except:
                            continue
                x = x + 1

            #this doesn't include the alignment changed images, as i can't find them in the internet
            with open('images.csv') as file:
                    csv_reader2 = csv.reader(file)
                    for row in csv_reader2:
                        try:
                            if row[1] == amy:

                                roles_dic["image"] = row[2]
                        except:
                            continue

            roles_dic["id"] = amy + '_es'
            
            script.append(roles_dic)

    with open("./botc_scripts/" + name.replace(" ","_") + ".json", "w+") as f:
        json.dump(script, f)  
    f.close()

    #save_file = open(name.replace(" ","_") + ".json", "w")  
    #json.dump(script, save_file)  
    #save_file.close() 

    print( name + " está listo.")