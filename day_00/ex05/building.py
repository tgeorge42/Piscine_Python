import sys

def building(text: str) -> None:
    """Prints the number of characters in the given string,\nas well as the number of upper and lower case letters,\npunctuation marks, spaces and digits."""
    
    print("The text contains " + str(len(text)) + " characters:")
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punctuation = sum(1 for c in text if c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    spaces = sum(1 for c in text if c.isspace())
    digits = sum(1 for c in text if c.isdigit())
    print(str(upper) + " upper letters")
    print(str(lower) + " lower letters")
    print(str(punctuation) + " punctuation marks")
    print(str(spaces) + " spaces")
    print(str(digits) + " digits")

def main():
    print(building.__doc__)
    try:
        if len(sys.argv) > 2:
            raise AssertionError("Too many arguments")
        elif len(sys.argv) == 2 and sys.argv[1] != "None":
            building(sys.argv[1])
        else:
            try:
                arg = input("Enter a string: ")
            except EOFError:
                return 1
            except KeyboardInterrupt:
                return 1
            building(arg)
    except AssertionError as e:
        if str(e) == "No argument given":
            print("\n" + type(e).__name__ + ":", e)
        else:
            print(type(e).__name__ + ":", e)
        sys.exit(1)
    
if __name__ == "__main__":
    main()