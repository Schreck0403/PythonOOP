import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    
    def __init__(self, file_path):
        """Initialize the WordFinder with a path to a file containing words."""
        self.words = self.read_words(file_path)
        print(f"{len(self.words)} words read")

    def read_words(self, file_path):
        """Read words from the specified file and return a list of words."""
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]

    def random(self):
        """Return a random word from the list of words."""
        return random.choice(self.words)

if __name__ == "__main__":
    wf = WordFinder("/Users/student/words.txt")

    for _ in range(5):
        print(wf.random())


class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words from a dictionary with handling comments and blank lines."""

    def read_words(self, file_path):
        """Read words from the specified file, excluding comments and blank lines, and return a list of words."""
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip() and not line.startswith('#')]

if __name__ == "__main__":
    wf = SpecialWordFinder("/Users/student/special_words.txt")

    for _ in range(5):
        print(wf.random())
