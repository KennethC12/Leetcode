# Big O Notation

# Add: O(1)
# Get: O(1)
# Remove: O(1)

class HashMap:
    def __init__(self, size):
        self.size = size
        self.map = [None] * size

    def _get_hash(self, key):
        """Generates a hash index for a given key."""
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        """Adds a key-value pair to the hash map."""
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value  # Update value if key already exists
                    return
            self.map[key_hash].append(key_value)  # Handle collision

    def get(self, key):
        """Retrieves the value associated with a key."""
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None  # Key not found

    def remove(self, key):
        """Removes a key-value pair from the hash map."""
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)  # Remove the key-value pair
                if len(self.map[key_hash]) == 0:
                    self.map[key_hash] = None  # Clean up empty bucket
                return True
        return False  # Key not found

    def print_map(self):
        """Prints the contents of the hash map."""
        for i, bucket in enumerate(self.map):
            if bucket is not None:
                print(f"Bucket {i}: {bucket}")
            else:
                print(f"Bucket {i}: Empty")
