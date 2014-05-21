Vowels = ['a','e','i','o','u']

def pig_latin(sentence)
  words = sentence.split
  words.map! do |word|
    if Vowels.include? word[0]
      word + 'ay'
    else
      first = word.slice!(0)
      word + first + 'ay'
    end
  end
  return words.join ' '
end

if __FILE__==$0
  sentence = pig_latin("it's never lupus")
  puts sentence
end
