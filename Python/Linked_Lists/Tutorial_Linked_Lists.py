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
