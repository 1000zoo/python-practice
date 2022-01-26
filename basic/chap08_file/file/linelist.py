score_file = open("score.txt", "r", encoding="utf8")

lines = score_file.readlines()
for line in lines:
    print(line, end="")

print("\n" + "-"*50)
print(lines)

score_file.close()