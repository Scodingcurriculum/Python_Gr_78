from tkinter import *
from tkinter import filedialog, messagebox

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
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)
        # Edit menu
        self.edit_menu =  Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        # Help menu
        self.help_menu =  Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.show_about)
        # Text area
        self.text_area =  Text(self.root)
        self.text_area.pack(fill= BOTH, expand=1)
    def new_file(self):
        self.text_area.delete(1.0,  END)
    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0,  END)
                self.text_area.insert(INSERT, content)
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get(1.0,  END)
                file.write(content)
    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]  )
        if file_path:
            # Save the content to the file
            with open(file_path, "w") as file:
                content = self.text_area.get(1.0, END)
                file.write(content)
    def exit_app(self):
        self.root.quit()
    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")
    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")
    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")
    def show_about(self):
        messagebox.showinfo("About", "NotepadUI v1.0\nCreated by [Your Name]")

if __name__ == "__main__":
    root = Tk()
    app = NotepadUI(root)
    root.mainloop()
