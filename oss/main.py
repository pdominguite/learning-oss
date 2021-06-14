import sys

def square(n) -> float:
    """
    Calculates the square of an float number.

    Args:
        number: the float number to be squared.

    Returns:
        The squared number.
    """

    return n*n

def main(args) -> None:
    """
    Application entrypoint.
    """
    if len(sys.argv) != 2:
        raise Exception("You must provide exactly one float argument. " + 
                        "You have provided " + 
                        str(len(sys.argv) - 1) + " argument(s).")

    number = float(sys.argv[1])
    
    print(square(number))
    

if __name__ == '__main__':
    try:
        main(sys.argv)
        
    except Exception as err:
        print("An error occured: " + str(err))