from operator import ne
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

mebers_com = {}
list_com = pd.read_excel('list_other.xlsx')
font_text = ImageFont.truetype("arial.ttf", 100)
font_for_head = ImageFont.truetype("arial.ttf", 140)
coor_head = [(1000, 470), (2353, 470), (1000, 1271), (2353, 1271), (1000, 2080), (2353, 2080),(1000, 470), (2353, 470), (1000, 1271), (2353, 1271), (1000, 2080), (2353, 2080), (1000, 470), (2353, 470), (1000, 1271), (2353, 1271), (1000, 2080), (2353, 2080) ]
coor = [(1000, 600), (2350, 600), (1000, 1400), (2353, 1400), (1000, 2220), (2353, 2220),(1000, 600), (2350, 600), (1000, 1400), (2353, 1400), (1000, 2220), (2353, 2220), (1000, 600), (2350, 600), (1000, 1400), (2353, 1400), (1000, 2220), (2353, 2220)]
max_size = 1200
max_size_head = 1200
def check_len (text, font):
    text = text.split('\n')
    return  max(list(map(lambda x: font.getlength(x), text)))

for data in list_com.itertuples(index=False, name='People'):
    com = data.Команда
    if com in mebers_com and mebers_com [com] > 5:
        name_file = com + "({}).png".format((mebers_com [com]|+1)//6)
    else:
        name_file =  com + ".png"
    if  com in mebers_com:
        mebers_com [com] += 1
    else:
        mebers_com [com] = 1
    if mebers_com [com] % 6 != 1 and mebers_com [com] != 1:
        image = Image.open(name_file)
        drawer = ImageDraw.Draw(image)
    elif mebers_com [com]%6 == 1 and mebers_com [com] != 1: 
        image = Image.open("template.png")
        drawer = ImageDraw.Draw(image)
    else:
        image = Image.open("template.png")
        drawer = ImageDraw.Draw(image)

    new_fio = data.ФИО.split()
    if len(new_fio)>2:
        new_fio = str(new_fio[0] + '\n' + new_fio[1] + ' ' + new_fio[2])
    else:    
        new_fio = str(new_fio[0] + ' ' + new_fio[1])
    text_head = "{}\n".format (data.Статус)
    text = "{}".format (new_fio)

    if check_len(text, font_text) > max_size:
        new_font = ImageFont.truetype("arial.ttf", 140)
        new_font = new_font.font_variant(size = new_font.size-1)
        while check_len(text, new_font) > max_size and new_font.size > 1 :
            new_font= new_font.font_variant(size = new_font.size-1)
        drawer.multiline_text(coor[mebers_com [com]%6], text, font = new_font, align = "center", anchor="ms", spacing=10, fill='black')
    else:
        drawer.multiline_text(coor[mebers_com [com]%6], text, font = font_text, align = "center", anchor="ms", spacing=10, fill='black')

    if check_len(text_head, font_for_head) > max_size:
        new_font = ImageFont.truetype("arial.ttf", 140)
        new_font = new_font.font_variant(size = new_font.size-1)
        while check_len(text_head, new_font) > max_size_head and new_font.size > 1 :
            new_font= new_font.font_variant(size = new_font.size-1)
        drawer.multiline_text(coor_head[mebers_com [com]%6], text_head, font = new_font, align = "center", anchor="ms", spacing=10, fill='black')
    else:
        drawer.multiline_text(coor_head[mebers_com [com]%6], text_head, font = font_for_head, align = "center", anchor="ms", spacing=10, fill='black')
    image.save(name_file)