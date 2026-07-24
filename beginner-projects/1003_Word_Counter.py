def counter(filename):
    """Counts the number of lines, words, letters and any extras stuff in the file"""

    try:
        with open(filename) as f:
            frequency = {}
            word_count = 0
            letter_count = 0
            line_count = 0
            extras_count = 0
            for lines in f:
                word_count += len(lines.split())
                
                for letter in lines:
                    if letter.isalpha():
                        letter_count += 1
                    
                    else:
                        extras_count += 1

                line_count += 1
            
            frequency["words"] = word_count
            frequency["letters"] = letter_count
            frequency["Lines"] = line_count
            frequency["extras"] = extras_count
        
        return frequency
    
    except FileNotFoundError:
        print("No such file exists")


print(counter("context.txt"))
print(counter.__doc__)