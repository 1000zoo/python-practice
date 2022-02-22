"""
    ex:
        data = {"a" : "A", "b" : "B", "c" : "C"}
        make_info_string("a", "c", data)
    =>  k = "a:A/c:C/"
"""

def make_info_string(*labels, data):
    k = ""
    for l in labels:
        try:
            k += l + ":" + str(data[l]) + "/"
        except KeyError as err:
            print("Key '%s' does not exist in data" % err)
    return k