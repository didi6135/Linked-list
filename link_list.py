
# Class that create the Node between the objects
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Class that create the linked list and make some function
class LinkList:

    def __init__(self):
        self.head = None

    # function that inserting elements in the beginning of the linked list
    def inserting_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    # function that inserting object in the end of the linked list
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    # function that inserting objects to linked list
    def insert_values(self, values):
        self.head = None
        for value in values:
            self.inserting_at_beginning(value)

    # function that calc the length of linked list
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

    # Function that remove elements from list
    def remove_element(self, index):
        length = self.get_length()
        if index >= length or index < 0:
            raise Exception('invalid index')

        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next

            itr = itr.next
            count += 1

    # function that inserting element in specific index
    def insert_at_index(self, index, data):
        length = self.get_length()
        if index >= length or index < 0:
            raise Exception('invalid index')

        if index == 0:
            self.head = Node(data, self.head)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1
    # function that print the AVG of all link list
    def average(self):
    avg = 0
    count = 0
    itr = self.head
    while itr:
        avg += int(itr.data)
        itr = itr.next
        count += 1

    return  avg // count

    # function that print the all linked list
    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        all_link_list = ''
        while itr:
            all_link_list += str(itr.data) + '-->'
            itr = itr.next
        print(all_link_list)


if __name__ == '__main__':
    pass
    # linked_list = LinkList()
    # linked_list.insert_values(['david', 'naftali', 'hadar'])
    # print(f"length: {linked_list.get_length()}")
    # linked_list.print()
    # linked_list.insert_at_index(0, 'shimon')
    # linked_list.print()
