def word_counter(text):
    # Split the text into words
    words = text.split()

    # Count the number of words
    word_count = len(words)

    return word_count

# Input text
input_text = input("Enter a sentence or paragraph: ")

# Calculate and display word count
count = word_counter(input_text)
print(f"Word Count: {count")
