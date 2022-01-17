myStr = 'Hello World.'

print(myStr.lower())
print(myStr.upper())
print(myStr[0].isupper())   #boolean
print(len(myStr))
print(myStr.replace('World.', 'Jiwoo!'))

index = myStr.index("o")
print(index)
index_ = myStr.index('o', index + 1) 
print(index_)
#.index: error, end / .find: return -1, keep run

print(myStr.count('o'))
