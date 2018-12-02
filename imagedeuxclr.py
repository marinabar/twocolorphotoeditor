from PIL import Image
nb=int(input("How much red or blue do you want ? -0 : total blue, 250 : total red and 100 the middle"))
img = Image.open("avantages-quil-y-a-a-grandir-dans-un-petit-village.jpg")
pixels = img.load()
for i in range(img.width):
    for j in range(img.height):
        r, g, b = pixels[i, j]
        z = (r + g + b) // 3
        if nb > z:
            pixels[i, j] = (237, 28, 28)
        else:
            pixels[i, j]=(7, 13, 58)
img.show()


            
