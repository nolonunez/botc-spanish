from fpdf import FPDF
import csv

def pdf_script(roles):
    
    print("\n"+"Generando archivo .pdf, esto suele tardar más.\n")
    import assets.amy
    amys = assets.amy.amy

    #pip install fpdf2

    #layout ('P','L')
    #unit ('mm','cm','in')
    #format ('A3','A4','A5','Letter','Legal',(100,150))
    #'B', 'U', 'I', '' (regular)
    #w = width, h = height

    pdf = FPDF('P','mm','Letter')
    pdf.set_margin(15)
    pdf.add_page()

    roles_amyd = []

    for amy in amys:
        if amy in roles:
            roles_amyd.append(amy)

    teams = ['townsfolk','outsider','minion','demon']
    script = []
    t = 0
    o = 0
    m = 0
    d = 0

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
                    char.append(row[3])

                    if row[3] == "townsfolk":
                        t = t + 1
                    elif row[3] == "outsider":
                        o = o + 1
                    elif row[3] == "minion":
                        m = m + 1
                    elif row[3] == "demon":
                        d = d + 1 
            
            script.append(char)
    
    i = 0
    for n in script:
        if i == 0:
            pdf.image('./assets/pdf_assets/'+ teams[0] +'.png',w=pdf.epw)
        if i == t:
            pdf.image('./assets/pdf_assets/'+ teams[1] +'.png',w=pdf.epw)
        if i == t + o:
            pdf.image('./assets/pdf_assets/'+ teams[2] +'.png',w=pdf.epw)    
        if i == t + o + m:
            pdf.image('./assets/pdf_assets/'+ teams[3] +'.png',w=pdf.epw)
        
        pdf.image(n[0],w=10,h=10)
       
        pdf.set_font('helvetica', 'B', 8)
        pdf.cell(24,10,n[1])

        pdf.set_font('helvetica', '', 8)
        pdf.cell(0,10,n[2],0,1,'L')

        print(n[1] + ' listo.')
        
        i = i + 1

    pdf.output('./botc_scripts/pdf_1.pdf')
    print('\n' + '.pdf listo')