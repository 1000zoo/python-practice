from linkedlist import LinkedList as ll

head = 1
tail = 15
head_node = ll(head)
pre_node = head_node

for i in range(head + 1, tail + 1):
    curr_node = ll(i)
    pre_node.next = curr_node
    pre_node = pre_node.next

head_node.print_all_next_node()
reverse_head_node = head_node.reverse_node()
reverse_head_node.print_all_next_node()