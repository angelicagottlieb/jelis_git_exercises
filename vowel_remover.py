# File: lib/vowel_remover.py

class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] +  self.text[i+1:]
                #with this we carry on looking at same index position because something has been 
                #removed so everything shuffles around by 1
            else:
                i += 1
                #if not vowel this makes it move to next index 
        return self.text
remover = VowelRemover("We will remove the vowels from this sentence.")
print(remover.remove_vowels())
