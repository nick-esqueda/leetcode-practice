class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = Node("")

    def insert(self, word: str) -> None:
        """
        use a node pointer to iterate downards
        will be iterating over the word and down the tree at the same time
        if the node does not have a child of cur char, create new node and add it, then move on
        if child does have cur char as child, move pointers onwards
        once the loop breaks and you've inserted the whole word, mark the end as such
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        iterate downwards
        if the cur letter is not in children, return False
        if you break out of the loop and the node is_word, return True else False
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)