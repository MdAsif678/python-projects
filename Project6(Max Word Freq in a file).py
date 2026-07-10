import string


def max_word_freq(filename):
    """This function returns the most frequent word and its occurrence count in a file."""
    frequency = {}
    try:
        with open(filename,"r") as file:
            for line in file:
                for word in line.split():
                    word = word.lower().strip(string.punctuation)
                
                    if word:
                        frequency[word] = frequency.get(word,0)+1

            if not frequency:
                return None
            
            most_freq_word = max(frequency,key = frequency.get)
            return most_freq_word, frequency[most_freq_word] 
    except FileNotFoundError:
        print("File not found")
        return None


result = max_word_freq("context.txt")

if result:
    word, count = result
    print(f"The word with most frequency is-> {word}:{count}")

print(max_word_freq.__doc__)
