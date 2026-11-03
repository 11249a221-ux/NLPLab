import nltk
sentences = [
    "a student",
    "the very intelligent student"
]
grammar = r"""
    NP: {<DT>?<RB.*>*<JJ.*>*<NN.*>+}
"""
chunker = nltk.RegexpParser(grammar)
for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    tree = chunker.parse(tagged)
    print("\nSentence:", sentence)
    print("POS Tags:", tagged)
    print("Chunk Structure:", tree)