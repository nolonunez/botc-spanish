import os, glob, json
from assets.json_source import source_json

def update_all(lang,pdf):
    path = './botc_scripts/' + lang
    folders = ['/base_three', '/custom', '/teensy']

    for folder in folders:
        for file in glob.glob(os.path.join(path + folder, '*.json')):
            with open(os.path.join(os.getcwd(), file), 'r') as f:
                data = json.load(f)
                id_script = data[0]

                if 'name' in id_script and id_script['name'] != "":
                    name_id = id_script['name']
                
                print('\nActualizando ' + name_id + '.')
                
                source_json(file,name='',author='',pdf=pdf,lang=lang)
                
                print(name_id + ' actualizado.')
    print('\nTodos los archivos están actualizados a la versión más reciente.')