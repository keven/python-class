import urllib

def read_text():
    quotes = open("/Users/kevenlin/Desktop/python_class/week8/movie_quotes.txt")
    contents_of_file = quotes.read()
    quotes.close()
    check_colour(contents_of_file)

def check_colour(text_to_check):
    connection = urllib.urlopen("http://animalwords-187005.appspot.com/?q=" + text_to_check)
    output = connection.read()
    print(output)
    connection.close()

read_text()
