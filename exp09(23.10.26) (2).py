import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentence = "The intelligent student reads a book in the library."
tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)
print("POS Tagged Words:")
print(tagged_words)
grammar = r"""
    NP: {<DT>?<JJ>*<NN.*>}
    VP: {<VB.*><DT>?<JJ>*<NN.*>*}
    PP: {<IN><NP>}
"""
chunk_parser = nltk.RegexpParser(grammar)
chunk_tree = chunk_parser.parse(tagged_words)
print("\nChunk Tree:")
print(chunk_tree)
print("\nPhrase Boundaries:")
for subtree in chunk_tree.subtrees():
    if subtree.label() != 'S':
        print(subtree.label(), ":", " ".join(word for word, tag in subtree.leaves()))
chunk_tree.pretty_print()
