import qrcode
from PIL import Image

original_name = input('Type target image name with extension: ')
original_image = Image.open(original_name)
original_width, original_height = original_image.size
text = input('Type some text here: ')
CHANNEL = 2

qr_image = qrcode.make(text)

width = original_height
if original_width < original_height:
    width = original_width

resized = qr_image.resize((width, width), resample=Image.NEAREST)

# resized.save('gg.png')

original_data = original_image.load()
qr_data = resized.load()

start_x = (original_width - width) / 2
start_y = (original_height - width) / 2

for y in range(width):
    for x in range(width):
        if qr_data[x, y] == 255:
            if not original_data[start_x + x, start_y + y][CHANNEL] % 2:
                if CHANNEL == 0:
                    original_data[start_x + x, start_y +
                                  y] = (original_data[start_x + x, start_y + y][CHANNEL]+1,) + original_data[start_x + x, start_y + y][1:]
                else:
                    original_data[start_x + x, start_y +
                                  y] = original_data[start_x + x, start_y + y][:CHANNEL] + (original_data[start_x + x, start_y + y][CHANNEL]+1,) + original_data[start_x + x, start_y + y][CHANNEL+1:]
        else:
            if original_data[start_x + x, start_y + y][CHANNEL] % 2:
                if CHANNEL == 0:
                    original_data[start_x + x, start_y +
                                  y] = (original_data[start_x + x, start_y + y][CHANNEL]-1,) + original_data[start_x + x, start_y + y][1:]
                else:
                    original_data[start_x + x, start_y +
                                  y] = original_data[start_x + x, start_y + y][:CHANNEL] + (original_data[start_x + x, start_y + y][CHANNEL]-1,) + original_data[start_x + x, start_y + y][CHANNEL+1:]

original_image.save(original_name.split('.')[0] + '_LSBOwO.png')
print('Image saved')
