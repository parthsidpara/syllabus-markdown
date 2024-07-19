import tkinter as tk
from tkinter import filedialog, messagebox
from .converter import extract_text_from_pdf, create_markdown_from_syllabus, save_markdown_to_file

class SyllabusConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Syllabus PDF to Markdown Converter")
        self.root.geometry("520x170")  # Set initial window size
        
        # center the window on the screen
        window_width = 520
        window_height = 170
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # set window icon
        # self.root.iconbitmap("logo.ico") # not working!!
        
        # syllabus pdf section
        self.label_pdf = tk.Label(root, text="Syllabus PDF:")
        self.label_pdf.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_pdf = tk.Entry(root, width=50)
        self.entry_pdf.grid(row=0, column=1, padx=10, pady=10, sticky="we")

        self.button_browse_pdf = tk.Button(root, text="Browse", command=self.browse_pdf)
        self.button_browse_pdf.grid(row=0, column=2, padx=10, pady=10)

        # markdown file section
        self.label_md = tk.Label(root, text="Markdown File:")
        self.label_md.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry_md = tk.Entry(root, width=50)
        self.entry_md.grid(row=1, column=1, padx=10, pady=10, sticky="we")

        self.button_browse_md = tk.Button(root, text="Browse", command=self.browse_md)
        self.button_browse_md.grid(row=1, column=2, padx=10, pady=10)

        # convert button
        self.button_convert = tk.Button(root, text="Convert PDF to Markdown", command=self.convert_pdf_to_markdown)
        self.button_convert.grid(row=2, column=1, pady=20)

    def browse_pdf(self):
        pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if pdf_path:
            self.entry_pdf.delete(0, tk.END)
            self.entry_pdf.insert(tk.END, pdf_path)

    def browse_md(self):
        md_path = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Markdown Files", "*.md")])
        if md_path:
            self.entry_md.delete(0, tk.END)
            self.entry_md.insert(tk.END, md_path)

    def convert_pdf_to_markdown(self):
        pdf_path = self.entry_pdf.get().strip()
        if not pdf_path:
            messagebox.showerror("Error", "Please select a PDF file.")
            return
        
        md_path = self.entry_md.get().strip()
        if not md_path:
            messagebox.showerror("Error", "Please select a Markdown file destination.")
            return

        try:
            # extract text from pdf
            pdf_text = extract_text_from_pdf(pdf_path)
            
            # create markdown content from extracted text
            markdown_content = create_markdown_from_syllabus(pdf_text)
            
            # save the markdown content to a file
            save_markdown_to_file(markdown_content, md_path)
            
            messagebox.showinfo("Conversion Successful", f"Markdown file created:\n{md_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

def create_gui():
    root = tk.Tk()
    app = SyllabusConverterApp(root)
    root.mainloop()
