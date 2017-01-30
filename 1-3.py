def encryption(passwd):
    result = ""
    for i in passwd:
        result += (chr(ord(i) + shift))
    return result


def decryption(passwd):
    result = ""
    for x in passwd:
        result += (chr(ord(x) - shift))
    return result

shift = int(input("INPUT THE SHIFT(NUM) :"))
passwd = input("INPUT THE PASSWORD : ")

result1 = encryption(passwd)
result2 = decryption(result1)

print("========= RESULT =========")
print("ENCRYPTED : ", result1)
print("DECRYPTED : ", result2)
print("==========================")