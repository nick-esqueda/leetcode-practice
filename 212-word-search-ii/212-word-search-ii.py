class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode('')
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.is_word = True
        
    def delete(self, word):
        """
        if a node doesn't have any children other than the one you want to delete, you can delete it
        if the last node/end of word has children, just switch the is_word flag
        what to do if you accidentally pass in a word that doesn't exist?

        iterate downwards and collect a list of each node and their parents
        loop backwards through that list and if the node doesn't have any children, remove it from the parent's children map
        """
        nodes = [self.root]
        node = self.root
        for char in word:
            if char not in node.children:
                return
            node = node.children[char]
            nodes.append(node)
            
        i = len(nodes) - 1
        while i >= 1:
            node = nodes[i]
            parent = nodes[i - 1]
            if len(node.children) == 0:
                del parent.children[node.char]
            else:
                return
            i -= 1
        
    def __repr__(self):
        res = ''
        cur = self.root
        sta = [cur]
        while sta:
            cur = sta.pop()
            res += cur.char
            if cur.is_word:
                res += "\n"
            for child in cur.children:
                sta.append(cur.children[child])
        return res
            
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        if you create a prefix tree out of 'words', then you only have to scan through the board once
        scan through and look for one of the root's chldren, and once you're on one, start of a backtracking DFS
        during the DFS, you'll have to scan through both the board and the trie at the same time
        if you find the next child, move pointer down the tree, and recurse with the next node
        if the word is found, add to a result list
        after iterating through the whole board, return the result list, even if there's stuff in the trie
        
        how are you able to pop back up in the DFS and have the trie pointer move back?
        how will you delete the word from the trie after you find it?
            might not be the best way, but you can just change the is_word variable to mark it as done
        how will you know what word to push to found?
            maybe build a string as you recurse downwards?
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        found = set()
        for r in range(len(board)):
            for c in range(len(board[r])):
                board_char = board[r][c]
                if board_char in trie.root.children:
                    self.find_word(board, r, c, trie.root, [], found, set(), trie)
                   
        return found
                    
    def find_word(self, board, r, c, node, word, found, vis, trie):
        """
        if the board[r][c] != the node char, return false
        need to also pass in the node itself as you recurse down
        what should you be returning?
        should probably just be building the string as an array (for efficiency) as you go down
        once you find the end of the word, just append to found
        """
        if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0])):
            return
        board_char = board[r][c]
        if (r, c) in vis:
            return
        if board_char not in node.children:
            return
        
        vis.add((r, c))
        word.append(board_char)
        node = node.children[board_char]
        if node.is_word:
            full_word = ''.join(word)
            trie.delete(full_word)
            found.add(full_word)
        
        self.find_word(board, r - 1, c, node, word, found, vis, trie)
        self.find_word(board, r + 1, c, node, word, found, vis, trie)
        self.find_word(board, r, c - 1, node, word, found, vis, trie)
        self.find_word(board, r, c + 1, node, word, found, vis, trie)

        vis.remove((r, c))
        word.pop()
        return
    
    
    
    
    
    
    
    
    