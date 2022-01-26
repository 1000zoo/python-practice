import pickle

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)

print(profile)
profile_file.close()