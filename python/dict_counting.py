def word_count(sentence):
  count={}
  words = sentence.split()
  
  for word in words:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
    
  return count

print(word_count("the cat and the hat and the bat"))


def char_count(word):
    count={}
    for character in word:
      if character in count:
         count[character]+=1
      else:
         count[character]=1
    return count

print(char_count("banana"))
