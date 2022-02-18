class TrieNode:
    def __init__(self, val=None, is_end=False):
        self.links = {}
        self.val = val
        self.is_end = is_end

    def contains(self, char):
        if char in self.links:
            if char in self.links:
                return True
            else:
                return False

    def put(self, char):
        if char not in self.links:
            self.links[char] = TrieNode(char)
        return self.links[char]

    def get(self, char):
        return self.links[char]

    def set_end(self):
        self.is_end = True


class Trie:

    def __init__(self):
        self.head = TrieNode("head")

    def insert(self, word: str) -> None:
        node = self.head
        for i in range(len(word)):
            if not node.contains(word[i]):
                node.put(word[i])
            node = node.get(word[i])
            if i == len(word) - 1:
                node.set_end()

    def search(self, word: str) -> bool:
        node = self.head
        for i in word:
            if node.contains(i):
                node = node.get(i)
            else:
                return False
        if node.is_end:
            return True
        return False

    def starts_with(self, prefix: str) -> bool:
        node = self.head
        for i in prefix:
            if node.contains(i):
                node = node.get(i)
            else:
                return False
        return True



if __name__ == '__main__':
    trie = Trie()
    print("********** Search **********")
    trie.insert("alexander")
    print(trie.search("alex"))
    trie.insert("alex")
    print(trie.search("alex"))
    print(trie.search("base"))
    trie.insert("ate")
    print(trie.search("ate"))
    trie.insert("ball")
    print("********** Starts With **********")
    print(trie.starts_with("ale"))
    print(trie.starts_with("app"))
