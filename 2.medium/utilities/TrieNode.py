from typing import List, Type


class TrieNode:
    def __init__(self):
        self.children: Type["TrieNode"] = [None] * 26
        self.isEndOfWord = False

    def _char2idx(self, ch: str) -> int:
        return ord(ch) - 97

    def _idx2char(self, idx: int) -> str:
        return chr(idx + 97)

    # Time Complexity:   O(len(key))
    # Memory Complexity: O(len(key))
    def insert(self, key: str) -> None:
        jumper = self
        n = len(key)
        for level in range(n):
            index = self._char2idx(key[level])
            if not jumper.children[index]:
                jumper.children[index] = TrieNode()
            jumper = jumper.children[index]
        jumper.isEndOfWord = True

    # Time Complexity:   O(len(key))
    # Memory Complexity: O(1)
    def search(self, key: str) -> bool:
        jumper = self
        n = len(key)
        for level in range(n):
            index = self._char2idx(key[level])
            if not jumper.children[index]:
                return False
            jumper = jumper.children[index]
        return jumper.isEndOfWord

    def add_from_arr(self, arr: List[str]) -> None:
        for word in arr:
            self.insert(word)

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

    def get_arr_from_prefix(self, prefix: str) -> List[str]:
        jumper = self
        n = len(prefix)
        for level in range(n):
            index = self._char2idx(prefix[level])
            if not jumper.children[index]:
                return False
            jumper = jumper.children[index]
        return [prefix + rest for rest in jumper.get_arr_of_all()]


word_list = [
    "ap",
    "apple",
    "banana",
    "apricot",
    "ball",
    "cat",
    "dog",
    "apartment",
    "bat",
    "carrot",
    "doghouse",
]

prefix = "ap"

trie = TrieNode()
trie.add_from_arr(word_list)
print(trie.get_arr_of_all())
print(trie.children)
print(trie.search("da"))
print(trie.search("carrot"))
print(trie.get_arr_from_prefix(prefix))
