from PIL import Image


def main():
    original_name = input('Type image name to decode: ')
    lsb_image = Image.open(original_name)
    image_data = lsb_image.load()

    width, height = lsb_image.size

    for y in range(height):
        for x in range(width):
            if image_data[x, y][0] & 1 == 1:
                image_data[x, y] = (255, 255, 255)
            else:
                image_data[x, y] = (0, 0, 0)

    lsb_image.save(original_name.split('.')[0] + '_Decoded.png')


def main_test():
    lsb_image = Image.open(input('Type image name to decode: '))
    image_data = lsb_image.load()

    width, height = lsb_image.size

    for y in range(height):
        count = 0
        ascii_code = 0
        for x in range(width):
            # if image_data[x, y][0] & 1 == 1:
            #     image_data[x, y] = (255, 255, 255)
            # else:
            #     image_data[x, y] = (0, 0, 0)
            if not image_data[x, y][0] == 0:
                ascii_code += 2**count
            count += 1

            if count > 7:
                print(chr(ascii_code))
                count = 0
                ascii_code = 0

    lsb_image.save('Decoded.png')


if __name__ == '__main__':
    main()
