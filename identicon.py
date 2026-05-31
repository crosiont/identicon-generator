from PIL import Image

def make_blank_canvas():
    img = Image.new("RGB", (300,300), "white")
    img.save("test_output.png")
    print("Canvas created!")
    
make_blank_canvas()
