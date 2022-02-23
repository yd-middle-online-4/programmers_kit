from random import choice

words = ['apple','banana','orange']
word = choice(words)
answers = ""

while True:
    Succeed = True
    
    for w in word:
        if w in answers:
            print(w, end=" ")
        else:
            print("_", end=" ")
            Succeed = False
            
    print()
    if Succeed == True:
        print('SUCCESS')
        break   
    
    answer = input("Press letter :")
    if answer not in answers:
        answers += answer
        print('Correct')
    else:
        print('Wrong')
  
