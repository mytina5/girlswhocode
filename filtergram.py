from filters import*

#Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(icecream):
    #im = Image.open("dulceicecream.jpg")
    #rgb_im = im.convert('RGB')
    #r, g, b = rgb_im.getpixel((1,1))
    #print(r, g, b)
    #color = list im
    darkBlue = ( 0, 51, 76)
    red = ( 217, 26, 33)
    lightblue = ( 112, 150, 150)
    yellow = (252, 227, 166)

    color = list(im.getdata())
    list_length = len(color)

    for i in range(list_length):
        redd = color[i][0]
        greend = color[i][1]
        blued = color[i][2]
        sum = redd + greend + blued

        if sum < 182:
            color [i] = darkBlue
        elif sum > 182 and sum < 364:
            color [i]  = red
        elif sum > 364 and sum < 546:
            color [i] = lightblue
        elif sum > 546:
            color [i] = yellow

    filternew = im.putdata(color)
    def save_img(im, filternew):
        im.save(filternew)
    save_img (im, "newdulceicecream.jpg")
    newpic = load_img("newdulceicecream.jpg")
    show_img(newpic)

im = load_img("dulceicecream.jpg")
show_img(im)
obamicon(im)
