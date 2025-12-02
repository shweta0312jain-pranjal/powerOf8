def isPowerOf8(number):
   
    if number <= 0:
        return False
    

    while number % 8 == 0:
        number = number // 8

    return number == 1


n = int(input("Enter a number: "))

if isPowerOf8(n):
    print("The number is a power of 8")
else:
    print("The number is NOT a power of 8")