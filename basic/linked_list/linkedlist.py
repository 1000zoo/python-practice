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
    
    # 처음으로 등장하는 val 제거
    def delete_node(self, pre_node, val):
        if self.val == val:
            pre_node.next = self.next
            return "success"
        else:
            if self.next is None:
                return "no %d in this node" % val
            else:
                return self.next.delete_node(self, val)

    # 처음으로 등장하는 val 뒤에 새로운 값 추가
    def insert_node(self, val, new_val):
        if self.val == val:
            new_node = LinkedList(new_val, self.next)
            self.next = new_node
            return "success"
        else:
            if self.next is None:
                return "no %d in this node" % val
            else:
                return self.next.insert_node(val, new_val)

