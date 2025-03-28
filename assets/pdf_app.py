import pandas as pd
from fpdf import FPDF
from fpdf.fonts import FontFace

class FPDF(FPDF):
    def footer(self):
        self.set_y(-10)
        self.set_font('helvetica', '', 6)
        self.cell(40,10, '© Steven Medway, bloodontheclocktower.com; unofficial translation by @nolonunez', 0, 0, 'L')

# This requires pip install fpdf2
def pdf_script(name,author,script_df,lang,base_total):
    
    print('\nGenerando archivo '+ name + '.pdf\n')
    script_df = pd.DataFrame(script_df)

    # Organization of roles by team.
    teams = ['townsfolk','outsider','minion','demon','traveler','fabled']

    def org(main_df,team):
        req_col = ['name','ability','image']
        main_df = pd.DataFrame(script_df)

        dataframe = main_df[(main_df['team']==team)][req_col]

        list_t = []
        for index,row in dataframe.iterrows():
            ind_t = []
            for n in list(dataframe.columns):
                ind_t.append(dataframe.at[index,n])
            list_t.append(ind_t)
        return list_t
    
    teams_comp = []

    for n in teams:
        teams_comp.append(org(script_df,team=n))

    # PDF parameters.
    #if base_total > 22:
    #    pdf = FPDF('P','mm','Legal')
    #elif base_total > 12 and fabled.empty == False:
    #    pdf = FPDF('P','mm','Legal')
    #else:
    #    pdf = FPDF('P','mm','Letter')

    pdf = FPDF('P','mm','Letter')

    pdf.set_left_margin(13)
    pdf.set_top_margin(3)
    pdf.set_auto_page_break(3)
    pdf.set_right_margin(5)
    pdf.add_page()
    pdf.set_font('helvetica', 'I', 10)

    ## Fable work in progress
    #if fabled.empty:
    #    name_length = 60
    #else:
    #    fab_c = script_df.groupby(['team']).count()['id'].reset_index()
    #    f_c = fab_c.loc[(fab_c['team']=='fabled')].reset_index()
    #    name_length = 60 - int(f_c.at[0,'id'])

    # Title
    name_length = 60
    if name != "":
        with pdf.table(borders_layout='NONE',col_widths=(name_length),text_align='LEFT',first_row_as_headings=False) as table:
            row = table.row()
            row.cell(name,style=FontFace(emphasis='ITALICS',size_pt=15))
            row = table.row()
            if author != '':
                row.cell(author,style=FontFace(size_pt=8))

    pdf.set_font('helvetica', '', 8)

    # First page just print first four teams.
    teams_p1 = teams_comp[0:4]
    n = 0
    while n < 4:
        if teams_p1[n]:
            pdf.image('./assets/lang/'+lang+'/pdf_assets/'+ teams[n] +'.png',w=pdf.epw)
            with pdf.table(borders_layout='NONE',line_height=4,col_widths=(3.5,8.5,54),text_align='LEFT',first_row_as_headings=False) as table:
                for character in teams_p1[n]:
                    row = table.row()
                    
                    row.cell(img=character[2][0],img_fill_width=True)
                    row.cell(character[0],style=FontFace(emphasis='BOLD'))
                    row.cell(character[1])

                    print(str(character[0])+' en documento.')
        n+=1

    night_col = ['name','firstNight','otherNight','ability']
    ndf = pd.read_csv('./assets/lang/' + lang + '/database.csv')[night_col]
    ndf = ndf.head(5)

    pdf.set_y(-10)
    pdf.set_font('helvetica', 'B', 8)
    pdf.cell(190,10,ndf.at[0,'name'],0,0,'R')

    # Night Order
    #night_one = script_df.loc[(script_df['firstNight']>0)].sort_values(['firstNight'], ascending=True)[['name','team','ability','image']]
    #night_one = night_one.reset_index(drop=True)

    pdf.output(name.replace(" ","_") + '.pdf')