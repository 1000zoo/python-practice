"""
    ex:
        string = (1.2345, 3.2331)
"""

def str_to_flist(t):
    try:
        k = t.split(",")
        k[0] = float(k[0])
        k[1] = float(k[1])
    except IndexError as err:
        return (0, 0)
    return k