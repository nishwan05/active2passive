Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import spacy
... 
... # Load English NLP model
... nlp = spacy.load("en_core_web_sm")
... 
... def convert_to_passive(sentence):
...     doc = nlp(sentence)
...     
...     subject = ""
...     verb = ""
...     obj = ""
...     
...     for token in doc:
...         if token.dep_ == "nsubj":
...             subject = token.text
...         elif token.dep_ == "ROOT":
...             verb = token.lemma_
...         elif token.dep_ == "dobj":
...             obj = token.text
... 
...     if not subject or not obj or not verb:
...         return "❌ Unable to convert. Try a simple active sentence like 'John eats an apple.'"
... 
...     # Basic past tense check (not always accurate)
...     tense = "past" if any(tok.tag_ == "VBD" for tok in doc) else "present"
... 
...     if tense == "past":
...         aux = "was"
...     else:
...         aux = "is"
... 
...     # Basic verb regularization (for simple verbs)
...     if verb.endswith("e"):
...         past_participle = verb + "d"
...     else:
...         past_participle = verb + "ed"

    passive = f"{obj.capitalize()} {aux} {past_participle} by {subject}."
    return passive

# === Main Program ===
print("🎯 Active to Passive Voice Converter\n")
sentence = input("Enter an active voice sentence:\n> ")
converted = convert_to_passive(sentence)
print(f"\n🔁 Passive Voice:\n{converted}")
