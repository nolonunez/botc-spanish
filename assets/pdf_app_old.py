from fpdf import FPDF
class FPDF(FPDF):
    def footer(self):
        self.set_y(-10)
        self.set_font('helvetica', '', 6)
        self.cell(40,10, '© Steven Medway, bloodontheclocktower.com; unofficial translation by @nolonunez', 0, 0, 'L')

from fpdf.fonts import FontFace
import csv

def pdf_script(name,author,roles,lang):
    
    print('\nGenerando archivo .pdf\n')
    import assets.special_df.amy_order
    amys = assets.special_df.amy_order.amy
    lang_pack = "./assets/"+lang+"/database.csv"

    #pip install fpdf2

    roles_amyd = []

    for amy in amys:
        if amy in roles:
            roles_amyd.append(amy)

    teams = ['townsfolk','outsider','minion','demon']
    townsfolk = []
    outsider = []
    minion = []
    demon = []

    night_one = {}
    night_other = {}

    fabled = []
    travelers = []

    for n in roles_amyd:
        char = []
        with open(lang_pack, encoding="utf-8") as file, open('./assets/images/images.csv', encoding="utf-8") as file_png:
            csv_reader = csv.reader(file)
            csv_image = csv.reader(file_png)

            for row in csv_image:
                if row[1] == n:
                    char.append(row[2])
                
            for row in csv_reader:
                if row[0] == n:
                    char.append(row[1])
                    char.append(row[10])

                    if row[3] == "townsfolk":
                        townsfolk.append(char)
                    elif row[3] == "outsider":
                        outsider.append(char)
                    elif row[3] == "minion":
                        minion.append(char)
                    elif row[3] == "demon":
                        demon.append(char)
                    elif row[3] == "fabled":
                        fabled.append(char)
                    elif row[3] == "traveler":
                        travelers.append(char)
                    
                    if row[4] != '' and row[4] != '0':
                        night_one[n] = int(row[4])
                    if row[6] != '' and row[6] != '0':
                        night_other[n] = int(row[6])

    night_one['duskinfo'] = 0
    night_one['minioninfo'] = 5
    night_one['demoninfo'] = 5
    night_one['dawninfo'] = 999
    night_other['duskinfo'] = 0
    night_other['dawninfo'] = 999

    value_based = {key:value for key, value in sorted(night_one.items(), key=lambda night_one: night_one[1])}
        
    dic_temp = []
    for i in value_based:
        dic_temp.append(i)
        
    night_one = []
    for n in dic_temp:
        char = []
        with open(lang_pack, encoding="utf-8") as file, open('./assets/images/images.csv', encoding="utf-8") as file_png:
            csv_reader = csv.reader(file)
            csv_image = csv.reader(file_png)
                
            if n == 'minioninfo':
                char.append('https://raw.githubusercontent.com/nolonunez/botc-spanish/main/assets/images/pngs/minioninfo.png')

            elif n == 'demoninfo':
                char.append('https://raw.githubusercontent.com/nolonunez/botc-spanish/main/assets/images/pngs/demoninfo.png')
            
            elif n == 'duskinfo':
                char.append('https://raw.githubusercontent.com/nolonunez/botc-spanish/main/assets/images/pngs/dusk.png')
            
            elif n == 'dawninfo':
                char.append('https://raw.githubusercontent.com/nolonunez/botc-spanish/main/assets/images/pngs/dawn.png')

            else:
                for row in csv_image:
                    if row[1] == n:
                        char.append(row[2])
                
            for row in csv_reader:
                if row[0] == n:
                    char.append(row[1])
        night_one.append(char)

    value_based = {key:value for key, value in sorted(night_other.items(), key=lambda night_other: night_other[1])}
        
    dic_temp = []
    for i in value_based:
        dic_temp.append(i)
        
    night_other = []
    for n in dic_temp:
        char = []
        with open(lang_pack, encoding="utf-8") as file, open('./assets/images/images.csv', encoding="utf-8") as file_png:
            csv_reader = csv.reader(file)
            csv_image = csv.reader(file_png)
                
            if n == 'duskinfo':
                char.append('https://raw.githubusercontent.com/nolonunez/botc-spanish/main/assets/images/pngs/dusk.png')
            
            elif n == 'dawninfo':
                char.append('https://raw.githubusercontent.com/nolonunez/botc-spanish/main/assets/images/pngs/dawn.png')

            else:
                for row in csv_image:
                    if row[1] == n:
                        char.append(row[2])
                
            for row in csv_reader:
                if row[0] == n:
                    char.append(row[1])
        night_other.append(char)

    teams_list = [townsfolk,outsider,minion,demon]
    
    total = len(townsfolk) + len(outsider) + len(minion) + len(demon)

    if total > 22:
        pdf = FPDF('P','mm','Legal')
    elif total > 12 and len(fabled) > 0:
        pdf = FPDF('P','mm','Legal')
    else:
        pdf = FPDF('P','mm','Letter')
    
    total = total + len(fabled)

    #pdf = FPDF('P','mm','Legal')    
    pdf.set_left_margin(13)
    pdf.set_top_margin(3)
    pdf.set_auto_page_break(3)
    pdf.set_right_margin(5)
    pdf.add_page()
    pdf.set_font('helvetica', 'I', 10)

    name_length = 60 - len(fabled)
    col_fb = [name_length]
    for i in fabled:
        col_fb.append(3.5)
        col_fb.append(len(i[1])*0.6)

    if name != "":
        with pdf.table(borders_layout='NONE',col_widths=(col_fb),text_align='LEFT',first_row_as_headings=False) as table:
            row = table.row()
            row.cell(name,style=FontFace(emphasis='ITALICS',size_pt=15))
            row = table.row()
            if author != '':
                row.cell('hecho por '+ author,style=FontFace(size_pt=8))
            #if len(fabled) > 0:
            #    for data in fabled:
            #            row.cell(img=data[0],img_fill_width=True)
            #            row.cell(data[1],style=FontFace(size_pt=8))
            #            print(data[1] +' listo.')

    pdf.set_font('helvetica', '', 8)

    i = 0
    for m in teams_list:
        if m:
            pdf.image('./assets/'+lang+'/pdf_assets/'+ teams[i] +'.png',w=pdf.epw)
            with pdf.table(borders_layout='NONE',line_height=4,col_widths=(3.5,8.5,54),text_align='LEFT',first_row_as_headings=False) as table:
                for n in m:
                    row = table.row()
                    j = 0
                    for datum in n:
                        if j == 0:
                            row.cell(img=datum,img_fill_width=True)
                        elif j == 1:
                            row.cell(datum,style=FontFace(emphasis='BOLD'))
                        else:
                            row.cell(datum)
                            print(n[1] + ' listo.')
                        
                        j = j + 1
        i = i + 1
    
    pdf.set_y(-10)
    pdf.set_font('helvetica', 'B', 8)
    pdf.cell(190,10,'*No la Primera Noche',0,0,'R')

    pdf.set_top_margin(8)
    pdf.add_page()
    pdf.set_font('helvetica', '', 10)
    
    with pdf.table(borders_layout='NONE',line_height=4,col_widths=(22,22,22),text_align='LEFT',first_row_as_headings=False) as table:
        row = table.row()
        row.cell('Primera Noche',align='L')
        row.cell('',align='C')
        row.cell('Otras Noches',align='R')
        row = table.row()
        row.cell('')
        row.cell('')
        row.cell('')
    
    n1 = len(night_one)
    n2 = len(night_other)
    max_n = max(n1,n2)
    
    pdf.set_font('helvetica', '', 8)

    with pdf.table(borders_layout='NONE',line_height=4,col_widths=(3.5,8.5,42,8.5,3.5),text_align='LEFT',first_row_as_headings=False) as table:
        x = 0
        while x < max_n:
            row = table.row()
            
            if x < n1:
                row.cell(img=night_one[x][0],img_fill_width=True)
                row.cell(night_one[x][1],style=FontFace(emphasis='BOLD'))
            else:
                row.cell('')
                row.cell('')

            row.cell('')

            if x < n2:
                row.cell(night_other[x][1],style=FontFace(emphasis='BOLD'),align='R')
                row.cell(img=night_other[x][0],img_fill_width=True)
            else:
                row.cell('')
                row.cell('')
            x = x + 1
            
                  
    from assets.base_scripts import tb,snv,bmr
    if roles == tb or roles == snv or roles == bmr:
        path = lang + "/base_three/"
    
    elif len(townsfolk) + len(outsider) + len(minion) + len(demon) > 12:
        path = lang + "/custom/"
    else:
        path = lang + "/teensy/"

    pdf.output('./botc_scripts/' + path + name.replace(" ","_") + '.pdf')
    print("\nSe agregaron " + str(total) + " de " + str(len(roles)) + " roles en total.")
    print("La distribución es " + str(len(townsfolk)) + "/" + str(len(outsider)) + "/" + str(len(minion)) + "/" + str(len(demon)) + ".")
    print(name + '.pdf está listo.')