class Node:
    "Trie node class"
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        self.meanWord = -1

class Trie:
    "Trie data structure class"
    _countNode = 0

    def __init__(self):
        self.root = self.getNode()
    
    def getNode(self):
        "Return new node (initialized to NULL)"
        return Node()
    
    def _charToIndex(self, ch):
        "Converts key current character into index"
        return (ord(ch)- ord('a'))
    
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
        pNode.meanWord = Trie._countNode
        Trie._countNode += 1

    def searchNode(self, word):
        "Search key in the trie"
        pNode = self.root
        length = len(word)
        
        for level in range(length):
            index = self._charToIndex(word[level])
            if not pNode.children[index]:
                return False
            pNode = pNode.children[index]

        return pNode != None and pNode.isEndOfWord == True

    def deleteNode(self, word):
        "Delete key in the trie"
        

if __name__ == "__main__":
    t = Trie()
    