import random
words=['father', 'enterprise', 'science', 'programming', 'resistance', 'fiction', 'condition', 'reverse', 'computer', 'python']
word=random.choice(words)
jumble="".join(random.sample(word,len(word)))
print("jumble:",jumble)
while True:
    guess=input("enter the word: ")
    guess=guess.lower()
    if guess==word:
        print("correct Guess")
        break
    else:
        print('wrong guess')