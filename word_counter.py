def word_counter():
    text = input("Enter some text: ")
    words = text.split()
    count = len(words)
    print("Word count: ", count)
    
word_counter()
