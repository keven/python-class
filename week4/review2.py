age = input("How old are you? ")
if age >= 12:
    print 'You are too old'
    print 'Why are you here?'
else:
    b = '\U0001F600'
    print b.decode('unicode-escape')

age = input("How old are you? ")
if age == 10 or age == 11 or age == 12 or age == 13:
    print "What's 13 + 39 + 84 + 155 + 97? A headache!"
else:
    print "Huh?"
