from manim import *
from numpy import size
from pyrr.vector3 import create


        


class BinTree(MovingCameraScene):
    def construct(self):

       a = Text("George")
       b = Text("George").shift(DOWN*2)
       c = Text("George").shift (UP*2)
       self.add(a)
       self.wait(1)
       self.add(a.copy().scale(2))

       
       
       self.play(a.animate.to_edge(LEFT))
       self.play(FadeOut(a))
       self.wait(3)
      

    
    

                # print("Origin")
                # print(ORIGIN)
                # print("Left")
                # print(LEFT*nodes_on_level//2)
                # print("right")
                # print(RIGHT*j)
                # print(ORIGIN + (LEFT*nodes_on_level//2) + RIGHT*2*(j))
