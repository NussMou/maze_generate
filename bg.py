from PIL import Image, ImageDraw

bg = Image.new('RGBA', (1000, 1000), (255, 0, 0, 0))
img = Image.open('stone.png')
stone = img.resize((25, 25))
for i in range(39):
    for j in range(41):
        x = j*25 
        y = i*25
        place = 40*i+j*1+i     
        bg.paste(stone,(x, y)) 
for k in range(40):
    x = k*25
    y = 39*25
    bg.paste(stone,(x,y))
bg.save('bg.png')
