from linkedlist import LinkedList as ll

head = 1
tail = 5
head_node = ll(head)
pre_node = head_node
for i in range(head + 1, tail + 1):
    curr_node = ll(i)
    pre_node.next = curr_node
    pre_node = pre_node.next

dummy_node = ll(-1, head_node)
dummy_node.next.print_all_next_node()
print(head_node.delete_node(dummy_node, 10))
dummy_node.next.print_all_next_node()