from random import *

lst = [['a','p','p','l','e'],['b','a','n','a','n','a'],['o','r','a','n','g','e']]
word = choice(lst)
answers = ""

while True:
    succeed = True
    for w in word:
        if w in answers:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False
    print("")
    if succeed:
        print("Success")
        break
    answer = input("Input letter: ")
    if answer not in answers:
        answers += answer
    
    if answer in word:
        print("Correct")
    else:
        print("Wrong")