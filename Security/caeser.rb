def encode(string, number)
  return string.chars.map { |char| (char.ord+number).chr }.join
end

def decode(string, number)
  return string.chars.map { |char| (char.ord-number).chr }.join
end
  
if __FILE__==$0
  message = encode("Quick! Get to the choppa!", 5)
  puts message
  code = decode(message, 5)
  puts code
end