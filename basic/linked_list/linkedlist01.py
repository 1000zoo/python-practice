from linkedlist import LinkedList

node1 = LinkedList(1)
node2 = LinkedList(2)
node3 = LinkedList(3)
node4 = LinkedList(4)
node5 = LinkedList(5)
node6 = LinkedList(6)

node1.set_node(node2)
node2.set_node(node3)
node3.set_node(node4)
node4.set_node(node5)
node5.set_node(node6)

node1.print_all_next_node()