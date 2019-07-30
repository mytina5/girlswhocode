#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")


print("Can your password survive a dictionary attack?")


#Take input from the keyboard, storing in the variable test_password

#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = input("Type in a trial password: ").lower()

#if test_password == row in f:
    #print("Your password is too weak")
#years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
        #2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
        #2016, 2017, 2018, 2019, 2020]


for row in f:
    if len(test_password) < 6:
        print("Your password is too short")
        break
    if test_password in  row:
        print("Your password is too weak")
        break
    if test_password not in row:
        #print("Your password is strong enough")
        continue



#Write logic to see if the password is in the dictionary file below here:
