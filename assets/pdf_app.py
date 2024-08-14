from fpdf import FPDF

import csv

#al momento de def la funcion, import assets.amy
import amy
amys = amy.amy

#pip install fpdf2

#layout ('P','L')
#unit ('mm','cm','in')
#format ('A3','A4','A5','Letter','Legal',(100,150))

pdf = FPDF('P','mm','Letter')

#add a page
pdf.add_page()

#'B', 'U', 'I', '' (regular)

#add text
#w = width, h = height

roles = ["atheist", "balloonist"]

for amy in amys:
    if amy in roles:        
        with open('./assets/es_MX.csv') as file, open('./assets/images.csv') as img_file:
            csv_reader = csv.reader(file)
            csv_image = csv.reader(file)

            for row in csv_reader:
                try:
                    if row[0] == amy:
                        pdf.cell(21,11, link=pdf.image('https://wiki.bloodontheclocktower.com//images/c/cb/Icon_balloonist.png',10,11,10))
                        
                        pdf.set_font('helvetica', 'B', 9)
                        pdf.cell(21,11,row[1])

                        pdf.set_font('helvetica', '', 9)
                        pdf.cell(0,11,row[10], ln=1)
                except:
                    continue


pdf.output('./botc_scripts/pdf_1.pdf')