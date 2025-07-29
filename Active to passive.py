import spacy
nlp = spacy.load("en_core_web_sm")

def convert_to_passive(sentence):
    doc = nlp(sentence)
    subject = ""
    verb = ""
    obj = ""
    for token in doc:
        if token.dep_ == "nsubj":
            subject = token.text
        elif token.dep_ == "ROOT":
            verb = token.lemma_
        elif token.dep_ == "dobj":
            obj = token.text
    if not subject or not obj or not verb:
        return "❌ Unable to convert. Try a simple active sentence like 'John eats an apple.'"
    tense = "past" if any(tok.tag_ == "VBD" for tok in doc) else "present"
    aux = "was" if tense == "past" else "is"
    if verb.endswith("e"):
        past_participle = verb + "d"
    else:
        past_participle = verb + "ed"
    passive = f"{obj.capitalize()} {aux} {past_participle} by {subject}."
    return passive

print("🎯 Active to Passive Voice Converter\n")
sentence = input("Enter an active voice sentence:\n> ")
converted = convert_to_passive(sentence)
print(f"\n🔁 Passive Voice:\n{converted}")
