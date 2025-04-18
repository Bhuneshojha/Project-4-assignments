
print("📝 Let's play Mad Libs!")
print("You'll enter some words, and I'll create a silly story for you!")

noun = input("Enter a noun: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb (past tense): ")
place = input("Enter a place: ")
celebrity = input("Enter the name of a celebrity: ")


story = f"""
One day, a {adjective} {noun} was walking through {place}.
Suddenly, it {verb} in front of {celebrity}, who laughed and said,
"Wow, that was unexpected!"
And they became best friends forever. 🥰
"""

print("\n🎭 Here's your story:")
print(story)
