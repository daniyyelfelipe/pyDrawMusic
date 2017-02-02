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


def set_note_position(note_position):
	note_position_1_x = -280
	note_position_1_y = 20

	for i in range(note_position):
		1+1


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

	

def draw_note_whole():
	"""Whole note drawing."""
	
	# Whole note drawing.
	# --------------------------------------------------
	lapis.penup()
	lapis.setposition(-280, 20)
	lapis.pendown()
	# lapis.begin_fill()
	lapis.circle(10)
	# lapis.end_fill()
	# --------------------------------------------------

def draw_note_half():
	"""half note drawing."""

	# --------------------------------------------------
	# Drawing the circle
	lapis.penup()
	lapis.setposition(-280, 20)
	lapis.pendown()
	lapis.begin_fill()
	lapis.circle(10)
	lapis.end_fill()

	# Drawing stem
	lapis.penup()
	lapis.left(90)
	lapis.setposition(-270, 27)
	lapis.pendown()
	lapis.forward(60)
	# --------------------------------------------------




draw_pentagram()
# draw_note_whole()
draw_note_half()
turtle.exitonclick()