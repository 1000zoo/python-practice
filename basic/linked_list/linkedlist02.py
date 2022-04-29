from linkedlist import LinkedList as ll

head = 1
tail = 20
head_node = ll(head)
pre_node = head_node

for i in range(head + 1, tail + 1):
    curr_node = ll(i)
    pre_node.next = curr_node
    pre_node = pre_node.next

head_node.print_all_next_node()