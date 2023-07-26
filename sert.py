import pymorphy2
from operator import ne
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
from petrovich.main import Petrovich
from petrovich.enums import Case, Gender
import re


p = Petrovich()

# morph = pymorphy2.MorphAnalyzer() 
list_com = pd.read_excel(r'list of comands.xlsx')


for data in list_com.itertuples(index=False, name='People'):
    com = data.Команда
    new_fio = data.ФИ.split()
    # name = morph.parse(new_fio[1])[0]
    # surname = morph.parse(new_fio[0])[0]
    # new_name = name.inflect({'datv'}).word
    # new_surname = surname.inflect({'datv'}).word
    name = new_fio[1]
    surname = new_fio[0]
    cased_lname = p.lastname(name, Case.GENITIVE)
    if data.Дательный == "":
        if data.Пол == 'м':
            new_name = p.firstname(name, Case.DATIVE, Gender.MALE)
            new_surname = p.lastname(surname, Case.DATIVE, Gender.MALE)
        else:
            new_name = p.firstname(name, Case.DATIVE, Gender.FEMALE)
            new_surname = p.lastname(surname, Case.DATIVE, Gender.FEMALE)
        new_fio = new_surname+ ' '+ new_name
    else:
        new_name = name
        new_surname = surname


    image = Image.open("template_s.png")
    image = image.convert('RGBA')
    drawer = ImageDraw.Draw(image)

    text = 'выдан'
    coor = (828, 865)
    font = font_for_head = ImageFont.truetype("times.ttf", 60)
    drawer.multiline_text(coor, text, font = font, align = "center", anchor="ms", spacing=10, fill='black')

    text= 'команда юных геологов \"{}\"'.format(com)
    coor = (828, 1180-2)
    font = font_for_head = ImageFont.truetype("times.ttf", 60)
    drawer.multiline_text(coor, text, font = font, align = "center", anchor="ms", spacing=10, fill='black')

    school = re.split('[,(\\\\n)]+', str(data.Школа))
    print (school)
    if '' in school:
        school.remove('')
    if 'a' in school:
        school.remove('a')
    text = ''
    for i in school:
        text += i + '\n'
    print (text)
    coor = (828, 1280-10)
    font = font_for_head = ImageFont.truetype("times.ttf", 50)
    if len(text) > 0:
        drawer.multiline_text(coor, text, font = font, align = "center", anchor="ms", spacing=10, fill='black')

    text= 'в том, что он(а) принимал(а) участие\n\
в IX Республиканской открытой полевой\n\
олимпиаде юных геологов\n\
с 24.04.2023 г. по 29.04.2023 г.'
    coor = (828, 1555)
    font = font_for_head = ImageFont.truetype("times.ttf", 40)
    drawer.multiline_text(coor, text, font = font, align = "center", anchor="ms", spacing=10, fill='black')

    text= new_fio
    coor = (828, 1050)
    font = font_for_head = ImageFont.truetype("times.ttf", 90)
    drawer.multiline_text(coor, text, font = font, align = "center", anchor="ms", spacing=10, fill='black')
    name_file = 'ser\\' + com + ' ' + new_fio + '.png'
    image.save(name_file)
    


