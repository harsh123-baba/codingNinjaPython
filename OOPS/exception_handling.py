
while True:
    try:
        n = int(input("Enter no "))
        m = int(input("second no "))
        z = n/m
        print(z)
        break
    except ValueError:
        print("somthing wrong ")
    except ZeroDivisionError:
        print("Division with zero is not allowed")
    
