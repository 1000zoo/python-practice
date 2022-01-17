domain = "http://youtube.com"

print(domain)
startIndex = domain.find('/')
if startIndex == -1:
    startIndex = 0
else:
    startIndex = domain.find('/', startIndex + 1) + 1

endIndex = domain.find('.')

renew = domain[startIndex: endIndex]
print(renew)

password = renew[0:3] + str(len(renew)) + str(renew.count('e')) + '!'

print(password)