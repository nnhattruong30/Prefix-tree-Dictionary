
class Node:
    def __init__(self):
        self.children = {}
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
    
    def _printAllWord(self, node, word = ""):
        "Print all words in the Trie"
        if node.isEndOfWord:
            print(word)
        for ch in node.children:
            self._printAllWord(node.children[ch], word + ch)
    
    def display(self):
        "Display the content of the Trie"
        self._printAllWord(self.root)

    def isEmptyNode(self, root):
        "Returns true if root has no children, else false"
        return len(root.children) == 0 

    def removeNode(self, root, word, depth = 0):
        "Remove key in the trie"
        if (depth == len(word)): 
            if root.isEndOfWord:
                root.isEndOfWord = False
            if self.isEmptyNode(root):
                return word[depth-1]
            else: return False
        ch = word[depth]
        if ch in root.children:
            child_ch = self.removeNode(root.children[ch], word, depth + 1)
        else: return False
        if child_ch:
            root.children.pop(child_ch)
        if (self.isEmptyNode(root) and root.isEndOfWord == False):
            return ch
        return False
              
    def deleteWord(self, word):
        "Delete word in the Trie"
        self.removeNode(self.root, word)
        

if __name__ == "__main__":
    t = Trie()
    t.insertNode('abc')
    t.insertNode('abcd')
    t.insertNode('abcdg')
    t.insertNode('aefg')
    t.insertNode('akjc')
    t.display()
    t.deleteWord("abcdg")
    print()
    t.display()


    