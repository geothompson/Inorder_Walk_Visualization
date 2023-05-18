from subprocess import call
from manim import *
from numpy import array_equiv
from pyrr.vector3 import create


class Node:
    def __init__(self, data):
       self.left = None
       self.right = None
       self.data = data
       self.shape = Circle(0.3)

    def insert(self, data):
# Compare the new value with the parent node
       if self.data != None:
          if data < self.data:
             if self.left is None:
                self.left = Node(data)
                self.left.shape = Circle(0.3)
             else:
               self.left.insert(data)
          elif data > self.data:
             if self.right is None:
                self.right = Node(data)
                self.right.shape = Circle(0.3)
          else:
             self.right.insert(data)
       else:
          self.data = data

    def PrintTree(self):
       if self.left:
          self.left.PrintTree()
       print(self.data)
       if self.right:
          self.right.PrintTree()

    def create_tree(self, node):
      node.shape = Circle(0.5)
      if node.left != None:
          self.create_tree(node.left)
      if node.right != None:
          self.create_tree(node.right)

class Scene(MovingCameraScene):
    def construct(self):
       tree = Node(7)
       tree.insert(4)
       tree.insert(5)
       func = self.generate_func_text()
       # self.display_tree(tree, tree, ORIGIN, ORIGIN+UP*3, 1)
       global call_count, count
       call_count = Integer()
       count = 0
       call_count.to_edge(LEFT).to_edge(DOWN)
       self.add(call_count)

       self.show_in_order(tree, tree, [func])
        # self.play(a.animate.shift(2* left), b.animate.shift(2* up),
                  # c.animate.shift(2* DOWN), d.animate.shift(2* RIGHT))


#``````````````````````````````````````````````````````````````````````#
    def show_in_order(self, parent, tree, call_stack: list[VGroup]):
       #counting
       global count
       global call_count
       call_count.add_updater(lambda i: i.set_value(count))
          # self.play(
                # Create(Line(tree.shape.get_center(),
                  # tree.left.shape.get_center(), buff=0.3).set_color(BLUE))
                # )

       # self.play(new_left.animate.move_to(ORIGIN-DOWN).scale(0.7))
       # self.play(tree.shape.animate.set_color(WHITE))

       # self.play(FadeOut(new_left), FadeOut(prev_func))
       # self.play(prev_func.animate.scale(1).move_to(ORIGIN))


       call = call_stack[len(call_stack)-1]


       if tree.left != None:
          count += 1
         
          new_call = call.copy()
          self.add(new_call)
          self.play(call.animate.set_color(ORANGE).to_edge(LEFT))
          call_stack.append(new_call)
          self.show_in_order(tree, tree.left, call_stack)
          count -= 1
          
       call = call_stack.pop()
       
       self.play(call.animate.move_to(ORIGIN).set_color(RED))
      
       if tree.right != None:
          # self.play(Create(Line(tree.shape.get_center(),
          # tree.right.shape.get_center(), buff=0.3).set_color(BLUE)))
          new_call = call.copy().set_color(WHITE)
          self.play(new_call.animate.shift(DOWN*2))
          self.play(call.animate.set_color(GREEN))
          self.play(Unwrite(call))
          self.play(new_call.animate.shift(UP*2))

          call_stack.append(new_call)
          self.show_in_order(tree, tree.right, call_stack)
       else:
          self.play(Unwrite(call))



      




       # self.play(FadeOut(new_right))
       # self.play(prev_func.animate.scale(1/.3).move_to(ORIGIN))


          # self.play(Create(Line(tree.shape.get_center(),
          # parent.shape.get_center(), buff=0.3).set_color(GREEN)))


    def display_tree(self, parent, tree, prev_coord, coord, off):
       text = Integer(number=tree.data).set_x(3).set_y(3)
       self.add(text)
       if not (array_equiv(prev_coord, ORIGIN)):
          self.play(Create(Line(parent.get_center(), coord, buff=0.3)))
        # vg =VGroup(text, tree.shape)
       tree.shape.move_to(prev_coord)
       self.play(tree.shape.animate.move_to(
          coord), text.animate.move_to(coord))
       if tree.left != None:
         self.display_tree(
               tree.shape, tree.left,  coord, coord + DOWN + (LEFT*off), off-0.4
               )
       if tree.right != None:
          self.display_tree(
               tree.shape, tree.right, coord, coord + DOWN + (RIGHT*off), off-0.4
               )



    def generate_func_text(self):
       collon  = Text(":", font_size=60)
       collon2 = Text(":", font_size=60)

       definition   = Text("Inorder_Tree_Walk(node)")
       if_statement = Text("if node != NULL")
       get_left     = Text("Inorder_Tree_Walk(node.left)")
       get_right    = Text("Inorder_Tree_Walk(node.right)")
       print_node   = Text("print(node.data)")




       collon.next_to(definition, RIGHT)

       if_statement.shift(DOWN)
       if_statement.align_to(definition, LEFT)
       if_statement.shift(RIGHT*1.5)
       collon2.next_to(if_statement, RIGHT)

       get_left.shift(DOWN*2)
       get_left.align_to(if_statement, LEFT)
       get_left.shift(RIGHT*1.5)

       print_node.shift(DOWN*3)
       print_node.align_to(if_statement, LEFT)
       print_node.shift(RIGHT*1.5)

       get_right.shift(DOWN*4)
       get_right.align_to(if_statement, LEFT)
       get_right.shift(RIGHT*1.5)
         
       func_list = [definition, collon, collon2, if_statement, get_left, print_node, get_right]
         

       group = VGroup()


       for obj in func_list:
          group.add(obj)

       group.scale(0.5)
       group.move_to(ORIGIN)
               
       return (group)
         

       # self.play(Write(group))
       # self.add(new_group)

       # self.play(group.animate.shift(LEFT*3).scale(0.3))
       # self.play(new_group.animate.shift(RIGHT*3).scale(0.3))



    
    

                # print("Origin")
                # print(ORIGIN)
                # print("Left")
                # print(LEFT*nodes_on_level//2)
                # print("right")
                # print(RIGHT*j)
                # print(ORIGIN + (LEFT*nodes_on_level//2) + RIGHT*2*(j))
