#!/usr/bin/python
#coding: utf-8



from turtle import *
import Tkinter


class Pentagram(RawTurtle):
    def __init__(self,canvas):
        RawTurtle.__init__(self,canvas)
        self.penup()

        self.setposition(-500,0)

        self.color("purple")
        self.speed(500)

        """Pentagram drawing."""
        # Pentagram drawing.
        # --------------------------------------------------
        # 19 notes fit in the default window size pentagram

        # Defines the horizontal size of the pentagram lines
        self.pentagram_line_size = 1000

        # Temp var to set the position of each line
        self.lapis_position_y = 100

        for i in range(5):
			self.penup()
			self.setposition(-500, self.lapis_position_y)
			self.pendown()
			self.forward(self.pentagram_line_size)
			self.lapis_position_y = self.lapis_position_y - 50
		# --------------------------------------------------