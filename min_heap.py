class MinHeap:

    def __init__(self, array=None):
        # Indexing begins at 1
        self.heap = [None]
    
    def parent(self, i):
        return i // 2

    def leftChild(self, i):
        return 2 * i

    def rightChild(self, i):
        return 2 * i + 1

    def size(self):
        return len(self.heap) - 1

    def heapifyUp(self, idx):
        '''
            TC: O(logn)
            AS: O(1)
        '''
        while idx > 1  and self.heap[idx] < self.heap[idx//2]:
           parent = idx//2
           self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
           idx = parent

    def heapifyDown(self, i):
        '''
            TC: O(logn)
            AS: O(1)
        '''
        while self.leftChild(i) <= self.size():
            left = self.leftChild(i)
            right = self.rightChild(i)
            smallest = i

            if left <= self.size() and self.heap[left] < self.heap[smallest]:
                smallest = left
            
            if right <= self.size() and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def insert(self, val):
        '''
            TC: O(logn)
            AS: O(1)
        '''
        self.heap.append(val)
        self.heapifyUp(self.size())

    def peek(self):
        '''
            TC: O(1)
            AS: O(1)
        '''
        if self.size() >= 1:
            return self.heap[1]
        return None     
    
    def print(self):
        '''
            TC: O(n)
            AS: O(n)
        '''
        print(self.heap[1:])

    

heap = MinHeap()
heap.insert(10)
heap.insert(15)
heap.insert(5)
heap.insert(6)
heap.insert(7)
heap.insert(2)

heap.print()