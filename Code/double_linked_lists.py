#!python

class ListNode:
    def __init__(self, data):
        #stores data
        self.data = data
        #stores reference for the next item
        self.next = None
        #store reference for previous item
        self.previous = None
        return

    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False

class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        return

    def list_length(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            #Increase counter by one
            count = count + 1

            #Jump to the linked node
            current_node = current_node.next

        return count

    def output_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            #Jump to the linked Node
            current_node = current_node.next

        return

    def unordered_search(self, value):
        #Define Current Node
        current_node = self.head

        #Define the position
        node_id = 1

        #Define the list of results
        results = []

        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)

            #jump to the linked node
            current_node = current_node.next
            node_id = node_id + 1

        return results

    def add_list_item(self, item):
        "add an item at the end of the list"

        if isinstance(item, ListNode):
            if self.head is None:
                self.head = item
                item.previous = None
                item.next = None
                self.tail = item
            else:
                self.tail.next = item
                item.previous = self.tail
                self.tail = item

    def remove_list_item(self, item_id):
        "remove a list item by its id"

        current_id = 1
        current_node = self.head

        while current_node is not None:
            previous_node = current_node.previous
            next_node = current_node.next

            if current_id == item_id:
                if previous_node is not None:
                    previous_node.next = next_node
                    if next_node is not None:
                        next_node.previous = previous_node
                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.previous = None
                return

            #Next Iteration
            current_node = next_node
            current_id = current_id + 1

        return
