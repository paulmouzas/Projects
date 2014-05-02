from pprint import pprint
vowels = "aeiou"
sentence = "here is a sentence with a bunch of vowels"

vowels_in_sentence = filter(lambda x: x in vowels, sentence)

report = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

for char in vowels_in_sentence:
    report[char] += 1
    
print "Number of vowels: %s" % len(vowels_in_sentence)
print "Vowel report: %s" % report