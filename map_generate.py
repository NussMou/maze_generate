from PIL import Image, ImageDraw

f = open("input.txt", "r")
char = f.read()
# char = char.replace("\n ","")
# print(character)
# print(len(char))

bg = Image.new('RGBA', (1000, 1000), (255, 0, 0, 0))
# img = Image.open('wall.png')
img = Image.open('brown.png')
# img2 = Image.open('empty.png')
wall = img.resize((25, 25))
# empty = img.resize((25, 25))
for i in range(39):
    for j in range(41):
        x = j*25 
        y = i*25
        place = 40*i+j*1+i
        if char[place] == '#':          
            bg.paste(wall,(x, y)) 
for k in range(40):
    x = k*25
    y = 39*25
    bg.paste(wall,(x,y))
# bg.save('final.png', 'gif', transparency=0)
bg.save('final.png')
