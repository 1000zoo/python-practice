class CharError(Exception):
    pass
class NoneAlphabetError(Exception):
    pass

# answer = "HANGMAN"
# blank = "_"*len(answer)
answer = list("HANGMAN")
blank = list("_"*len(answer))



while answer != '-'*len(blank):
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
    
    
#루프탈출