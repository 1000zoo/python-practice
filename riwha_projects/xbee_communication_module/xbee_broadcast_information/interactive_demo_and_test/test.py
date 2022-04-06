# # dic = {}

# # try:
# #     print(dic["k"])
# # except KeyError as err:
# #     print(err)
# #     print("error")

# k = "hello-my.pp"

# dic = {}
# dic["a"] = k
# dic["b"] = "wfa"

# # print(dic)
# # del dic["a"]
# # print(dic)
# # print(dic.__contains__("b"))
# # print(dic.keys())

# try:
#     print(dic["c"])
# except KeyError as err:
#     print(err)
#     print("error : %s" %err)
#     if str(err) == "'c'":
#         print("error CCCC!!")
#     else:
#         print("no")

# data = {
#     'vehicleId': '97가1006', 
#     'nodeId': 'BACK', 
#     'lane': 'lane2', 
#     'GPS': (36.12323, 123.32312)
# }
# s = str(data)

# dic = {}
# s = s.strip("{""}")
# ls = s.split(",")
# for w in ls:
#     try:    
#         w = w.split(":")
#         dic[w[0].strip(" '")] = w[1].strip(" '")
#     except IndexError as err:
#         print(err) 
# print(dic)

# k = (1,2,3,4)
# try:
#     def print_tup(k):
#         try:
#             print(k[6])
#         except:
#             print("f")
#             raise KeyError("no")
#     print_tup(k)
# except KeyError as err:
#     print("dd")
#     print(err)
    
# k = ["2.4213", "2.111"]
# print(float(k))