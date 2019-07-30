from PIL import Image
# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(picture):
    im = Image.open(picture)
    return im


# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(picture):
    picture.show()
    #im = Image.new("RGB", (471, 552))
# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.

def save_img(picture, icecream):
    picture.save(icecream)


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(pic):
    a = 0

im = load_img("dulceicecream.jpg")
show_img(im)

save_img (im, "myicecream.jpg")
