from PIL import Image, ImageDraw, ImageFont
import pandas as pd

mebers_com = {}
list_com = pd.read_excel('list of comands.xlsx')
font = ImageFont.truetype("C:\Windows\Fonts\Gabriola.ttf", 20)
coor = [(130, 110), (410, 110), (130, 310), (410, 310), (130, 500), (410, 490), (130, 675)]

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
        text = "{}\n\"{}\"\n{}".format (data.Статус, com, data.ФИО)
    else:
        new_fio = data.ФИО.split()
        new_fio = new_fio[0] + '\n' + new_fio[1] + ' ' + new_fio[2]
        text = "{}\n\"{}\"\n{}".format (data.Статус, com, new_fio)
    drawer.multiline_text(coor[mebers_com [com]], text, font=font, align = "center", anchor="ms", fill='black')
    image.save(name_file)

