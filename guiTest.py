#!/usr/bin/python
#coding: utf-8



from turtle import *
import Tkinter
import lib



screenMinX = -600
screenMinY = -200
screenMaxX = 600
screenMaxY = 200

#---------------------------------------------------------
# window configutrations
#---------------------------------------------------------
main_window = Tkinter.Tk()
main_window.title("guitest")

# Set the canvas size
canvas = ScrolledCanvas(main_window,600,200,600,200)

# Turtle window
turtle_window = RawTurtle(canvas)

# Screen
screen = turtle_window.getscreen()



def btn_draw_pentagram_command(canvas):
	# Clean screen
	screen.clear()

	# lib.draw.Pentagram(canvas)
	p = lib.draw.Pentagram(canvas)
	p.draw_pentagram()
	n = lib.draw.Note(canvas)
	# n.note_whole(1, "F3")
	# for i in range(10):
		# n.note_half(i, "F3")
		# n.note_quarter(i, "F3")
		# n.draw_note_eighth(i,"F3")
		# n.draw_note_sixteenth(i, "F3")
	# p.supplementary_line(1)
	c = lib.draw.Clef(canvas)
	c.draw_clef("G")

def btn_clean_screen_command(canvas):
	# Clean screen
	screen.clear()


def main():

	#---------------------------------------------------------
	# window configutrations
	#---------------------------------------------------------

	# main_window = Tkinter.Tk()
	# main_window.title("guitest")
	# main_window.maxsize(650,300) # window max size
	# main_window.minsize(650,300) # window min size

	# # Set the canvas size
	# canvas = ScrolledCanvas(main_window,600,200,600,200)
	

	# Widgets
	txt_notas = Tkinter.Entry(main_window, width = 60)
	txt_notas.pack()
	btn_draw_pentagram = Tkinter.Button(main_window, text = "Pentagram", command = lambda: btn_draw_pentagram_command(canvas)).pack()
	btn_clean_screen = Tkinter.Button(main_window, text = "Clean Screen", command = lambda: btn_clean_screen_command(canvas)).pack()

	
	# Packing canvas
	canvas.pack(side = Tkinter.LEFT)
	# turtle_window = RawTurtle(canvas)


	# screen = turtle_window.getscreen()
	screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)
	# screen.register_shape("rock3",((-20, -16),(-21, 0), (-20,18),(0,27),(17,15),(25,0),(16,-15),(0,-21)))

	frame = Tkinter.Frame(main_window)
	frame.pack(side = Tkinter.RIGHT,fill=Tkinter.BOTH)
	turtle_window.ht()

	#mainloop
	main_window.mainloop()


	
if __name__ == "__main__":
	main();
	
