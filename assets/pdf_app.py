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

    script = ['townsfolk','outsider','minion','demon']
    
    for team in script:
        pdf.image('./assets/pdf_assets/'+ team +'.png',w=pdf.epw)
        for n in roles_amyd:
            with open('./assets/es_MX.csv') as file:
                csv_reader = csv.reader(file)

                for row in csv_reader:
                    try:
                        if row[0] == n and row[3] == team:
                                
                            pdf.set_font('helvetica', 'B', 8)
                            pdf.cell(24,10,row[1],1)

                            pdf.set_font('helvetica', '', 8)
                            pdf.cell(0,10,row[10],0,1,'L')
                    except:
                        continue

    pdf.output('./botc_scripts/pdf_1.pdf')
    print('\n' + '.pdf listo')