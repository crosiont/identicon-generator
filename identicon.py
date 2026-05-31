from PIL import Image, ImageDraw
import hashlib
import sys

user_input = input("Your string here: ")
encoded_input = user_input.encode('utf-8') #convert to computer readable
hashed_input = hashlib.md5(encoded_input) #hashing the encoded text
user_data = list(hashed_input.digest()) #turning the hashed input into a list of numbers
#print(user_data)

def coord_update(x_start, y_start, x_end, y_end, img):
    x_start += 60
    x_end += 60
    if x_start == 360:
        y_start += 60
        y_end += 60
        x_start = 0
        x_end = 60
        if y_start == 360:
            img.save("output.png")
            sys.exit("finished generating identicon! saved in output.png. exiting now...")
    return x_start, y_start, x_end, y_end

def draw_thing():
    x_start = 0
    x_end = 60
    y_start = 0
    y_end = 60
    w = 3
    img = Image.new("RGB", (300,300), "white")
    draw = ImageDraw.Draw(img)# bind drawing tool to blank canvas
    #pillow defines a rectangle using [x_start, y_start, x_end, y_end]
    #block size is 60
    while True:
        if user_data[w] % 2 == 0:
            draw.rectangle([x_start, y_start, x_end, y_end], fill=(user_data[0], user_data[1], user_data[2]))
            w += 1
            if w == 15:
                w = 4
            x_start, y_start, x_end, y_end = coord_update(x_start, y_start, x_end, y_end, img)
        else:
            w += 1
            if w == 15:
                w = 4
            x_start, y_start, x_end, y_end = coord_update(x_start, y_start, x_end, y_end, img)

draw_thing()
