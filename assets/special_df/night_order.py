import pandas as pd

df = pd.read_csv('./assets/es_MX/database.csv')

char = df.loc[(df['firstNight']>0)|(df['otherNight']>0)]['id'][5:-1]
char = char.reset_index(drop=True)

char.loc[-1] = {"id":"_meta","author":"","name":""}
char.index = char.index + 1
char.sort_index(inplace=True) 

char.to_json('./assets/night_order.json', orient='values')
print(char)
