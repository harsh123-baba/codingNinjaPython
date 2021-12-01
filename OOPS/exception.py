class ZeroDenominatorError(Exception):
    pass


while True:
    try:
        n = int(input("Enter no "))
        m = int(input("second no "))
        if(m==0):
            raise ZeroDenominatorError("Denominator shounld not be zero")

        z = n/m
        print(z)
        break
    except ValueError:
        print("somthing wrong ")

    except ZeroDenominatorError:
        print("Zero nh hoga denominator")
    
    except ZeroDivisionError:
        print("not allowed 0 in denomintor")

    except:
        print("Pta nh knsi exception aayi bro... ")
    
    
