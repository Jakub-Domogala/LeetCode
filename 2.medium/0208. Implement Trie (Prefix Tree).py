# this one is actually pure laziness
# I took functions from my previously implemented TrieNode.py class
# appropriate solution could have been a bit better optimized when it comes to 'startsWith' function

from typing import List, Type


class Trie:
    def __init__(self):
        self.children: Type["Trie"] = [None] * 26
        self.isEndOfWord = False

    def _char2idx(self, ch: str) -> int:
        return ord(ch) - 97

    def _idx2char(self, idx: int) -> str:
        return chr(idx + 97)

    def insert(self, word: str) -> None:
        word = "".join(char for char in word.lower() if char.islower())
        jumper = self
        n = len(word)
        for level in range(n):
            index = self._char2idx(word[level])
            if not jumper.children[index]:
                jumper.children[index] = Trie()
            jumper = jumper.children[index]
        jumper.isEndOfWord = True

    def search(self, word: str) -> bool:
        word = "".join(char for char in word.lower() if char.islower())
        jumper = self
        n = len(word)
        for level in range(n):
            index = self._char2idx(word[level])
            if not jumper.children[index]:
                return False
            jumper = jumper.children[index]
        return jumper.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        prefix = "".join(char for char in prefix.lower() if char.islower())
        jumper = self
        n = len(prefix)
        for level in range(n):
            index = self._char2idx(prefix[level])
            if not jumper.children[index]:
                return False
            jumper = jumper.children[index]
        return len([prefix + rest for rest in jumper.get_arr_of_all()]) > 0

    def get_arr_of_all(self) -> List[str]:
        result = []
        if self.isEndOfWord:
            result.append("")
        for idx, child in enumerate(self.children):
            part_result = []
            if child:
                part_result += child.get_arr_of_all()
            for i in range(len(part_result)):
                part_result[i] = self._idx2char(idx) + part_result[i]
            result += part_result
        return result


# trie = Trie()
# trie.insert("apple")
# print(trie.search("apple"))  # return True
# print(trie.search("app"))  # return False
# print(trie.startsWith("app"))  # return True
# trie.insert("app")
# print(trie.search("app"))  # return True
