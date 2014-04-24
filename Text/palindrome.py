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
        
if __name__ == '__main__':
    print palindrome1('racecar')
    print palindrome1('nintendo')
    
    print palindrome2('racecar')
    print palindrome2('nintendo')