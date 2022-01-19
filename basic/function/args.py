def profile(name, age, *favorite_movie):
    print("name: {0}\t age: {1}\t".format(name, age), end="")
    for m in favorite_movie:
        print(m,  end=" ")
    print()
    
profile("JW", 26, "Endgame", "Lalaland", "Kimi", "Pulp fiction", "Don't look up")
profile("JK", 18, "Avengers", "Ironman", "Thor", "Spiderman")