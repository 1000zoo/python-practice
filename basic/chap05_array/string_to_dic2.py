dic = {"a":"A", "b":"B", "c":123, "d":43.12, "e":(123.22, 122.22)}

def dic_to_cust_dic(*labels):
    k = ""
    for l in labels:
        k += l + ":" + str(dic[l]) + "/"
    return k
print(dic_to_cust_dic("a", "c", "d"))
l = dic_to_cust_dic("a", "c", "e").split("/")

print(l)

ndic = {}
for w in l:
    if w != '':
        w_ = w.split(":")
        ndic[w_[0]] = w_[1]
        
print(ndic, type(ndic))