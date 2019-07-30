from filters import*

def rainbow(icecream):
    red = (231, 76, 60)
    orange = (243, 156, 18)
    yellow = (244, 208, 63)
    green = (39, 174, 96)
    blue = (52, 152, 219)
    purple = (142, 68, 173)

    color = list(im.getdata())
    list_length = len(color)

    for i in range(list_length):
        redd = color[i][0]
        greend = color[i][1]
        blued = color[i][2]
        sum = redd + greend + blued

        if sum < 150:
            color [i] = red
        elif sum > 150 and sum < 250:
            color [i] = orange
        elif sum > 250 and sum < 350:
            color [i] = yellow
        elif sum > 350 and sum < 400:
            color [i] = green
        elif sum > 400 and sum < 450:
            color [i] = blue
        elif sum > 450:
            color [i] = purple

    #filternew = im.putdata(color)
    #def save_img(im, filternew):
        #im.save(filternew)
    #save_img (im, "newnewnewnewdulceicecream.jpg")
    #newpic = load_img("newnewnewnewdulceicecream.jpg")
    #show_img(newpic)

#im = load_img("dulceicecream.jpg")
#show_img(im)
#rainbow(im)

    new_image2 = Image.new("RGB", (1000, 669), p)
    new_image2.putdata (color)
    return new_image2
