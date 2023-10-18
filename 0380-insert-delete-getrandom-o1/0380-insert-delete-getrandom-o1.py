import random

class RandomizedSet:
    def __init__(self):
        self.val_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False

        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        # Swap the value to remove with the last value in the list
        index_to_remove = self.val_to_index[val]
        last_value = self.values[-1]
        self.values[index_to_remove] = last_value
        self.val_to_index[last_value] = index_to_remove

        # Delete the value and its index
        del self.val_to_index[val]
        self.values.pop()
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
