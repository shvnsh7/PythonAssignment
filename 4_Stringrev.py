# IV.Write a program to return below output from given input (with and without uses of inbuilt function)
# Input -  "My name is Suraj"
# output - "Suraj is name My"

def reverseStr(Sentence):
    word=Sentence.split(' ')
    #print(word)
    rev=' '.join(reversed(word))
    return rev

# if __name__=="__main__":
#     input="My name is Suraj"
#     print(reverseStr(input))

Sentence="My name is Suraj"
print(reverseStr(Sentence))


    















# def reverse(S):
#     Str=""
#     for i in S:
#         Str=i+Str
#     return Str

# S="My name is Suraj"

# print(reverse(S))
