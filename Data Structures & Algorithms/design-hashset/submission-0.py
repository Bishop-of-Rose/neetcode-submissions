class MyHashSet:
    def __init__(self):
        self.store = []

    def add(self, key: int) -> None:
        for i in self.store:
            if i == key:
                return
        self.store = self.store + [key]
        return

    def remove(self, key: int) -> None:
        for i in range(len(self.store)):
            if self.store[i] == key:
                self.store.pop(i)
                return
        return

    def contains(self, key: int) -> bool:
        for i in self.store:
            if i == key:
                return True
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)