def count_words_in_file(filename):
    # Counts the number of words in the given text file.
    with open(filename, 'r') as file:
        content = file.read()
        # Split the content into words
        words = content.split()  
        # Return the word count
        return len(words)  

if __name__ == "__main__":
    word_count = count_words_in_file('task6_read_me.txt')
    print(f"Number of words in task6_read_me.txt: {word_count}")