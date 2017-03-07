squared = []
for n in range(11):
    squared.append(n**2)

print(squared)


squared = [ n**2 for n in range(11) if n % 2 is 0 ]
print(squared)
