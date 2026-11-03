import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
sentences = [
    "The children are playing outside.",
    "She writes beautiful poems.",
    "They visited the library yesterday."
]
for sentence in sentences:
    print("\nSentence:", sentence)
    tokens = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(tokens)
    print("Word\t\tPOS Tag\t\tClassification")
    print("-" * 45)
    for word, tag in tagged_words:
        if tag.startswith("NN"):
            category = "Noun"
        elif tag.startswith("VB"):
            category = "Verb"
        elif tag.startswith("JJ"):
            category = "Adjective"
        elif tag.startswith("RB"):
            category = "Adverb"
        elif tag.startswith("PRP"):
            category = "Pronoun"
        elif tag == "DT":
            category = "Determiner"
        else:
            category = "Other"

        print(f"{word:<15}{tag:<15}{category}")
