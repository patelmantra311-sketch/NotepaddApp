import tkinter as tk
from tkinter import filedialog, messagebox 

class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.text_area=tk.Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')

        self.menu_bar=tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu=tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        self.edit_menu=tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)
        self.edit_menu.add_command(label="undo", command=self.undo)

        self.help_menu=tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.show_about)
    
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        messagebox.showinfo("New File", "New file created successfully!")

    def open_file(self):
        file_path= filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content=file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, content)
            messagebox.showinfo("File opened", "File opened successfully!")

    def save_file(self):
        content=self.text_area.get(1.0, tk.END)
        file_path=filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(content)
            messagebox.showinfo("File saved", "File saved successfully!")
    def qut(self):
        self.root.quit()
    def cut(self):
        selected_text = self.text_area.selection_get()
        self.text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)
        self.root.clipboard_clear()
        self.root.clipboard_append(selected_text)
        messagebox.showinfo("Cut", "Text cut successfully!")

    def copy(self):
        selected_text = self.text_area.selection_get()
        self.root.clipboard_clear()
        self.root.clipboard_append(selected_text)
        messagebox.showinfo("Copy", "Text copied successfully!")
    def paste(self):
        try:
            clipboard_text = self.root.clipboard_get()
            self.text_area.insert(tk.INSERT, clipboard_text)
            messagebox.showinfo("Paste", "Text pasted successfully!")
        except tk.TclError:
            messagebox.showerror("Error", "No text in clipboard to paste.")
    def undo(self):
        try:
            self.text_area.edit_undo()
            messagebox.showinfo("Undo", "Action undone successfully!")
        except tk.TclError:
            messagebox.showerror("Error", "No actions to undo.")
    def show_about(self):
        messagebox.showinfo("About", "This is a simple notepad application.")
        





        
    
    

if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()