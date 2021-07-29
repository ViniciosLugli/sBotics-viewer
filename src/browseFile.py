from tkinter import filedialog

class FileBrowser:
	def browse():
		filetypes = (
			('text files', '*.txt'),
			('All files', '*.*')
		)
		filename = filedialog.askopenfilename(title='Open a console file', filetypes=filetypes)
		return filename