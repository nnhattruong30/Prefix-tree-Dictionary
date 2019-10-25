import os
import prefix_tree
import pickle


class Dictionary:

    def __init__(self):
        self.trie = prefix_tree.Trie()
        self.hash_mean = dict()
        self.path_file_mean = "data/mean_word.bin"
    
    def loadStructure(self):
        pass

    def dumpStructure(self):
        with open("data/trie.pickle", "rb") as f:
            
    
    def addOneWord(self, word, mean):
        "Add one word to dictionary"
        node = self.trie.insertNode(word)
        mean_value = node.getMeanValue()
        with open(self.path_file_mean, "ab") as f:
            offset_start = f.tell()
            f.write(mean.encode('utf-8'))
            offset_end = f.tell()
        self.hash_mean[mean_value] = (offset_start, offset_end)
        
    def deleteOneWord(self, word):
        "Delete one word in dictionary"
        self.trie.deleteWord(word)
    
    def searchWord(self, word):
        "Search word"
        node = self.trie.searchNode(word)
        if not node: return None
        key = node.getMeanValue()
        value_offset = self.hash_mean[key]
        offset_start = value_offset[0]
        len_mean_word = value_offset[1] - value_offset[0]
        with open(self.path_file_mean, "rb") as f:
            f.seek(offset_start)
            mean_word = f.read(len_mean_word)
        mean_word = mean_word.decode("utf-8")
        return (word, mean_word)

    def addWordInFile(self, path_file):
        "Add all word in file to dictionary"
        try:
            mean_file = open(self.path_file_mean, "ab")
            with open(path_file, "r") as f:
                for line in f:
                    word_mean  = line.split( maxsplit=1)
                    node = self.trie.insertNode(word_mean[0])
                    offset_start = mean_file.tell()
                    mean_file.write(word_mean[1].encode('utf-8'))
                    offset_end = mean_file.tell()
                    self.hash_mean[node.getMeanValue()] = (offset_start, offset_end)
        finally:
            mean_file.close()

        
if __name__ == "__main__":
    my_dict = Dictionary()
    path = "data/common-english-viet-words.txt"
    my_dict.addWordInFile(path)