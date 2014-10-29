#########################################
#
#         100pt - Working with Canvas
#
#########################################


# Add a button called "Right"
# Make it so that when you press the button, the oval moves to the left or right

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=480,height=320, background='white')
oval = drawpad.create_oval(160,160,320,320, fill="red")

class MyApp:
	def __init__(self, parent):
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		self.buttonState = True
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="Left", background= "green")
		self.button1.pack(side=LEFT)
		
	        # Add a second button!
				
						
		self.button1.bind("<Button-1>", self.button1Click) 
		drawpad.pack(side=BOTTOM)
		
	def button1Click(self, event):   
		# Make me move to the left!
		global oval
		global drawpad
		
		self.buttonState = not self.buttonState
		
		if self.buttonState:
		    self.button1.configure(text="Left")
		else:
		    self.button1.configure(text="Right")
	
	# Add the event handler for the second button!
	
		
myapp = MyApp(root)
root.mainloop()