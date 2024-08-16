import json
from assets.json_app import script
from assets.base_scripts import tb,snv,bmr

def source_json(name,author,pdf):

    name_og = name
    author_og = author

    f = open('./source.json')
    data = json.load(f)

    id_script = data[0]

    name = ''
    author = ''
    logo = ''
    background = ''
    
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
        author = 'Nolo (trad.)'
    if roles == snv:
        name = 'De Lirios y Sectas'
        author = 'Nolo (trad.)'
    if roles == bmr:
        name = 'Luna de Sangre'
        author = 'Nolo (trad.)'
    
    if name == "" and name_og == "":
        name = "no_name"
    if name_og != "":
        name = name_og

    if author_og != "":
        author = author_og

    script(name,author,logo,background,roles,pdf)

