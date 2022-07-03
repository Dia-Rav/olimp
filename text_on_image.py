from PIL import Image, ImageDraw, ImageFont
comands = open ("comands.txt", "r", encoding='utf-8')
font = ImageFont.truetype("arial.ttf", 20)

for s in comands:
    image = Image.open("template.png")
    drawer = ImageDraw.Draw(image)
    com = s[:-1]
    text = "Участник\n\"{}\"".format (com)
    drawer.multiline_text((130, 120), text, font=font, align = "center", anchor="ms", fill='black')
    drawer.multiline_text((410, 120), text, font=font, align = "center", anchor="ms", fill='black')
    drawer.multiline_text((130, 320), text, font=font, align = "center", anchor="ms", fill='black')
    drawer.multiline_text((410, 320), text, font=font, align = "center", anchor="ms", fill='black')
    drawer.multiline_text((130, 500), text, font=font, align = "center", anchor="ms", fill='black')
    drawer.multiline_text((410, 500), text, font=font, align = "center", anchor="ms", fill='black')
    text = "Руководитель\n\"{}\"".format (com)
    drawer.multiline_text((130, 695), text, font=font, align = "center", anchor="ms", fill='black')
    name_file = com + ".png"
    print (name_file)
    image.save(name_file)

