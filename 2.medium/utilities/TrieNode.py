from typing import List, Type


# This class uses only lowercase letters as keys.
# Every string is converted so that:
#   all letters are converted to lowercase
#   all non letter characters are removed
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
        key = "".join(char for char in key.lower() if char.islower())
        jumper = self
        n = len(key)
        for level in range(n):
            index = self._char2idx(key[level])
            if not jumper.children[index]:
                jumper.children[index] = TrieNode()
            jumper = jumper.children[index]
        jumper.isEndOfWord = True

    # Time Complexity:   O(len(key))
    # Memory Complexity: O(len(key))
    def delete(self, key: str) -> None:
        key = "".join(char for char in key.lower() if char.islower())
        n = len(key)

        def dive_delete(node, idx):
            if node is None:
                return True
            if idx == n:
                node.isEndOfWord = False
                if len([x for x in node.children if x]) == 0:
                    return True
                else:
                    return False
            if dive_delete(node.children[self._char2idx(key[idx])], idx + 1):
                node.children[self._char2idx(key[idx])] = None
            return len([x for x in node.children if x]) == 0 and not node.isEndOfWord

        dive_delete(self, 0)

    # Time Complexity:   O(len(key))
    # Memory Complexity: O(1)
    def search(self, key: str) -> bool:
        key = "".join(char for char in key.lower() if char.islower())
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
        prefix = "".join(char for char in prefix.lower() if char.islower())
        jumper = self
        n = len(prefix)
        for level in range(n):
            index = self._char2idx(prefix[level])
            if not jumper.children[index]:
                return False
            jumper = jumper.children[index]
        return [prefix + rest for rest in jumper.get_arr_of_all()]


# word_list = [
#     "ap",
#     "apple",
#     "Banana",
#     "apricot",
#     "ball",
#     "cat",
#     "dog",
#     "apartment",
#     "bat",
#     "carrot",
#     "doghouse",
# ]

# prefix = "ap"

# trie = TrieNode()
# trie.add_from_arr(word_list)
# print(trie.search("da"))
# print(trie.search("carrot"))
# print(trie.get_arr_from_prefix(prefix))
# print(trie.get_arr_of_all())
# trie.delete("apple")
# print(trie.get_arr_of_all())
