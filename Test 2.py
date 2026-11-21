try:
    num = int(input("Enter a number ( 1 and beyond ) : "))
    
    num2 = int(input("Enter a second number ( 1 and beyond ) : "))

except ValueError :

    print ("Enter a nummber.")

except ZeroDivisionError :

    print("You should not enter a zero.")

    def sub ( a , b):
        minus = a - b
        print(minus)
        return (minus)

    def add ( c, d):
        sums = c + d
        print(sums)
        return(sums)

    def multiply ( e, f):
        product = e * f
        print(product)
        return (product)

    def divide ( g, h):
        quotient = g / h
        print(quotient)
        return (quotient)

    print (sub (num, num2))

    print (add (num, num2))

    print ( multiply(num, num2))

    print (divide (num, num2))