from filters import*

def newicon(icecream):
    red = (255, 87, 51)
    orange = (230, 126, 34)
    lighto = (245, 176, 65)
    yellow = (247, 220, 111)

    color = list(im.getdata())
    list_length = len(color)

    for i in range(list_length):
        redd = color[i][0]
        greend = color[i][1]
        blued = color[i][2]
        sum = redd + greend + blued

        if sum < 182:
            color [i] = red
        elif sum > 182 and sum < 364:
            color [i] = orange
        elif sum > 364 and sum < 546:
            color [i] = lighto
        elif sum > 546:
            color [i] = yellow

    filternew = im.putdata(color)
    def save_img(im, filternew):
        im.save(filternew)
    save_img (im, "newnewnewdulceicecream.jpg")
    newpic = load_img("newnewnewdulceicecream.jpg")
    show_img(newpic)

im = load_img("dulceicecream.jpg")
show_img(im)
newicon(im)
