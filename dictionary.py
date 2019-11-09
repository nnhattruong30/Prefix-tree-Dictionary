import os
import prefix_tree
import pickle


class Dictionary:

    def __init__(self):
        self.trie = prefix_tree.Trie()
        self.hash_mean = dict()
        self.path_file_mean = os.path.join('data', 'mean_word.bin')
        self.path_trie = os.path.join('data', 'trie.pickle')
        self.path_hash = os.path.join('data', 'hash_mean.pickle')
        if os.path.isfile(self.path_trie) and os.path.isfile(self.path_hash):
            self.loadStructure()

    def loadStructure(self):
        with open(self.path_trie, "rb") as f:
            self.trie = pickle.load(f)
        with open(self.path_hash, "rb") as f:
            self.hash_mean = pickle.load(f)

    def saveStructure(self):
        with open(self.path_trie, "wb") as f:
            pickle.dump(self.trie, f)
        with open(self.path_hash, "wb") as f:
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
            return ''
        offset = self.hash_mean[word][0]
        len_mean = self.hash_mean[word][1] - offset
        with open(self.path_file_mean, 'rb') as f:
            f.seek(offset)
            mean_word = f.read(len_mean)
        mean_word = mean_word.decode('utf-8')
        mean_word = mean_word.replace(r'\n', '\n')
        return mean_word

    def addWordInFile(self, path_file):
        "Add all word in file to dictionary"
        try:
            mean_file = open(self.path_file_mean, "wb")
            with open(path_file, "r", encoding='utf-8') as f:
                for line in f:
                    word_mean = line.split(maxsplit=1)
                    self.trie.insertNode(word_mean[0])
                    offset_start = mean_file.tell()
                    mean_file.write(word_mean[1].encode('utf-8'))
                    offset_end = mean_file.tell()
                    self.hash_mean[word_mean[0]] = (offset_start, offset_end)
        finally:
            mean_file.close()
    
    def getSuggestion(self, query):
        return self.trie.getAutoSuggestion(query)

if __name__ == "__main__":
    path_file_dataset = os.path.join('res', 'common-english-viet-words.txt')
    my_dict = Dictionary()
    my_dict.addWordInFile(path_file_dataset)
    my_dict.saveStructure()
    print("Add successfully.")