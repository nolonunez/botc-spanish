from fpdf import FPDF
from fpdf.fonts import FontFace
import csv

def pdf_script(name,author,roles):
    
    print('\nGenerando archivo .pdf\n')
    import assets.amy
    amys = assets.amy.amy

    #pip install fpdf2

    pdf = FPDF('P','mm','Letter')
    pdf.set_left_margin(13)
    pdf.set_top_margin(3)
    pdf.set_auto_page_break(3)
    pdf.set_right_margin(5)
    pdf.add_page()
    
    pdf.set_font('helvetica', 'I', 10)
    if author == '':
        pdf.cell(0,5,name,0,1, align = 'C')
    else:
        pdf.cell(0,5,name + ' por ' + author,0,1, align = 'C')
    pdf.set_font('helvetica', '', 8)

    roles_amyd = []

    for amy in amys:
        if amy in roles:
            roles_amyd.append(amy)

    teams = ['townsfolk','outsider','minion','demon']
    townsfolk = []
    outsider = []
    minion = []
    demon = []

    for n in roles_amyd:
        char = []
        with open('./assets/es_MX.csv') as file, open('./assets/images.csv') as file_png:
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

    teams_list = [townsfolk,outsider,minion,demon]

    i = 0
    for m in teams_list:
        pdf.image('./assets/pdf_assets/'+ teams[i] +'.png',w=pdf.epw)
        with pdf.table(borders_layout='NONE',line_height=4,col_widths=(3.5,8.5,60),text_align='LEFT',first_row_as_headings=False) as table:
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

    total = len(townsfolk) + len(outsider) + len(minion) + len(demon)

    from assets.base_scripts import tb,snv,bmr
    if roles == tb or roles == snv or roles == bmr:
        path = "base_three/"
    
    elif len(roles) > 12:
        path = "custom/"
    else:
        path = "teensy/"

    pdf.output('./botc_scripts/' + path + name.replace(" ","_") + '.pdf')
    print("\nSe agregaron " + str(total) + " de " + str(len(roles)) + " roles en total.")
    print("La distribución es " + str(len(townsfolk)) + "/" + str(len(outsider)) + "/" + str(len(minion)) + "/" + str(len(demon)) + ".")
    print(name + '.pdf está listo.')