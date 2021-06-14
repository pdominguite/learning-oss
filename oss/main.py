import sys

def square(n) -> int:
    """
    Calculates the square of an integer number.

    Args:
        number: the integer number to be squared.

    Returns:
        The squared number.
    """
    return n*n

def main(args) -> None:
    """
    Application entrypoint.
    """
    if len(sys.argv) != 2:
        raise Exception("You must provide exactly one integer argument. " + 
                        "You have provided " + 
                        str(len(sys.argv) - 1) + " argument(s).")

    number = int(sys.argv[1])
    
    print(square(number))
    

if __name__ == '__main__':
    try:
        main(sys.argv)
        
    except Exception as err:
        print("An error occured: " + str(err))