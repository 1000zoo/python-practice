scores = {"Math" : 80, "Java" : 70, "Python" : 90}

for subject, score in scores.items():
    print(subject, score, sep=": ")

for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4),  sep=" : ")