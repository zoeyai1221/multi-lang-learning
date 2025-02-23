from my_queue import myQueue
from stack import Stack


# Magic number replacement
NUM_ZERO = 0
NUM_ONE = 1


class WordLadder:
    """A class providing functionality to create word ladders
    between words of varying lengths"""
    def __init__(self, w1, w2, wordlist):
        self.start_word = w1
        self.end_word = w2
        self.wordlist = wordlist
        self.queue = myQueue()
        self.visited = set()

        initial_stack = Stack()
        initial_stack.push(w1)
        self.queue.enqueue(initial_stack)

    def one_letter_apart(self, word1, word2):
        """Check if two words are one letter apart
        or have an insertion/deletion"""
        if word1 == word2:
            return False

        len_word1 = len(word1)
        len_word2 = len(word2)

        if abs(len_word1 - len_word2) == NUM_ONE:
            # If lengths differ by 1, check for insertion/deletion
            shorter_word, longer_word = (
                word1, word2) if len_word1 < len_word2 else (word2, word1
                                                             )

            i = j = NUM_ZERO
            found_difference = False

            while i < len(shorter_word) and j < len(longer_word):
                if shorter_word[i] != longer_word[j]:
                    if found_difference:
                        return False
                    found_difference = True
                    if len_word1 < len_word2:
                        j += NUM_ONE  # Move pointer in the longer word
                    else:
                        i += NUM_ONE  # Move pointer in the shorter word
                else:
                    i += NUM_ONE
                    j += NUM_ONE

            return True

        return False

    def make_ladder(self):
        """Generate the stack of ladder"""
        while not self.queue.isEmpty():
            current_stack = self.queue.dequeue()
            current_word = current_stack.peek()

            if current_word == self.end_word:
                return current_stack

            if current_word not in self.visited:
                self.visited.add(current_word)

                # Fetch words of specific length
                for next_word in self.wordlist[len(current_word)]:
                    if self.one_letter_apart(current_word, next_word):
                        new_stack = current_stack.copy()
                        new_stack.push(next_word)
                        self.queue.enqueue(new_stack)

                if len(current_word) + NUM_ONE <= len(self.end_word):
                    # Allow insertion of a character to current_word
                    for i in range(len(current_word) + NUM_ONE):
                        for char in 'abcdefghijklmnopqrstuvwxyz':
                            new_word = current_word[:i] + \
                                char + current_word[i:]
                            if (
                                new_word in self.wordlist[len(new_word)] and
                                new_word not in self.visited
                            ):
                                new_stack = current_stack.copy()
                                new_stack.push(new_word)
                                self.queue.enqueue(new_stack)

                if len(current_word) - NUM_ONE >= len(self.start_word):
                    # Allow deletion of a character from current_word
                    for i in range(len(current_word)):
                        new_word = current_word[:i] + \
                            current_word[i + NUM_ONE:]
                        if (
                            new_word in self.wordlist[len(new_word)] and
                            new_word not in self.visited
                        ):
                            new_stack = current_stack.copy()
                            new_stack.push(new_word)
                            self.queue.enqueue(new_stack)

        return None
