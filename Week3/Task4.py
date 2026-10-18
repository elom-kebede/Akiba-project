text = input("Enter your text: ")
text = text.lower()
text = text.replace(".","").replace(",","").replace("!","").replace("?","")


# count words 
def count_words(text):
    word = text.split()
    return len(word)
# print(count_words(text))

# count charachter 
def count_char(text):
    count = 0
    for char in text:
        if char != " ":
            count +=1
    return count
    
# count vowel and consonant
def vowelandConsonants(text):
    vowel = "aeiou"
    v_count = 0
    c_count = 0
    for char in text:
        if char in vowel:
            v_count += 1
        elif char.isalpha(): # to check it is alphabet
            c_count += 1
    return v_count, c_count

# To find the longest word
def longestWord(text):
    words = text.split()
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# counting the word that are reapted

def countreaptWord(text):
    words = text.split()
    repeatcount = {}
    for word in words:
        if word in repeatcount:
            repeatcount[word]+=1
        else:
            repeatcount[word]=1
    return repeatcount
repeatcount = countreaptWord(text)

repeatcount = countreaptWord(text)

def repeatWord(repeatcount):
    repeat = []
    for word in repeatcount:
        if repeatcount[word] > 1 :
            repeat.append(word)
    return repeat


def all_in_one(text):
    
    
    num_of_words = count_words(text)
    num_of_char = count_char(text)
    vowels, consonant = vowelandConsonants(text)
    longWord = longestWord(text)
    frequency = countreaptWord(text)
    repeatedWord = repeatWord(repeatcount)

    print(f"\nnum of word: {num_of_words}")
    print(f"num of charachter: {num_of_char}")
    print(f"num of vowel letters: {vowels}")
    print(f"num of consonant letters: {consonant}")
    print(f"The longest word is: {longWord}")
    print(f"num of repeated words: {frequency}")
    print(f"repeated words: {repeatedWord}")

all_in_one(text)
    


    



