from fpdf import FPDF
import csv

def pdf_script(roles):
    
    print("\n"+"Generando archivo .pdf, esto suele tardar más.")
    import assets.amy
    amys = assets.amy.amy

    #pip install fpdf2

    #layout ('P','L')
    #unit ('mm','cm','in')
    #format ('A3','A4','A5','Letter','Legal',(100,150))
    #'B', 'U', 'I', '' (regular)
    #w = width, h = height

    pdf = FPDF('P','mm','Letter')
    pdf.set_margin(5)
    pdf.add_page()

    roles_amyd = []

    for amy in amys:
        if amy in roles:
            roles_amyd.append(amy)

    town = []
    outsiders = []
    minions = []
    demons = []
    travelers = []
    fabled = []

    for n in roles_amyd:
        with open('./assets/es_MX.csv') as file, open('./assets/images.csv') as img_file:
            csv_reader = csv.reader(file)
            csv_image = csv.reader(img_file)

            for row1 in csv_reader:
                try:
                    if row1[0] == n:

                        if row1[3] == 'townsfolk':
                            town.append(n)
                        elif row1[3] == 'outsider':
                            outsiders.append(n)
                        elif row1[3] == 'minion':
                            minions.append(n)
                        elif row1[3] == 'demon':
                            demons.append(n)
                        elif row1[3] == 'traveler':
                            travelers.append(n)
                        elif row1[3] == 'fabled':
                            fabled.append(n)
                        else:
                            continue
                        
                        for row2 in csv_image:
                            try:
                                if row1[0] == row2[1] and n not in travelers or fabled:
                                    #pdf.image(10,11,row2[2],0,0)    

                                    pdf.set_font('helvetica', 'B', 8)
                                    pdf.cell(48,10,row1[1],0,0,'L')

                                    pdf.set_font('helvetica', '', 8)
                                    pdf.cell(0,10,row1[10],0,1,'L')
                            except:
                                continue
                except:
                    continue

    pdf.output('./botc_scripts/pdf_1.pdf')
    print('\n' + '.pdf listo')