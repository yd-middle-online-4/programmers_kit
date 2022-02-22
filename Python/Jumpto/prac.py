def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lnag in language:
        print(lang, end=" ")
    print()

profile('유재석', 20, 'kot', 'java')