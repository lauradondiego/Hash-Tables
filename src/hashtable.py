# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity # the actual values being placed in the buckets
        self.count = 0  # added this

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        print("key/value:", key, value)
        index = self._hash_mod(key)
        pairs = [key, value]
        print("index:", index)
        # current_pair = self.storage[index]
        # last_pair = 

        if self.count >= self.capacity:
            self.resize()  # you made this function below
            # print("Error, array is full!")
            # return
        # for i in range(self.count, index, -1):
        #     self.storage[i] = self.storage[i-1]
        # ^ now shift everything to the right
        print("capacity", self.capacity)
        self.storage[index] = pairs
        print("self.storage", self.storage)
        self.count += 1
        # ^ insert the value

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pass

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # pairs refers to key/value pairs
        index = self._hash_mod(key)
        print("index:", index, key)
        pairs = self.storage[index]
    
        if pairs is not None and key == pairs[0]:
            return pairs[1] # pairs[1] = value
        else:
            return None

        print("storage 0", pairs)
        return pairs[1] # index 1 = values



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # make another block a memory that is double the current capacity
        self.capacity *= 2
        new_storage = [None] * self.capacity
        # copy everything over below
        print("capacity2", self.capacity)
        for i in range(self.count):
            pairs = self.storage[i]
            key = pairs[0]
            print("key", key)
            index = self._hash_mod(key)
            new_storage[index] = pairs
        self.storage = new_storage  # point to new storage
        print("capacity3", self.capacity)


if __name__ == "__main__":
    ht = HashTable(2)
    # initializing it to 2 up here
    # print(ht.storage)
    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")
    # ht.retrieve("laura")
    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    print("")
