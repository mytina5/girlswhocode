from filters import*

def newnewicon(icecream):
    darkest = (69, 69, 69)
    dark = (140, 140, 140)
    light = (154, 154, 154)
    lightest = (203, 203, 203)

    color = list(im.getdata())
    list_length = len(color)

    for i in range(list_length):
        redd = color[i][0]
        greend = color[i][1]
        blued = color[i][2]
        sum = redd + greend + blued

        if sum < 182:
            color [i] = darkest
        elif sum > 182 and sum < 364:
            color [i] = dark
        elif sum > 364 and sum < 546:
            color [i] = light
        elif sum > 546:
            color [i] = lightest

    filternew = im.putdata(color)
    def save_img(im, filternew):
        im.save(filternew)
    save_img (im, "newnewnewnewdulceicecream.jpg")
    newpic = load_img("newnewnewnewdulceicecream.jpg")
    show_img(newpic)

im = load_img("dulceicecream.jpg")
show_img(im)
newnewicon(im)
