"""
Check if Palindrome - Checks if the string entered
by the user is a palindrome. That is that it reads
the same forwards as backwards like "racecar"
"""

def palindrome1(word):
    backwards = word[::-1]
    if word == backwards: return True 
    else: return False


def palindrome2(word):
    if len(word) <=3:
        if word[0] == word[-1]:
            return True
        else:
            return False
    else:
        return palindrome2(word[1:-1])
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))
    
if __name__ == '__main__':
    test(palindrome1('racecar'), True)
    test( palindrome1('nintendo'), False)
    
    test(palindrome2('racecar'), True)
    test(palindrome2('nintendo'), False)

