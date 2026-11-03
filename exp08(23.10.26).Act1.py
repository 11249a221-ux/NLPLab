import nltk
sentence = "Ravi plays cricket every evening"
tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)
print("Word\tPOS Tag")
print("-" * 25)
for word, tag in tagged_words:
    print(f"{word}\t{tag}")

