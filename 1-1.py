file = open("alice.txt", 'r')

data = file.read()
result = []

print(data)

for i in range(65, 91):
    result.append({"name": chr(i), "count": int(eval("str(data.count(\"" + chr(i) + "\"))"))})

for x in range(97, 123):
    result.append({"name": chr(x), "count": int(eval("str(data.count(\"" + chr(x) + "\"))"))})

result.sort(reverse=True, key=lambda x: x['count'])

for z in range(0, 52):
    print(result[z])

file.close()



