print("{0}".format(500))
print("{0: >10}".format(500))
print("{0: >10}".format(-500))

print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

print("{0:_<10}".format(500))

print("{0:,}".format(1000000000000000))

print("{0:.2f}".format(5/3))

# {인덱스:[[빈자리채우기]정렬][기호][확보공간][콤마][.자릿수][타입]}