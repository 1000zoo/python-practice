"""
    ex:
        string = {"a" : "A", "b" : "B", "c" : "123"}
    =>  dictionary = {"a" : "A", "b" : "B", "c" : "123"}
    
    wrong parameter:
        string = {"a" : (1,2,3), "b" : "my name: 1000zoo"}
"""

def string_to_dict(s):
    dic = {}
    s = s.strip("{""}")
    ls = s.split(",")
    for w in ls:
        try:    
            w = w.split(":")
            dic[w[0].strip(" '")] = w[1].strip(" '")
        except IndexError as err:
            print(err)
            ed = {}
            return ed
    return dic