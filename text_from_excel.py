from PIL import Image, ImageDraw, ImageFont
import pandas as pd

mebers_com = {}
list_com = pd.read_excel('list of comands.xlsx')
font_text = ImageFont.truetype("C:\Windows\Fonts\BOOKOSI.TTF", 23)
font_for_head = ImageFont.truetype("C:\Windows\Fonts\BOOKOSB.TTF", 20)
coor_head = [(130, 110), (410, 110), (130, 310), (410, 310), (130, 500), (410, 490), (130, 675)]
coor = [(130, 150), (410, 150), (130, 350), (410, 350), (130, 550), (410, 530), (130, 715)]
max_size = 190
max_size_head = 160
def check_len (text, font):
    text = text.split('\n')
    return  max(list(map(lambda x: font.getlength(x), text)))

for data in list_com.itertuples(index=False, name='People'):
    com = data.Команда
    name_file = com + ".png"
    if com in mebers_com:
        mebers_com [com] += 1
        image = Image.open(name_file)
        drawer = ImageDraw.Draw(image)
    else: 
        mebers_com [com] = 0 
        image = Image.open("template.png")
        drawer = ImageDraw.Draw(image)

    if data.Статус != "Руководитель":
        text_head = "{}\n\"{}\"".format (data.Статус, com)
        text = "{}".format (data.ФИО)
    else:
        new_fio = data.ФИО.split()
        new_fio = new_fio[0] + '\n' + new_fio[1] + ' ' + new_fio[2]
        text_head = "{}\n\"{}\"".format (data.Статус, com)
        text = "{}".format (new_fio)

    if check_len(text, font_text) > max_size:
        new_font = ImageFont.truetype("C:\Windows\Fonts\BOOKOSI.TTF", 23)
        new_font = new_font.font_variant(size = new_font.size-1)
        while check_len(text, new_font) > max_size and new_font.size > 1 :
            new_font= new_font.font_variant(size = new_font.size-1)
        drawer.multiline_text(coor[mebers_com [com]], text, font = new_font, align = "center", anchor="ms", fill='black')
    else:
        drawer.multiline_text(coor[mebers_com [com]], text, font = font_text, align = "center", anchor="ms", fill='black')

    if check_len(text_head, font_for_head) > max_size:
        new_font = ImageFont.truetype("C:\Windows\Fonts\BOOKOSB.TTF", 20)
        new_font = new_font.font_variant(size = new_font.size-1)
        while check_len(text_head, new_font) > max_size_head and new_font.size > 1 :
            new_font= new_font.font_variant(size = new_font.size-1)
        drawer.multiline_text(coor_head[mebers_com [com]], text_head, font = new_font, align = "center", anchor="ms", fill='black')
    else:
        drawer.multiline_text(coor_head[mebers_com [com]], text_head, font = font_for_head, align = "center", anchor="ms", fill='black')
    image.save(name_file)



