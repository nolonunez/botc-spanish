import pandas as pd, numpy as np, json
#from assets.pdf_app import pdf_script

def script(name,author,logo,background,roles,pdf,lang):

    print('Generando archivo .json\n')
    lang_pack = './assets/lang/' + lang + '/database.csv'
    lang_pack_jinx = './assets/lang/' + lang + '/jinxes.csv'

    df = pd.read_csv(lang_pack)

    # Construction of the credentials within the script: name, logo and author.
    credentials = {
    'id':'_meta',
    'name': name,
    }

    if logo != '':
        credentials['logo'] = logo

    if author != '':
        credentials['author'] = author

    # Inner join of only the selected roles within all the database.
    roles_df = pd.DataFrame({'id':roles})
    script_df = pd.merge(df,roles_df,how='inner')

    # Import special abilities if necessary.
    fs = open('./assets/special_df/special.json')
    special_json = json.load(fs)

    special_df = pd.DataFrame()
    for i in special_json:
        new_row = pd.DataFrame({'id':i,'special':[special_json[i]]})
        special_df = pd.concat([special_df,new_row], ignore_index=True)

    script_df = pd.merge(script_df,special_df,how='left')

    # Import jinxs rules if necessary.
    jinx_df = pd.read_csv(lang_pack_jinx)
    jinx_sp = pd.merge(script_df,jinx_df,how='inner')[['id','jinx_id','reason']]
    
    jinx_ndf = pd.DataFrame()

    for index,row in jinx_sp.iterrows():
        rol_id = jinx_sp.at[index,'id']
        rol_jx = jinx_sp.at[index,'jinx_id']
        reason = jinx_sp.at[index,'reason']
        
        if script_df.isin([rol_jx]).any().any():
            jinx = {}

            jinx['id'] = rol_jx + '_ts'
            jinx['reason'] = reason

            new_row = pd.DataFrame({'id':rol_id,'jinxes':[jinx]})
            jinx_ndf = pd.concat([jinx_ndf,new_row], ignore_index=True)

    jinx_ndf = jinx_ndf.groupby('id')['jinxes'].apply(list).reset_index()
    script_df = pd.merge(script_df,jinx_ndf,how='left')

    # Background base.
    bg_link = 'https://botc.app/assets/background'

    if background != '':
        credentials['background'] = background

    # Change the background according to the edition.
    elif (script_df['edition'] == 'tb').all() == True:
        credentials['background'] = bg_link + '5-B3ODOfpI.webp'
        credentials['name'] = 'Trouble Brewing'
    elif (script_df['edition'] == 'bmr').all() == True:
        credentials['background'] = bg_link + '5-BcRG2zhb.webp'
        credentials['name'] = 'Bad Moon Rising'
    elif (script_df['edition'] == 'snv').all() == True:
        credentials['background'] = bg_link + '5-CWiuwbQc.webp'
        credentials['name'] = 'Sects and Violets'
    else:
        credentials['background'] = bg_link + '1-C0iW8pNy.webp'
    
    # This puts them in AMY order.    
    amy_df = pd.read_csv('./assets/special_df/amy_order.csv')
    script_df = pd.merge(script_df,amy_df,how='inner').sort_values('amy')
    script_df = script_df.reset_index(drop=True).iloc[:,0:-1]

    # Add images to the roles.
    img_df = pd.read_csv('./assets/images/images.csv')
    img_df = img_df.rename(columns={'roles':'id'})
    img_df = pd.merge(script_df,img_df,how='left')[['id','image','team']]

    for index,row in img_df.iterrows():
        test = img_df.at[index,'id']
        test_team = img_df.at[index,'team']

        other_team = ',https://raw.githubusercontent.com/nolonunez/botc-spanish/main/assets/images/pngs/otherteam/'

        if test_team != 'fabled' and test_team != 'traveler':
            img = img_df.at[index,'image'] + other_team + test + '.png'
            img = img.split(',')

            img_df.at[index,'image'] = img

        elif test_team == 'traveler':
            img = img_df.at[index,'image'] + other_team + test + '1.png'
            img = img + other_team + test + '2.png'
            img = img.split(',')

            img_df.at[index,'image'] = img

    script_df = pd.merge(script_df,img_df,how='inner')

    # Role count.
    count = script_df.groupby(['team']).count()['id'].reset_index()
    count = count.rename(columns={'id':'count'})

    teams = {'townsfolk':0,'outsider':0,'minion':0,'demon':0,'traveler':0,'fabled':0}
    for index,row in count.iterrows():
        teams[row['team']] = count.at[index,'count']

    base_total = teams['townsfolk'] + teams['outsider'] + teams['minion'] + teams['demon']
    total = base_total + teams['traveler'] + teams['fabled']

    # Corrections for .json file
    script_df['id'] = script_df['id'].astype(str) + '_ts'
    script_df['edition'] = script_df['edition'].fillna('exp')
    script_df['firstNight'] = script_df['firstNight'].fillna(0)
    #script_df['firstNight'] = script_df['firstNight'].astype(int) # Must be int for the Official App
    script_df['otherNight'] = script_df['otherNight'].fillna(0)
    #script_df['otherNight'] = script_df['otherNight'].astype(int) # Must be int for the Official App
    #script_df['setup'] = script_df['setup'].fillna(False)
    script_df = script_df.fillna('')

    for index,row in script_df.iterrows():
        if script_df.at[index,'reminders'] != '':
            rem = script_df.at[index,'reminders'].split(',')
            script_df.at[index,'reminders'] = rem
        if script_df.at[index,'remindersGlobal'] != '':
            rem = script_df.at[index,'remindersGlobal'].split(',')
            script_df.at[index,'remindersGlobal'] = rem

    # Path to store the new scripts.
    if (script_df['edition'] == 'tb').all() == True or (script_df['edition'] == 'bmr').all() == True or (script_df['edition'] == 'snv').all() == True:
        path = lang + '/base_three/'
    elif base_total > 12:
        path = lang + '/custom/'
    else:
        path = lang + '/teensy/'

    # DataFrame complete, now comes the .json file.
    json_file = [credentials]

    for index,row in script_df.iterrows():
        json_role = {}
        for i in script_df.columns:
            if script_df.at[index,i] != '':
                if type(script_df.at[index,i]) == np.float64:
                    json_role[i] = int(script_df.at[index,i])
                else:
                    json_role[i] = script_df.at[index,i]
        json_file.append(json_role)

    with open("./botc_scripts/" + path + name.replace(" ","_") + ".json", "w+") as f:
        json.dump(json_file, f, indent = 2)  
    f.close()

    print("\nSe agregaron " + str(total) + " de " + str(len(roles)) + " roles en total.")
    print("La distribución es " + str(teams['townsfolk']) + "/" + str(teams['outsider']) + "/" + str(teams['minion']) + "/" + str(teams['demon']) + ".")
    print( name + ".json está listo.")

    #if pdf == "Y":
    #    pdf_script(name,author,roles,lang)

def source_json(file,name,author,logo,background,pdf,lang):

    # Make the list for the roles based on the .json file.
    source_df = pd.read_json(file)
    if source_df.isin(['_meta']).any().any():
        source_df = source_df.drop(index=0)
    
    source_df = source_df.reset_index()['id']
    roles = []

    for i in source_df:
        roles.append(i.replace('_ts','').replace('-',''))

    # Extract the author information.
    info_og = {'name':name,'author':author,'logo':logo,'background':background}
    info_new = {'name':'','author':'','logo':'','background':''}

    f = open(file)
    data = json.load(f)
    
    id_script = data[0]
    if 'id' in id_script and id_script['id'] == '_meta':
        for n in info_new.keys():
            print(n)
            if n in id_script and id_script[n] != '':
                print('si tiene nombre')
                info_new[n] = id_script[n]
    f.close()
    
    print(info_new)

    for n in info_og.keys():
        if n != '':
            info_new[n] = info_og[n]
            
    script(name,author,logo,background,roles,pdf,lang)

import os, glob

def update_all(lang,pdf):
    path = './botc_scripts/' + lang
    folders = ['/base_three', '/custom', '/teensy']

    for folder in folders:
        for file in glob.glob(os.path.join(path + folder, '*.json')):
            
            print('\nActualizando ' + file.replace(path+folder,'')[1:] + '.')
            
            source_json(file,pdf,lang,name='',author='',logo='',background='')                

            print(file.replace(path+folder,'')[1:] + ' actualizado.')
    print('\nTodos los archivos están actualizados a la versión más reciente.')