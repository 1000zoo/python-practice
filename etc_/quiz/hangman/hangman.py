class CharError(Exception):
    pass
class NoneAlphabetError(Exception):
    pass

# answer = "HANGMAN"
# blank = "_"*len(answer)
answer = list("HANGMAN")
answer_backup = list("HANGMAN")
blank = list("_"*len(answer))



<<<<<<< HEAD
while answer != answer_backup:
=======
while blank != answer_backup:
>>>>>>> 3115d82abdd5953db23b54fe335ccc2742e92878
    try:
        turn = input(">>>")
        if len(turn) != 1 or type(turn) != str:
            raise CharError
        elif not turn.isalpha():    #        elif ((turn < 'a' or turn > 'z') and (turn < 'A' or turn > 'Z')):
            raise NoneAlphabetError
            
    except CharError:
        print("only one alphabet")
        continue
    except NoneAlphabetError:
        print("only alphabet")
        continue
    
    turn = str(turn).capitalize()
    i = 0
    while i < len(answer) and answer.__contains__(turn):
        k = answer.index(turn, i)
        answer[k] = "-"
        blank[k] = turn
        i += k + 1
    print(str(blank))
    
print("Correct!")