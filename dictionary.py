import os
import prefix_tree



class Dictionary:

    def __init__(self):
        self.trie = prefix_tree.Trie()
        self.hash_mean = dict()
        self.path_file_mean = "data/mean.bin"
    
    def 