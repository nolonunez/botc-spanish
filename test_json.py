import json

name = "test"
author = "Nolo"
#logo = "https:\/\/www.bloodstar.xyz\/p\/nolo\/Trouble_Brewing_ES_FULL\/_meta.png"

credentials = {
"id":"_meta",
"name":name,
"author":author,
#"logo":logo,
}  

import csv

roles = [
"alchemist",
"amnesiac",
"artist",
"atheist",
"balloonist",
"bountyhunter",
"cannibal",
"chambermaid",
"chef",
"choirboy",
"clockmaker",
"courtier",
]

script = [credentials]

for role in roles:

    roles_dic = {}
    
    obj_list = ['id','name','team','ability','firstNightReminder','otherNightReminder','remindersGlobal','reminders','firstNight','otherNight']

    x = 0
    while x < 10:
        with open('es_MX.csv') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                try:
                    if row[0] == role:
                        
                        obj_name = obj_list[x]
                        
                        if row[x] != '':
                            roles_dic[obj_name] = row[x]
                except:
                    continue
        x = x + 1

    roles_dic['id'] = role + '_es'
    roles_dic['image'] = "https://raw.githubusercontent.com/bra1n/townsquare/main/src/assets/icons/" + role + ".png"

    script.append(roles_dic)


save_file = open("test.json", "w")  
json.dump(script, save_file)  
save_file.close() 