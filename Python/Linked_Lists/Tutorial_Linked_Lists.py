# Define your Node class below:

class Node:
  def __init__(self, value, next_node = None):
    self.value = value
    self.next_node = next_node
  
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node

  def set_next_node(self, new_next_node):
    self.next_node = new_next_node

# an instance of Node
my_node = Node(44)
my_node.value = 44
print(my_node.get_value())


# Create your LinkedList class below:
class LinkedList:
  def __init__(self, value = None):
    self.head_node = Node(value = value)
    
  def get_head_node(self):
    return self.head_node

  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

  def stringify_list(self):
    string_list = ''
    current_node = self.get_head_node()
    while (current_node):
      if (current_node.get_value() is not None):
        string_list += str(current_node.get_value()) + '\n'
        current_node = current_node.get_next_node()
    
    return string_list



def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node

# Test your code by uncommenting the statements below - did your list print to the terminal?
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())

ll.remove_node(90)
print(ll.stringify_list())
