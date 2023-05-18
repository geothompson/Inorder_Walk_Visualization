from click import group
from manim import *
from numpy import size
from pyrr.vector3 import create

        


class BinTree(MovingCameraScene):
    def construct(self):
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

       obj_stack = []

       for obj in func_list:
           group.add(obj)
       # print(definition) 

       group.shift(UP*2+LEFT*2).scale(0.6)

       new_func_list = []
       new_group = VGroup()
       for ele in func_list:
            copy = ele.copy()
            new_func_list.append(copy)
            new_group.add(copy)
            
       obj_stack.append((func_list, group))
            

       self.play(Write(group))
       self.add(new_group)

       self.play(group.animate.shift(LEFT*3).scale(0.3))
       self.play(new_group.animate.shift(RIGHT*3).scale(0.3))
       # self.play(Write(group))
       # self.play(definition.animate.set_color(BLUE) )#run_time=3
       # self.play(if_statement.animate.set_color(BLUE))
       # self.play(get_left.animate.set_color(BLUE))



      

       # # new_group = group.copy()
       # self.add(new_node)
       # self.play(group.animate.scale(0.2).shift(LEFT*2))

       # self.play(group.animate.shift(UP*3+LEFT*3).scale(0.5))
       self.wait(3)





    
       # group = VGroup(definition, if_statement, get_left, print_node, get_right)
       # func_parts = [("def", definition), ("c1", collon),  ("c2", collon2),("if", if_statement) , ("left", get_left), ("print", print_node), ("right", get_right)]
       # func_dict = VDict(func_parts, show_keys=True)
