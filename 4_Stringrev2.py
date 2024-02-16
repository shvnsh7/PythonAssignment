def reverse_sentence(Sentence):
    words=[]  #empty list is initialised to store the words in sentence
    current_word=' ' #empty string 
    for character in Sentence:
        if character==' ':
            words.append(current_word)
            current_word=''
        else:
            current_word+=character
    words.append(current_word)
    reversed_sentence=' '.join(reversed(words))
    return reversed_sentence

input_sentence=input("Enter a sentence: ")
#input_sentence="My name is Suraj"
reversed_sentence=reverse_sentence(input_sentence)
print("Reversed Sentence: ",reversed_sentence)


