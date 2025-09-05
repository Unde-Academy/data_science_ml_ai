def word_count(sentence):
    sentence = sentence.lower().split()  # Make everything lowercase and split words
    word_counts = {}  # Store word counts
    
    for word in sentence:
        word = ''.join(c for c in word if c.isalnum())  # Remove punctuation
        # isalnum() - checks if it is a letter or a number
        if word:  # If word is not empty
            word_counts[word] = word_counts.get(word, 0) + 1  # Count words
    
    for word, count in word_counts.items():
        print(f"{word} => {count}")

# Test it
text = "The book was stolen. it was my book."
word_count(text)
