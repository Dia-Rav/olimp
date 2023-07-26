from operator import ne
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

mebers_com = {}
list_com = pd.read_excel('rep.xlsx')
font_text = ImageFont.truetype("arial.ttf", 80)
font_for_head = ImageFont.truetype("arial.ttf", 90)
coor_head = [(340, 500), (1020, 500), (1730, 500), (340, 500), (1050, 500), (1730, 500),(340, 500), (1050, 500), (1730, 500),(340, 500), (1050, 500), (1730, 500)]
coor = [(340, 690), (1020, 690), (1730, 690), (340, 690), (1050, 690), (1730, 690), (340, 690), (1050, 690), (1730, 690),(340, 690), (1050, 690), (1730, 690)]
max_size = 800 - 150
def check_len (text, font):
    text = text.split('\n')
    return  max(list(map(lambda x: font.getlength(x), text)))
i = -1
for data in list_com.itertuples(index=False, name='People'):
    com = data.Команда
    i+=1
    name_file = "repeat{}.png".format(i//3)

    if i % 3 != 0:
        image = Image.open(name_file)
        drawer = ImageDraw.Draw(image)
    elif i %3 == 0: 
        image = Image.open("template.png")
        image = image.convert('RGBA')
        drawer = ImageDraw.Draw(image)

    new_fio = data.ФИО.split()
    if len(new_fio)>2:
        new_fio = str(new_fio[0] + '\n' + new_fio[1] + ' ' + new_fio[2])
    else:    
        new_fio = str(new_fio[0] + ' ' + new_fio[1])
    text_head = "{}\n\"{}\"".format (data.Статус, com)
    text = "{}".format (new_fio)

    if check_len(text, font_text) > max_size:
        new_font = ImageFont.truetype("arial.ttf", 70)
        new_font = new_font.font_variant(size = new_font.size-1)
        while check_len(text, new_font) > max_size and new_font.size > 1 :
            new_font= new_font.font_variant(size = new_font.size-1)
        drawer.multiline_text(coor[i%3], text, font = new_font, align = "center", anchor="ms", spacing=10, fill='black')
    else:
        drawer.multiline_text(coor[i%3], text, font = font_text, align = "center", anchor="ms", spacing=10, fill='black')

    if check_len(text_head, font_for_head) > max_size:
        new_font = ImageFont.truetype("arial.ttf", 70)
        new_font = new_font.font_variant(size = new_font.size-1)
        while check_len(text_head, new_font) > max_size and new_font.size > 1 :
            new_font= new_font.font_variant(size = new_font.size-1)
        drawer.multiline_text(coor_head[i%3], text_head, font = new_font, align = "center", anchor="ms", spacing=10, fill='black')
    else:
        drawer.multiline_text(coor_head[i%3], text_head, font = font_for_head, align = "center", anchor="ms", spacing=10, fill='black')
    image.save(name_file)

