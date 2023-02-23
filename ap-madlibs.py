#https://www.youtube.com/watch?v=O69N6Gk3eaw

# set variables for input
adj1=input("Adjective: ")
verb1=input("Verb: ")
verb2=input("Verb: ")
famous_person=input("Famous person: ")

#set variable for madlib, including placeholders for input variables to fill. Assign madlibs placeholders to variables 
madlib="Computer programming is so {adj1}! It makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}".format(adj1=adj1,verb1=verb1,verb2=verb2,famous_person=famous_person)

#print the madlib. Shell will ask for user input before it can complete the print
print(madlib)

#workaround to keep microsoft shell open by waiting for input. Stops the autoclose
input('Press ENTER to exit')