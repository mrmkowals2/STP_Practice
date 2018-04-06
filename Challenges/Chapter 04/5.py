def string_to_float():
    """
    Takes a string representing a floating point
    number and returns as type float - else returns
    error message
    """
    x = input("Enter a floating point number: ")
    try:
        x = float(x)
        print(x)
    except:
        print("Input cannot be converted to type float.")

string_to_float()
