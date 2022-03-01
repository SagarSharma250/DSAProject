def checkPalindrome(str):
    if len(str) < 1:
        return True
    else:
        if str[0] == str[-1]:
            return checkPalindrome(str[1:-1])
        else:
            return False


    return False