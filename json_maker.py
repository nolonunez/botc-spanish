import json
import csv

def script_make(name,author,logo,roles):

    credentials = {
    "id":"_meta",
    "name":name,
    "author":author,
    }  

    #list for exporting json in amy order
    import amy
    amys = amy.amy

    if logo != "":
        credentials["logo"] = logo

    script = [credentials]

    for amy in amys:

        if amy in roles:

            roles_dic = {}

            obj_list = ['id','name','ability','edition','firstNight','firstNightReminder','otherNight','otherNightReminder','reminders','remindersGlobal','setup','team']

            x = 0
            while x < 12:
                with open('es_MX.csv') as file:
                    csv_reader = csv.reader(file)
                    for row in csv_reader:
                        try:
                            if row[0] == amy:
                                
                                obj_name = obj_list[x]
                                
                                if row[x] != '':
                                    roles_dic[obj_name] = row[x]
                        except:
                            continue
                x = x + 1

            roles_dic['id'] = amy + '_es'
            roles_dic['image'] = "https://raw.githubusercontent.com/bra1n/townsquare/main/src/assets/icons/" + amy + ".png"

            script.append(roles_dic)


    save_file = open(name.replace(" ","_") + ".json", "w")  
    json.dump(script, save_file)  
    save_file.close() 