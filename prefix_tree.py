
ALPHABET_SIZE = 26
class Node:
    "Trie node class"
    def __init__(self):
        self.children = [None] * ALPHABET_SIZE
        self.isEndOfWord = False
        self.meanValue = -1
    
    def getMeanValue(self):
        return self.meanValue

class Trie:
    "Trie data structure class"
    _countWord = 0

    def __init__(self):
        self.root = self.getNode()
    
    def getNode(self):
        "Return new node (initialized to NULL)"
        return Node()
    
    def _charToIndex(self, ch):
        "Converts key current character into index"
        return (ord(ch)- ord('a'))
    
    def _indexToChar(self, index):
        "Converts index into character"
        return(chr(index + ord('a')))

    def insertNode(self, word):
        "Insert key into trie"
        pNode = self.root
        length = len(word)
        
        for level in range(length):
            index = self._charToIndex(word[level])
            if not pNode.children[index]:
                pNode.children[index] = self.getNode()
            pNode = pNode.children[index]
        
        pNode.isEndOfWord = True
        pNode.meanValue = Trie._countWord
        Trie._countWord += 1
        return pNode

    def searchNode(self, word):
        "Search key in the trie"
        pNode = self.root
        length = len(word)
        
        for level in range(length):
            index = self._charToIndex(word[level])
            if not pNode.children[index]:
                return None
            pNode = pNode.children[index]

        if (pNode != None and pNode.isEndOfWord):
            return pNode
        return None
    
    def _printAllWord(self, node, word = ""):
        "Print all words in the Trie"
        if node.isEndOfWord:
            print(word)
        for i in range(ALPHABET_SIZE):
            if node.children[i]:
                word += self._indexToChar(i)
                self._printAllWord(node.children[i], word)
    
    def display(self):
        "Display the content of the Trie"
        self._printAllWord(self.root)

    def isEmptyNode(self, root):
        "Returns true if root has no children, else false"
        for i in range(ALPHABET_SIZE):
            if not root.children[i]:
                return False
        return True

    def removeNode(self, root, word, depth = 0):
        "Remove key in the trie"
        if not root:
            return None
        if depth == len(word):
            if root.isEndOfWord:
                root.meanValue = -1
                root.isEndOfWord = False
            if self.isEmptyNode(root):
                root = None
            return root
        
        index = self._charToIndex(word[depth])
        root.children[index] = self.removeNode(root.children[index], word, depth + 1)
        if (self.isEmptyNode(root) and root.isEndOfWord == False):
            root = None
        return root
    
    def deleteWord(self, word):
        "Delete word in the Trie"
        self.removeNode(self.root, word)
        

if __name__ == "__main__":
    t = Trie()
    y = t.insertNode("adidas")
    t.insertNode("abcd")
    x = t.insertNode("abc")
    t.display()
    print(t.searchNode("abcdd"))

    