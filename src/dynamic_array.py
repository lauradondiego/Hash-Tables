class DynamicArray:
    def__init__(self, capacity=8):
        self.storage = [None] + self.capacity
        self.count = 0  # count is how much is currently used
        self.capacity = capacity  # how much is currently allocated

    def insert(self, index, value):
        if self.count == self.capacity:
            self.resize()  # you made this function below
            print("Error, array is full")
            return

        # shift everything to the right
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]

        # insert our value
        self.storage[index] = value
        self.count += 1

    def append(self, value):
        self.insert(self.count, value)

    def resize(self):
        # make another block a memory that is double the current capacity
        self.capacity += 2
        new_storage = [None] * self.capacity
        # copy everything over below
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage  # point to new storage

    def replace(self, index, value):
        # to replace a value
        self.storage[index] = value

    def add_to_front(self, value):
        self.insert(0, value)  # at zero insert the value

    def slice(self, beginning_index, end_index):  # default value
        # need beginning and end
        # create subarray to store values

        # copy beginning to end to subarray

        # decide how this works, what happens to the original array?
        # leave it alone? OR cut out what we are slicing?

        # return subarray

        # from the guided project in lecture
