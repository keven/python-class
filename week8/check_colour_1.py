def read_text():
    quotes = open("/Users/kevenlin/Desktop/python_class/week8/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
read_text()
