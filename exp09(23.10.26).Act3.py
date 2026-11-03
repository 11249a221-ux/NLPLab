import nltk
sentence = "The young researcher develops an AI model."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""
chunker = nltk.RegexpParser(grammar)
tree = chunker.parse(tagged)
print("POS Tagged Sequence:")
print(tagged)
print("\nChunked Sentence:")
print(tree)
print("\nNoun Phrases:")
for subtree in tree.subtrees():
    if subtree.label() == "NP":
        print(" ".join(word for word, tag in subtree.leaves()))