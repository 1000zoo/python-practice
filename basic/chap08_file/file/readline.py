score_file = open("score.txt", "r", encoding="utf8")

print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print("\n")

score_file = open("score.txt", "r", encoding="utf8")

while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
    
score_file.close()