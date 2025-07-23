import art
def add(n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return  n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(art.logo)

go = True

while go:
    first_numer =int(input("First number"))
    operator = input("type a mathematical operatora choice of '+', '-' , '*'  or  '/'")
    seond_numer =int(input("Second number"))

    result = operations[operator](first_numer, seond_numer)
    print(result)

    continu = input("Do you want to continue whit the previus resolut? (yes or no)")
    if continu == "yes":
        operator = input("type a mathematical operatora choice of '+', '-' , '*'  or  '/'")
        seond_numer = int(input("Second number"))

        result = operations[operator](result, seond_numer)
        print(result)



