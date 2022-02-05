def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number -1) + fibonacci(number - 2)


def palindrome(sentence):
    """Return true if sentence is a palindrome
    otherwise return False

    sentence -- String or integer

    >>> palindrome("anita lava la tina")
    True

    >>> palindrome(12321)
    True

    >>> palindrome("EasyCode")
    True

    """

    sentence = str(sentence).lower().replace(" ", "")
    return sentence == sentence[::-1]
   
