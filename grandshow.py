from grandfilters import *

def main():
    #change "file_name_here with your image link"
    myImg = load_img("dulceicecream.jpg")
    #pick one of the filters here
    newImg = annie_instagram(myImg)

    newImg.show()

main()
