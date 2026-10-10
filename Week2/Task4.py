word = input("Enter a word: ")
word = word.lower()
for i in range(len(word)):
    if word[i]!= word[len(word)-1-i]:
        print(f"{word} is not a palindrome")
        break
else:
    print(f"{word} is a palindrome")
    
