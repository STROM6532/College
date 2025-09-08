# palindrome.py

# Get input from user
text = input("Enter a word or number: ")

# Remove spaces and convert to lowercase for uniformity
cleaned_text = text.replace(" ", "").lower()

# Check if cleaned_text is equal to its reverse
if cleaned_text == cleaned_text[::-1]:
    print(f'"{text}" is a palindrome.')
else:
    print(f'"{text}" is not a palindrome.')
