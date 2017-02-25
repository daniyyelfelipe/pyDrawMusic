#!/usr/bin/python
#coding: utf-8


# -----------------------------------------------------------------------
# FILE THAT CONTAINS ALL TURTLE PATERNS TO DRAW MUSICAL ELEMENTS IN
# THE RAWTURTLE WINDOW.
# AUTOR: DANIYYELFELIPE
# START DATE: 21/02/2017
# -----------------------------------------------------------------------


from turtle import *
import Tkinter

# ------------------------------------------------
# Global variables
# ------------------------------------------------
lapis_color = "black"

class Pentagram(RawTurtle):
	def __init__(self,canvas):
		"""Pentagram drawing."""

		RawTurtle.__init__(self,canvas)
		self.shapesize(0,0,0)
		self.color(lapis_color)
		self.speed(500)

	def draw_pentagram(self):
		# Pentagram drawing.
		# --------------------------------------------------
        # 19 notes fit in the default window size pentagram

        # Defines the horizontal size of the pentagram lines
		self.__pentagram_line_size = 1000

		# Temp var to set the position of each line
		self.__lapis_position_y = 100

		for i in range(5):
			self.penup()
			self.setposition(-500, self.__lapis_position_y)
			self.pendown()
			self.forward(self.__pentagram_line_size)
			self.__lapis_position_y = self.__lapis_position_y - 20
		# --------------------------------------------------

	def supplementary_line(self,line_position_x):
		"""Supplementary line drawing"""
		
		# Sets the supplementary line size
		self.__supplementary_line_size = 35

		# Sets the line y position (note position + 10)
		self.__lapis_position_y = -10 + 10

		# Set line x position
		self.__lapis_position_x = self.set_supplementary_line_position_x(line_position_x)

		self.penup()
		self.setposition(self.__lapis_position_x, self.__lapis_position_y)
		self.pendown()
		self.forward(self.__supplementary_line_size)

	def set_supplementary_line_position_x(self,line_position_x):
		"""Set the note x position"""

		# Default fist position
		self.line_position_1_x = -280

		if(line_position_x > 1):
			for i in range(line_position_x - 1):
				self.line_position_1_x = self.line_position_1_x + 30

			return self.line_position_1_x
		else:
			# Note position - 18
			return self.line_position_1_x - 18

class Note(RawTurtle):
	def __init__(self,canvas):
		RawTurtle.__init__(self,canvas)
		self.shapesize(0,0,0)
		self.color(lapis_color)
		self.speed(500)

	def set_note_position_x(self,note_position):
		"""Set the note x position"""

		# Default fist position
		note_position_1_x = -280

		if(note_position > 1):
			for i in range(note_position - 1):
				note_position_1_x = note_position_1_x + 30

			return note_position_1_x
		else:
			return note_position_1_x

	def set_note_height(self,note_height):
		"""Set the note height"""

		if(note_height == "C3"):
			return -10
		elif(note_height == "D3"):
			return 0
		elif(note_height == "E3"):
			return 10
		elif(note_height == "F3"):
			return 20
		elif(note_height == "G3"):
			return 30
		elif(note_height == "A3"):
			return 40
		elif(note_height == "B3"):
			return 50
		elif(note_height == "C4"):
			return 60

	def note_whole(self,note_position_x,note_height):
		"""Whole note drawing."""

		# setting up note position
		note_position_x = self.set_note_position_x(note_position_x)
		note_height = self.set_note_height(note_height)
		# Whole note drawing.
		# --------------------------------------------------
		self.penup()
		self.setposition(note_position_x, note_height)
		self.pendown()
		self.circle(10)
		# --------------------------------------------------

	def note_half(self,note_position,note_height):
		"""half note drawing."""

		# setting up note position
		note_position = self.set_note_position_x(note_position)
		note_height = self.set_note_height(note_height)

		# --------------------------------------------------
		# Drawing the circle
		self.penup()
		self.setposition(note_position, note_height)
		self.pendown()
		self.circle(10)

		# Drawing stem
		self.penup()
		self.left(90)
		self.setposition(note_position + 10, note_height + 7)
		self.pendown()
		self.forward(60)
		# lapis go back to initial angle
		self.right(90)
		# --------------------------------------------------

	def note_quarter(self,note_position,note_height):
		"""half note drawing."""

		# setting up note position
		note_position = self.set_note_position_x(note_position)
		note_height = self.set_note_height(note_height)

		# --------------------------------------------------
		# Drawing the circle
		self.penup()
		self.setposition(note_position, note_height)
		self.pendown()
		self.begin_fill()
		self.circle(10)
		self.end_fill()

		# Drawing stem
		self.penup()
		self.left(90)
		self.setposition(note_position + 10, note_height + 7)
		self.pendown()
		self.forward(60)
		# lapis go back to initial angle
		self.right(90)
		# --------------------------------------------------

	def draw_note_eighth(self,note_position,note_height):
		"""half note drawing."""

		# setting up note position
		note_position = self.set_note_position_x(note_position)
		note_height = self.set_note_height(note_height)

		# --------------------------------------------------
		# Drawing the circle
		self.penup()
		self.setposition(note_position, note_height)
		self.pendown()
		self.begin_fill()
		self.circle(10)
		self.end_fill()

		# Drawing stem
		self.penup()
		self.left(90)
		self.setposition(note_position + 10, note_height + 7)
		self.pendown()
		self.forward(60)

		# We need this position to go back to
		position_before_angle = self.position()

		# Drawing the flag
		self.right(145)
		self.forward(10)
		for i in range(6):
			self.forward(5)
			self.right(10)

		# Go back to position and angle before the stem angle
		self.penup()
		self.setposition(position_before_angle)
		self.left(115)

		# --------------------------------------------------

	def draw_note_sixteenth(self,note_position,note_height):
		"""sixteenth note drawing."""

		# setting up note position
		note_position = self.set_note_position_x(note_position)
		note_height = self.set_note_height(note_height)

		# --------------------------------------------------
		# Drawing the circle
		self.penup()
		self.setposition(note_position, note_height)
		self.pendown()
		self.begin_fill()
		self.circle(10)
		self.end_fill()

		# Drawing stem
		self.penup()
		self.left(90)
		self.setposition(note_position + 10, note_height + 7)
		self.pendown()
		self.forward(60)

		# We need this position to go back to
		position_before_angle = self.position()

		# Drawing the first flag
		self.right(145)
		self.forward(10)
		for i in range(6):
			self.forward(5)
			self.right(10)

		# Go back to position and angle before the fist stem angle
		self.penup()
		self.setposition(position_before_angle)
		self.left(115)

		# Going down
		self.right(90)
		self.forward(15)
		self.left(40)

		# Drawing the second flag
		self.pendown()
		for i in range(6):
			self.forward(5)
			self.right(10)

		# Go back to position and angle before the second stem angle
		self.penup()
		self.setposition(position_before_angle)
		self.left(110)

	def draw_note_single_dot(self,note_position,note_height):
		"""Single note dot drawing."""
		1+1

	def draw_note_double_dot(self,note_position,note_height):
		"""Double note dot drawing."""
		1+1

class Clef(RawTurtle):
	def __init__(self,canvas):
		RawTurtle.__init__(self,canvas)
		self.shapesize(1,1,1)
		self.color(lapis_color)
		self.speed(500)

	def draw_clef(self,clef):
		"""clef drawing."""

		# setting up clef position
		clef_position = -470
		clef_height = 33

		if(clef == "G"):
			# --------------------------------------------------
			# Drawing the inicial circle
			self.penup()
			self.setposition(clef_position, clef_height)
			# self.pendown()
			# self.begin_fill()
			# self.circle(7)
			# self.end_fill()

			self.penup()
			self.left(120)
			self.pendown()
			for i in range(25):
				self.forward(4)
				self.right(15)


			# # Drawing stem
			# self.penup()
			# self.left(90)
			# self.setposition(clef_position + 10, clef_height + 7)
			# self.pendown()
			# self.forward(60)
			# # lapis go back to initial angle
			# self.right(90)
			# --------------------------------------------------
		elif(clef == "F"):
			1+1

		elif(clef == "C"):
			1+1

