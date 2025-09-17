# Node class for linked list
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Hashtable:
    def __init__(self, size=20):
        self.size = size
        self.table = [None] * size # create array

    def _hash(self, key):
        return hash(key) % self.size
    
    # insert new key pair value
    def insert(self, key, value):
        index = self._hash(key)
        head = self.table[index]

        # check if key is alrady exist
        current = head
        while current:
            if current == key:
                current.value = value
                return
            current = current.next
        
        # insert new node at the head of the list
        new_node = Node(key, value)
        new_node.next = head
        self.table[index] = new_node

    # Search for a key and return its value
    def search(self, key):
        index = self._hash(key)
        current = self.table[index]

        # traverse the list to find the key
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
     # delete key-value pair from the hash table
    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None

        # taverse the linked list to find the key
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next
        return False
    
    # edit the value for existing key
    def edit(self, key, new_value):
        index = self._hash(key)  
        current = self.table[index]

        # traverse the linked list to find the key
        while current:
            if current.key == key:
                current.value = new_value 
                return True  
            current = current.next
        return False
    
    # display all contents of the hash table
    def display(self):
        for i, head in enumerate(self.table):
            print(f"Bucket {i}:", end=" ") 
            current = head
            
            # Traverse the linked list and print each key-value pair
            while current:
                print(f"[{current.key}: {current.value.name}]", end=" -> ")
                current = current.next
            print("None") 
