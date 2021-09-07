try:
    x=int(input("enter any number with in 30:"))
    assert x<30
    print ("number is valid")
except AssertionError:
    print("invalid input")
    