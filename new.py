from filters import*

def iceicon(icecream):
    black = (0, 0, 0)
    darkgray = (128, 128, 128)
    lightgray = (192, 192, 192)
    white = (255, 255, 255)

    color = list(im.getdata())
    list_length = len(color)

    for i in range(list_length):
        redd = color[i][0]
        greend = color[i][1]
        blued = color[i][2]
        sum = redd + greend + blued

        if sum < 182:
            color [i] = black
        elif sum > 182 and sum < 364:
            color [i] = darkgray
        elif sum > 364 and sum < 546:
            color [i] = lightgray
        elif sum > 546:
            color [i] = white

    filternew = im.putdata(color)
    def save_img(im, filternew):
        im.save(filternew)
    save_img (im, "newnewdulceicecream.jpg")
    newpic = load_img("newnewdulceicecream.jpg")
    show_img(newpic)

im = load_img("dulceicecream.jpg")
show_img(im)
iceicon(im)   
