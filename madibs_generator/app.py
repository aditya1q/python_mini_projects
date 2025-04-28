# Open and read the story
with open("story.txt", "r") as f:
    story = f.read()

# Find all the placeholders like <place>, <noun>, etc.
words = []
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    elif char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        if word not in words:
            words.append(word)
        start_of_word = -1

# Ask the user to replace each placeholder
answers = {}

for word in words:
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer

# Replace placeholders with the answers
for word in words:
    story = story.replace(word, answers[word])

# Show the final story
print("\nYour final story:\n")
print(story)
