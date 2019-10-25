import os
import prefix_tree
import pickle


class Dictionary:

    def __init__(self):
        self.trie = prefix_tree.Trie()
        self.hash_mean = dict()
        self.path_file_mean = "data/mean_word.bin"

    def loadStructure(self):
        with open("data/trie.pickle", "rb") as f:
            self.trie = pickle.load(f)
        with open("data/hash_mean.pickle", "rb") as f:
            self.hash_mean = pickle.load(f)

    def saveStructure(self):
        with open("data/trie.pickle", "wb") as f:
            pickle.dump(self.trie, f)
        with open("data/hash_mean.pickle", "wb") as f:
            pickle.dump(self.hash_mean, f)

    def addOneWord(self, word, mean):
        "Add one word to dictionary"
        self.trie.insertNode(word)
        with open(self.path_file_mean, "ab") as f:
            offset_start = f.tell()
            f.write(mean.encode('utf-8'))
            offset_end = f.tell()
        self.hash_mean[word] = (offset_start, offset_end)

    def deleteOneWord(self, word):
        "Delete one word in dictionary"
        self.trie.deleteWord(word)
        self.hash_mean.pop(word)

    def searchWord(self, word):
        "Search word"
        if not self.trie.searchNode(word):
            return False
        offset = self.hash_mean[word][0]
        len_mean = self.hash_mean[word][1] - offset
        with open(self.path_file_mean, 'rb') as f:
            f.seek(offset)
            mean_word = f.read(len_mean)
        return mean_word.decode('utf-8')

    def addWordInFile(self, path_file):
        "Add all word in file to dictionary"
        try:
            mean_file = open(self.path_file_mean, "ab")
            with open(path_file, "r") as f:
                for line in f:
                    word_mean = line.split(maxsplit=1)
                    self.trie.insertNode(word_mean[0])
                    offset_start = mean_file.tell()
                    mean_file.write(word_mean[1].encode('utf-8'))
                    offset_end = mean_file.tell()
                    self.hash_mean[word_mean[0]] = (offset_start, offset_end)
        finally:
            mean_file.close()


if __name__ == "__main__":
    my_dict = Dictionary()
    my_dict.loadStructure()
    print(my_dict.searchWord('hello'))