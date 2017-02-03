#!/usr/bin/python
#coding: utf-8


# -----------------------------------------------------------------------
# FILE THAT CONTAINS ALL TURTLE PATERNS TO DRAW MUSICAL ELEMENTS.
# AUTOR: DANIYYELFELIPE
# START DATE: 01/02/2017
# -----------------------------------------------------------------------

import turtle


# Var definitions
lapis = turtle.Turtle()
lapis.shape("classic")
# lapis.shapesize(1,1,1)
lapis.shapesize(0,0,0)
# lapis.color("yellow")
lapis.speed(500)


def set_note_position_x(note_position):
	"""Set the note x position"""

	# Default fist position
	note_position_1_x = -280

	if(note_position > 1):
		for i in range(note_position - 1):
			note_position_1_x = note_position_1_x + 30

		return note_position_1_x
	else:
		return note_position_1_x

def set_note_height(note_height):
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

def draw_pentagram():
	"""Pentagram drawing."""

	# Pentagram drawing.
	# --------------------------------------------------

	# Defines the horizontal size of the pentagram lines
	pentagram_line_size = 600

	# Temp var to set the position of each line
	lapis_position_y = 100

	for i in range(5):
		lapis.penup()
		lapis.setposition(-300, lapis_position_y)
		lapis.pendown()
		lapis.forward(pentagram_line_size)
		lapis_position_y = lapis_position_y - 20

	# --------------------------------------------------

def draw_note_whole(note_position_x, note_height):
	"""Whole note drawing."""
	
	# setting up note position
	note_position_x = set_note_position_x(note_position_x)
	note_height = set_note_height(note_height)

	# Whole note drawing.
	# --------------------------------------------------
	lapis.penup()
	lapis.setposition(note_position_x, note_height)
	lapis.pendown()
	# lapis.begin_fill()
	lapis.circle(10)
	# lapis.end_fill()
	# --------------------------------------------------

def draw_note_half(note_position,note_height):
	"""half note drawing."""

	# setting up note position
	note_position = set_note_position_x(note_position)
	note_height = set_note_height(note_height)

	# --------------------------------------------------
	# Drawing the circle
	lapis.penup()
	lapis.setposition(note_position, note_height)
	lapis.pendown()
	lapis.circle(10)

	# Drawing stem
	lapis.penup()
	lapis.left(90)
	lapis.setposition(note_position + 10, note_height + 7)
	lapis.pendown()
	lapis.forward(60)
	# lapis go back to initial angle
	lapis.right(90)
	# --------------------------------------------------

def draw_note_quarter(note_position,note_height):
	"""half note drawing."""

	# setting up note position
	note_position = set_note_position_x(note_position)
	note_height = set_note_height(note_height)

	# --------------------------------------------------
	# Drawing the circle
	lapis.penup()
	lapis.setposition(note_position, note_height)
	lapis.pendown()
	lapis.begin_fill()
	lapis.circle(10)
	lapis.end_fill()

	# Drawing stem
	lapis.penup()
	lapis.left(90)
	lapis.setposition(note_position + 10, note_height + 7)
	lapis.pendown()
	lapis.forward(60)
	# lapis go back to initial angle
	lapis.right(90)
	# --------------------------------------------------

def draw_note_eighth(note_position,note_height):
	"""half note drawing."""

	# setting up note position
	note_position = set_note_position_x(note_position)
	note_height = set_note_height(note_height)

	# --------------------------------------------------
	# Drawing the circle
	lapis.penup()
	lapis.setposition(note_position, note_height)
	lapis.pendown()
	lapis.begin_fill()
	lapis.circle(10)
	lapis.end_fill()

	# Drawing stem
	lapis.penup()
	lapis.left(90)
	lapis.setposition(note_position + 10, note_height + 7)
	lapis.pendown()
	lapis.forward(60)

	# We need this position to go back to
	position_before_angle = lapis.position()

	lapis.right(145)
	lapis.forward(10)
	for i in range(6):
		lapis.forward(5)
		lapis.right(10)

	# Go back to position and angle before the stem angle
	lapis.penup()
	lapis.setposition(position_before_angle)
	lapis.left(115)

	# --------------------------------------------------



# draw_pentagram()


# draw_note_whole(1,"C3")
# draw_note_half(2,"D3")
# draw_note_quarter(3,"E3")
# draw_note_eighth(4,"F3")
# draw_note_whole(5,"G3")
# draw_note_half(6,"A3")
# draw_note_quarter(7,"B3")
# draw_note_eighth(8,"C4")



# draw_note_half(2)
# draw_note_quarter(3)
# draw_note_eighth(4)

turtle.exitonclick()