f = open("alice.txt", 'r')

data = f.readline()
result = []

for x in data:
    result.append({"name : " + x + "count : " + str(data.count(x))})

for x in result:
    print(result)
f.close()
