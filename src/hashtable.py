# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # this is for collision, creates a new node
        # ^ both stored at the same index, except now you can create a linked list


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table how big the array is
        # gives you empty slots.the actual values being placed in the buckets
        self.storage = [None] * capacity
        # ^ if the capacity is 100, storage gives you an array with 100 empty slots - this is the hash table
        # ^ you will store the key,value pair in here
        self.count = 0  # added this
        # ^ means storage is empty
        # ^ increase the counter by 1 in the insert method self.count += 1
        # ^ and remove function is self.count -= 1

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)
        # python's automated hash algo - returns a hashed value

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
        # hashing a value to an index, that will fit inside the storage

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        new_node = LinkedPair(key, value)

        if self.storage[index] == None:
            self.storage[index] = new_node
            self.count += 1
        else:
            temp = self.storage[index]
            if temp.key == key:
                self.storage[index].value = value
                return None
            else:
                while temp.next != None:
                    temp = temp.next
                    if temp.key == key:
                        temp.value = value
                        return None
            temp.next = new_node
            self.count += 1

        return None
        # print("key/value:", key, value)
        # index = self._hash_mod(key) # this gives you an index position, where to insert
        # # the key is the only thing that gets hashed
        # pairs = [key, value]
        # print("index:", index)
        # # current_pair = self.storage[index]
        # # last_pair =

        # if self.count >= self.capacity:
        #     self.resize()  # you made this function below
        #     # print("Error, array is full!")
        #     # return
        # # for i in range(self.count, index, -1):
        # #     self.storage[i] = self.storage[i-1]
        # # ^ now shift everything to the right
        # print("capacity", self.capacity)
        # self.storage[index] = pairs
        # print("self.storage", self.storage)
        # self.count += 1
        # # ^ insert the value

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            return

        head = self.storage[index]
        if head.key == key:
            self.storage[index] = head.next
            return

        current = self.storage[index]
        previous = head
        while current:
            if current.key == key:
                previous.next = current.next
                return

            else:
                previous = current
                current = current.next

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
            return pairs[1]  # pairs[1] = value
        else:
            return None

        print("storage 0", pairs)
        return pairs[1]  # index 1 = values

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
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    # ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    print("")
