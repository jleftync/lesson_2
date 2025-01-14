def titlize(sentence):
    words = sentence.split()
    new_words = []

    for word in words:
        if len(word) > 2:
            word = word.capitalize()
            # print(word)        # Delete line
        new_words.append(word)
            #print(new_words)
            
        #elif len(word) <= 2:
            #new_words.append(word)
            #print(word)
    return ' '.join(new_words)
  

title = 'hello world of programming'
print(titlize(title))
