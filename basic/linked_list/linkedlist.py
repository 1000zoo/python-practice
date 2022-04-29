class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def set_node(self, next):
        self.next = next
    
    # self 부터 tail 까지 출력 
    def print_all_next_node(self, count=0):
        count += 1
        if self.next is None:
            print(self.val)
        else:
            print(self.val, "\t=>\t", end="")
            if count >= 5:
                print()
                count = 0
            self.next.print_all_next_node(count)
    
    def delete_node(self, pre_node, val):
        if self.val == val:
            pre_node.next = self.next
            return "success"
        
        else:
            if self.next is None:
                return "no %d in this node" % val
            else:
                return self.next.delete_node(self, val)
