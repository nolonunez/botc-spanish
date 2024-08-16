import json
from assets.json_app import script
from assets.base_scripts import tb,snv,bmr

def source_json(pdf):
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

    if type(data[1]) == str:
        for role in data[1:]:
            roles.append(role)
    else:
        for role_dic in data[1:]:
            if '_es' in role_dic['id']:
                roles.append(role_dic['id'].replace("_es",""))
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

    script(name,author,logo,background,roles,pdf)

