from tkinter import *

class App:

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()


		Label(frame, text='path: ').grid(row=0, column=0)
		self.path_var = StringVar()
		Entry(frame, textvariable=self.path_var).grid(row=0, column = 1)
		
		Label(frame, text='original string: ').grid(row=1, column=0)
		self.original_string_var = StringVar()
		Entry(frame, textvariable=self.original_string_var).grid(row=1, column = 1)
		
		Label(frame, text='replacement string: ').grid(row=2, column=0)
		self.replacement_string_var = StringVar()
		Entry(frame, textvariable=self.replacement_string_var).grid(row=2, column = 1)
		
		button = Button(frame, text='Change Name', command = self.rename)
		button.grid(row = 3, columnspan=2)

	def rename(self):
		print(self.path_var.get())

root = Tk()
root.wm_title('Rename files')
app = App(root)
root.mainloop()