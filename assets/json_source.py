import json
from assets.json_app import script
from assets.base_scripts import tb,snv,bmr

def source_json(file,name,author,pdf):

    name_og = name
    author_og = author

    if file != 'all':
        f = open(file)
    else:
        f = file
    data = json.load(f)

    name = ''
    author = ''
    logo = ''
    background = ''

    id_script = data[0]
    if 'id' in id_script and id_script['id'] == '_meta':
        if 'name' in id_script and id_script['name'] != "":
            name = id_script['name']
        if 'author' in id_script and id_script['author'] != "":
            author = id_script['author']
        if 'logo' in id_script and id_script['logo'] != "":
            logo = id_script['logo']
        if 'background' in id_script and id_script['background'] != "":
            background = id_script['background']   
    

    roles = []
    
    if type(data[0]) == str:
        for role in data:
            roles.append(role.replace("_","").replace("-",""))
    elif type(data[0]) != str and type(data[1]) == str:
        for role in data[1:]:
            roles.append(role.replace("_","").replace("-",""))
    else:
        for role_dic in data:
            if role_dic['id'] == '_meta':
                continue    
            elif '_es' in role_dic['id']:
                roles.append(role_dic['id'].replace("_es",""))
            elif '_' in role_dic['id'] or '-' in role_dic['id']:
                roles.append(role_dic['id'].replace("_","").replace("-",""))
            else:
                roles.append(role_dic['id'])

    f.close()

    if roles == tb:
        name = 'Destilando Problemas'
        author = '(Trouble Brewing)'
    if roles == snv:
        name = 'De Lirios y Sectas'
        author = '(Sects and Violets)'
    if roles == bmr:
        name = 'Luna de Sangre'
        author = '(Bad Moon Rising)'
    
    if name == "" and name_og == "":
        name = "no_name"
    if name_og != "":
        name = name_og

    if author_og != "":
        author = author_og

    script(name,author,logo,background,roles,pdf)

