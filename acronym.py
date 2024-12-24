def acronym(phrase):
    
    ignore_words = {"of", "and", "the"}
    
    words = phrase.split()
      
    acronym = "".join(word[0].upper() for word in words if word.lower() not in ignore_words)
    
    return acronym
if __name__ == "__main__":
    
    phrase = input("Enter a phrase to create an acronym: ").strip()
    
    acronym = acronym(phrase)
    
    print(f"\nThe acronym for '{phrase}' is: {acronym}")
