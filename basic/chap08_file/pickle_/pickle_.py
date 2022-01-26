import pickle

profile_file = open("profile.pickle", "wb")
profile = {"name" : "Jiwoo", "age" : 26, "hobby" : ["game", "coding", "Youtube"]}

pickle.dump(profile, profile_file)
profile_file.close()