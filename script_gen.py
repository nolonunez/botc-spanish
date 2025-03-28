from assets.json_app import script, source_json

lang = "es_MX"

name = ''
author = ''
logo = ''
background = ''

#'Y' or 'N'
pdf = 'N'

roles = [
]

file = './source.json'

# Use 'source_json' if you want to translate the source.json, otherwise use 'script'.
#script(name,author,logo,background,roles,pdf,lang)
source_json(file,name,author,logo,background,pdf,lang)