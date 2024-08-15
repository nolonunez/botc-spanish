from assets.json_app import script
from assets.pdf_app import pdf_script
from assets.base_scripts import tb,snv,bmr

name = "test"
author = "test"
logo = ""
background = ""
pdf = "Y"

roles = [
    'washerwoman',
    'drunk',
    'scarletwoman',
    'pukka'
]

script(name,author,logo,background,roles)
if pdf == "Y":
    pdf_script(roles)