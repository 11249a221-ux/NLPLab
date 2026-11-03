import nltk
sentence = "The teacher explains the lesson in the classroom."
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    PP: {<IN><NP>}
"""
chunker = nltk.RegexpParser(grammar)
tree = chunker.parse(tagged)
print("POS Tags:", tagged)
print("\nChunk Tree:")
print(tree)
print("\nIdentified Phrases:")
for subtree in tree.subtrees():
    if subtree.label() in ("NP", "PP"):
        print(subtree.label(), ":", " ".join(word for word, tag in subtree.leaves()))