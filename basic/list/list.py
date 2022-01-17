subway = [10, 20, 30]
print(subway)

subway_ = ["1호", "2호", "3호"]
print(subway_)
print(subway_.index("3호"))

subway_.append("4호")
print(subway_)

subway_.insert(1, "1+3/4호")
print(subway_)

print(subway_.pop())
print(subway_)
print(subway_.pop())
print(subway_)

subway_.append("2호")
print(subway_)
print(subway_.count("2호"))

