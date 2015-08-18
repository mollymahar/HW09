x = 0
y = 1
names = ["Guido"]
try:
    # this
    # print names[y]
    # ans = 3/x
    if x < 2:
        raise ValueError("this function requires x >= 2")
    pass
except IndexError:
    print("You attempted to use an index larger than our list of names.")
    print("You attempted: {0} Highest Index: {1}".format(y, len(names)-1))
except NameError as e:
    print("Debug Note: we haven't defined *this* yet.")
except ZeroDivisionError as e:
    print("x cannot be zero: you just attempted {0}".format(e))
except ValueError as e:
    print("Raised ValueError:{e}".format(e=e))
except Exception as e:
    print("I wasn't prepared for this:")
    print(type(e), e)

while True:
    try:
        test = raw_input(">")
        if test == "done":
            break
    except Exception:               # Exception doesn't catch CTRL + C, whereas a naked except also counts CTRL + C as an exception
        print("\nTry again:")
    # except:
    #     print("\nTry again:")