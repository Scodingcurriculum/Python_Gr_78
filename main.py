from tkinter import *

class NotepadUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Magical Notebook")
        # Create menu bar
        self.menu_bar =  Menu(self.root)
        self.root.config(menu=self.menu_bar)
        # File menu
        self.file_menu =  Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        #Additional Activity :  Add Save As option in File Menu
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_command(label="Exit", command=self.exit_app)
        # Edit menu
        self.edit_menu =  Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        #Additional Activity: Add Help Menu
        # Help menu
        self.help_menu =  Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.show_about)
        # Text area
        self.text_area =  Text(self.root)
        self.text_area.pack(fill= BOTH, expand=1)

        
    def new_file(self):
        pass

    def open_file(self):
       pass

    def save_file(self):
        pass

    def save_as_file(self):
        pass

    def exit_app(self):
        pass

    def cut_text(self):
        pass

    def copy_text(self):
        pass

    def paste_text(self):
        pass

    def show_about(self):
        pass
if __name__ == "__main__":
    root = Tk()
    app = NotepadUI(root)
    root.mainloop()
