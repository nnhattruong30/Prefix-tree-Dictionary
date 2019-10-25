import pickle
class Node:
    def __init__(self):
        self.children = dict()
        self.isEndOfWord = False

class Trie:
    "Trie data structure class"
    def __init__(self):
        self.root = self.getNode()
    
    def getNode(self):
        "Return new node (initialized to NULL)"
        return Node()
    
    def insertNode(self, word):
        "Insert key into trie"
        pNode = self.root
        for ch in word:
            if ch in pNode.children:
                pNode = pNode.children[ch]
            else:
                newNode = self.getNode()
                pNode.children[ch] = newNode
                pNode = newNode
        pNode.isEndOfWord = True
        return pNode

    def searchNode(self, word):
        "Search key in the trie"
        pNode = self.root

        for ch in word:
            if ch not in pNode.children:
                return False
            pNode = pNode.children[ch]

        if pNode.isEndOfWord:
            return pNode
        return False
    
    def _print(self, node, word = ""):
        "Print all words in the Trie"
        if node.isEndOfWord:
            print(word)
        for ch in node.children:
            self._print(node.children[ch], word + ch)
    
    def printAllWord(self):
        "Display the content of the Trie"
        self._print(self.root)

    def isEmptyNode(self, root):
        "Returns true if root has no children, else false"
        return len(root.children) == 0 

    def _deleteNode(self, root, word, depth = 0):
        "Remove key in the trie"
        if (depth == len(word)): 
            if root.isEndOfWord:
                root.isEndOfWord = False
            if self.isEmptyNode(root):
                return word[depth-1]
            else: return False
        ch = word[depth]
        if ch in root.children:
            child_ch = self._deleteNode(root.children[ch], word, depth + 1)
        else: return False
        if child_ch:
            root.children.pop(child_ch)
        if (self.isEmptyNode(root) and root.isEndOfWord == False):
            return ch
        return False
              
    def deleteWord(self, word):
        "Delete word in the Trie"
        self._deleteNode(self.root, word)
    
    def _suggestionRec(self, root, word, word_list):
        if root.isEndOfWord:
            word_list.append(word)
        for ch, node in root.children.items():
            self.suggestionRec(node, word + ch, word_list)

    def getAutoSuggestion(self, query):
        pNode = self.root
        for ch in query:
            if ch not in pNode.children:
                return False
            pNode = pNode.children[ch]
        word_list = []
        self._suggestionRec(pNode, query, word_list)
        return word_list
        
if __name__ == "__main__":
    t = Trie()
    t.insertNode("hello")
    t.insertNode("hell")
    t.insertNode("help")
    t.insertNode("helps")
    t.insertNode("helping")
    t.insertNode("dog")
    t.getAutoSuggestion('hello')
    