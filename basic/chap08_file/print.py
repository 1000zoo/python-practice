print("Python", "Java")
print("Python" + "Java")

print("Python", "Java", sep=", ")
print("Python", "Java", sep=", ", end="?")
print("JS")

import sys

print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)
