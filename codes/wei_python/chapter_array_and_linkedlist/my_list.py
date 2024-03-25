class MyList:
    """List class"""

    def __init__(self):
        """Constructor"""
        self._capacity: int = 10  # List capacity
        self._arr: list[int] = [0] * self._capacity  # List array
        self._size: int = 0  # List size
        self._extend_ratio: int = 2  # Extend ratio

    def size(self) -> int:
        """Return list size"""
        return self._size

    def capacity(self) -> int:
        """Return list capacity"""
        return self._capacity

    def get(self, index: int) -> int:
        """Get element by index"""
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        return self._arr[index]

    def set(self, num: int, index: int):
        """Set element by index"""
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        self._arr[index] = num

    def add(self, num: int):
        """Add element to the end of list"""
        # If the list is full, extend the capacity
        if self.size() == self.capacity():
            self.extend_capacity()
        self._arr[self._size] = num
        self._size += 1

    def insert(self, num: int, index: int):
        """Insert element to the list"""
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")
        # If the list is full, extend the capacity
        if self.size() == self.capacity():
            self.extend_capacity()
        # Move elements to the right
        for j in range(self._size - 1, index - 1, -1):
            self._arr[j + 1] = self._arr[j]
        # Insert element
        self._arr[index] = num
        # Update size
        self._size += 1

    def remove(self, index: int) -> int:
        """Remove and return element by index"""
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        # Get the element
        num = self._arr[index]
        # Move elements to the left
        for j in range(index, self._size - 1):
            self._arr[j] = self._arr[j + 1]
        # Update size
        self._size -= 1
        return num

    def extend_capacity(self):
        """Extend list capacity"""
        # Create a new list with _extend_ratio times capacity, and copy elements from the old list to the new list
        self._arr = self._arr + [0] * self._capacity * (self._extend_ratio - 1)
        # Update capacity
        self._capacity = len(self._arr)

    def to_array(self) -> list[int]:
        """Convert list to array"""
        return self._arr[:self._size]


"""Main function"""
if __name__ == "__main__":
    # Create a list
    my_list = MyList()
    # Add elements to the end of list
    my_list.add(1)
    my_list.add(3)
    my_list.add(2)
    my_list.add(5)
    my_list.add(4)
    print(f"List my_list = {my_list.to_array()} , capacity = {my_list.capacity()} , size = {my_list.size()}")

    # Insert element
    my_list.insert(6, 3)
    print("List after inserting element 6 at index 3:", my_list.to_array())

    # Remove element
    my_list.remove(3)
    print("List after removing element at index 3:", my_list.to_array())

    # Get element
    num = my_list.get(1)
    print("Get element at index 1:", num)

    # Set element
    my_list.set(0, 1)
    print("List after setting element 0 at index 1:", my_list.to_array())

    # Extend capacity test
    for i in range(10):
        # When i = 5, the list is full, the capacity will be extended automatically
        my_list.add(i)
    print(f"List after extending capacity:", my_list.to_array(), ", capacity =", my_list.capacity(), ", size =", my_list.size())

