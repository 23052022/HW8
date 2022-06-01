string = "The Very Hungry Caterpillar"
print("1:", string[0:len(string):2])
print("2:", string[1:len(string):2])
print("3:", string[5])
print("4:", string[0:10:])
print("5:",string[22:])
print("6:",string[::-1])
print("7",string[::-2])
print("8:", [len(string)])
if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


