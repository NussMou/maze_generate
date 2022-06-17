from PIL import Image, ImageDraw

bg = Image.new('RGBA', (25, 25), (255, 0, 0, 0))

bg.save('empty.png', 'gif', transparency=0)