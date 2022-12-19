data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result = sort()

if value != 0:
    result.apend(str(value))

print('', join(result))