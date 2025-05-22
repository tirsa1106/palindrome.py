import string

def palindrome(s: str) -> bool:

    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


examples = [
    "Do geese see God?",
    "Was it Eliot's toilet I saw?",
    "Yo, Banana Boy!",
    "Red roses run no risk, sir, on Nurse's order.",
    "Sir, I demand, I am a maid named Iris.",
    "Palindromes are fun to find.",
    "The quick brown fox jumps over the lazy dog.",
    "Artificial intelligence is powerful.",
    "I love learning new things!",
    "Python is a great programming language."
]

for text in examples:
    print(f'"{text}" -> {palindrome(text)}')