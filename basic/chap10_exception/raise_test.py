k = {"a" : "A", "b" : "B"}
a = [1,2,3]

def main():
    try:
        # print(k["c"])
        some()
    except KeyError as err:
        print(err)
        print(str(err) == "'some error'")

def some():
    try:
        print(a[4])
    except IndexError:
        print("error at 'some()'")
        raise KeyError("some error")        

if __name__ == '__main__':
    main()