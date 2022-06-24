class Node:
    def __init__(self):
        # self.char = char
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        if the char is a dot, need to go search through all children
        can maybe do this recursively, throwing in the rest of the word
        iterate through word normally for letters that aren't '.'
        for '.', make recursive call, passing in each possible child
        """
        def backtrack(node, i):
            while i < len(word) and word[i] in node.children:
                node = node.children[word[i]]
                i += 1
            if i == len(word):
                return node.is_word
            if word[i] == ".":
                for child in node.children:
                    if backtrack(node.children[child], i + 1):
                        return True
            return False
                
        return backtrack(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)