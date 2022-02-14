def callback(c):
    return c

def str_len(callback):
    myStr = "asdfasd"
    k = callback(len(myStr))
    return k
    
k = str_len(callback)

print(k)