print("a" + "b")
print("a", "b") #space

# %form
print("I'm %d." %26)
print("I like %s." %"apple")
print("Apple starts with %c." %"A")

print("I'm %s." %26)

print("I like %s and %s." % ('Apple',  'Samsung'))

# format
print("I'm {age} and I like {language}.".format(age = 26, language = 'Python'))

age = 26
language = 'Python'

print(f"I'm {age} and I like {language}.")