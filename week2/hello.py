girls = ["Mia", "Ella", "Cory", "Tasmin", "Zoe", "Emi"]
boys = ["Hiro", "Jasper", "Beckett", "Aydin"]

while True:
    person = raw_input('Enter your name: ')
    if person in boys:
        print "Yo!  What's up " + person + "!!!"
    elif person in girls:
        print "Hey " + person + ". How are you? :)"
    else:
        print "Hello " + person
    if person == "Exit":
        break
