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
        scan through and look for one of the root's chldren, and once you're on one, start backtracking DFS
        during the DFS, you'll have to scan through both the board and the trie at the same time
        recurse with the current node, and if the next position is in node.children, advance node, and keep going
        if the word is found, add to a result list, and delete word from trie so you don't go back down the same path
        after iterating through the whole board, return the result list, even if there's still stuff in the trie
        
        BACKTRACKING:
        if the board[r][c] not in node.children, return 
        need to also pass in the node itself as you recurse down
        the grid will lead
            recurse in all 4 directions first, and then see if that letter is in the node's children
            if so, keep going, but if not, you then know that you shouldn't go that direction
            it's as if the recursion is eager, but asks for permission before going too far
        should probably just be building the string as an array (for efficiency) as you go down
        once you find the end of the word, just append to found and delete the word from the trie
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        def find_word(r, c, node, word, vis):
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

            find_word(r - 1, c, node, word, vis)
            find_word(r + 1, c, node, word, vis)
            find_word(r, c - 1, node, word, vis)
            find_word(r, c + 1, node, word, vis)

            vis.remove((r, c))
            word.pop()
            return

        found = set()
        for r in range(len(board)):
            for c in range(len(board[r])):
                board_char = board[r][c]
                if board_char in trie.root.children:
                    find_word(r, c, trie.root, [], set())
                   
        return found
                    
    
    
    
    
    
    
    
    