import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter.font import Font
from tkinter.colorchooser import askcolor

class MagicalNotebook:
    def __init__(self, root):
        self.root = root
        self.root.title("Magical Notebook")

        # Create menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)

        # Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Change Font", command=self.change_font)
        self.edit_menu.add_command(label="Change Color Theme", command=self.change_theme)
       # self.edit_menu.add_command(label="Spell Check", command=self.spell_check)

        # Help menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.show_about)

        # Text area
        self.text_area = tk.Text(self.root, wrap=tk.WORD, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)

        # Initialize default font and color
        self.current_font = Font(family="Arial", size=12)
        self.current_bg_color = "#FFFFFF"
        self.current_fg_color = "#000000"
        self.text_area.config(font=self.current_font, bg=self.current_bg_color, fg=self.current_fg_color)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.INSERT, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)

    def save_as_file(self):
        # Save As functionality here
        self.save_file()

    def exit_app(self):
        self.root.quit()

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

    def change_font(self):
        font_family = simpledialog.askstring("Font Family", "Enter the font family (e.g., Arial, Courier):", 
                                             initialvalue=self.current_font.actual("family"))
        font_size = simpledialog.askinteger("Font Size", "Enter the font size (e.g., 12, 14):", 
                                            initialvalue=self.current_font.actual("size"))

        if font_family and font_size:
            self.current_font = Font(family=font_family, size=font_size)
            self.text_area.config(font=self.current_font)

    def change_theme(self):
        color = askcolor(title="Choose Background Color")[1]

        if color:
            self.current_bg_color = color
            self.current_fg_color = "#FFFFFF" if color == "#000000" else "#000000"
            self.text_area.config(bg=self.current_bg_color, fg=self.current_fg_color)

   
   
    def show_about(self):
        messagebox.showinfo("About", "Magical Notebook v1.1\nCreated by [Your Name]\nWith Font Changing, Color Themes, and Basic Spell Check!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MagicalNotebook(root)
    root.mainloop()
