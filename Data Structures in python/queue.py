class queue():
    def __init__(self, limit=5):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0
    
    def isEmpty(self):
        return self.size <=0