import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from processor import separate_programmes
import sys
from io import StringIO
import os

class ProgrammeSeparatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CLCS Programme CSV Separator")
        self.root.geometry("900x700")
        self.root.minsize(700, 500)
        
        # Configure colors and fonts
        self.bg_color = "#f0f0f0"
        self.header_color = "#2c3e50"
        self.accent_color = "#3498db"
        self.success_color = "#27ae60"
        self.error_color = "#e74c3c"
        self.text_color = "#2c3e50"
        
        self.root.configure(bg=self.bg_color)
        
        self.file_path = tk.StringVar()
        self.create_widgets()
        
    def create_widgets(self):
        # Header frame with gradient-like background
        header_frame = tk.Frame(self.root, bg=self.header_color, height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        # Title
        title_label = tk.Label(
            header_frame, 
            text="📄 CLCS Programme CSV Separator",
            font=("Segoe UI", 18, "bold"),
            bg=self.header_color,
            fg="white",
            pady=15
        )
        title_label.pack()
        
        # Subtitle
        subtitle_label = tk.Label(
            header_frame,
            text="Efficiently separate CSV data by programme",
            font=("Segoe UI", 10),
            bg=self.header_color,
            fg="#ecf0f1"
        )
        subtitle_label.pack()
        
        # Main content frame
        content_frame = tk.Frame(self.root, bg=self.bg_color)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # File selection card
        file_card = tk.LabelFrame(
            content_frame,
            text="📁 Select File",
            font=("Segoe UI", 11, "bold"),
            bg=self.bg_color,
            fg=self.text_color,
            padx=10,
            pady=10
        )
        file_card.pack(fill=tk.X, pady=(0, 10))
        
        file_input_frame = tk.Frame(file_card, bg=self.bg_color)
        file_input_frame.pack(fill=tk.X)
        
        self.file_entry = tk.Entry(
            file_input_frame,
            textvariable=self.file_path,
            font=("Segoe UI", 10),
            bg="white",
            fg=self.text_color,
            relief=tk.FLAT
        )
        self.file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        browse_btn = tk.Button(
            file_input_frame,
            text="🔍 Browse",
            command=self.browse_file,
            bg=self.accent_color,
            fg="white",
            font=("Segoe UI", 10, "bold"),
            padx=15,
            pady=5,
            relief=tk.FLAT,
            cursor="hand2"
        )
        browse_btn.pack(side=tk.LEFT)
        
        # File info label
        self.file_info_label = tk.Label(
            file_card,
            text="No file selected",
            font=("Segoe UI", 9),
            bg=self.bg_color,
            fg="#7f8c8d"
        )
        self.file_info_label.pack(anchor=tk.W, pady=(5, 0))
        
        # Action buttons frame
        button_frame = tk.Frame(content_frame, bg=self.bg_color)
        button_frame.pack(fill=tk.X, pady=(0, 10))
        
        process_btn = tk.Button(
            button_frame,
            text="▶ Process File",
            command=self.process_file,
            bg=self.success_color,
            fg="white",
            font=("Segoe UI", 11, "bold"),
            padx=30,
            pady=10,
            relief=tk.FLAT,
            cursor="hand2"
        )
        process_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        clear_btn = tk.Button(
            button_frame,
            text="🗑️ Clear Output",
            command=self.clear_output,
            bg="#95a5a6",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            padx=20,
            pady=10,
            relief=tk.FLAT,
            cursor="hand2"
        )
        clear_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        exit_btn = tk.Button(
            button_frame,
            text="✕ Exit",
            command=self.root.quit,
            bg=self.error_color,
            fg="white",
            font=("Segoe UI", 10, "bold"),
            padx=20,
            pady=10,
            relief=tk.FLAT,
            cursor="hand2"
        )
        exit_btn.pack(side=tk.LEFT)
        
        # Output card
        output_card = tk.LabelFrame(
            content_frame,
            text="📊 Output",
            font=("Segoe UI", 11, "bold"),
            bg=self.bg_color,
            fg=self.text_color,
            padx=10,
            pady=10
        )
        output_card.pack(fill=tk.BOTH, expand=True)
        
        self.output_text = scrolledtext.ScrolledText(
            output_card,
            height=15,
            width=80,
            font=("Courier New", 9),
            bg="white",
            fg=self.text_color,
            relief=tk.FLAT,
            wrap=tk.WORD
        )
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
        # Configure text tags for colored output
        self.output_text.tag_configure("success", foreground=self.success_color)
        self.output_text.tag_configure("error", foreground=self.error_color)
        self.output_text.tag_configure("info", foreground=self.accent_color)
        
        # Footer
        footer_frame = tk.Frame(self.root, bg=self.header_color)
        footer_frame.pack(fill=tk.X)
        
        footer_label = tk.Label(
            footer_frame,
            text="© 2024 CLCS Programme Separator • Ready to process",
            font=("Segoe UI", 9),
            bg=self.header_color,
            fg="#95a5a6",
            pady=8
        )
        footer_label.pack()
        
    def browse_file(self):
        file = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
            title="Select a CSV File"
        )
        if file:
            self.file_path.set(file)
            # Update file info label
            file_name = os.path.basename(file)
            file_size = os.path.getsize(file) / 1024  # Size in KB
            self.file_info_label.config(
                text=f"✓ Selected: {file_name} ({file_size:.1f} KB)",
                fg=self.success_color
            )
    
    def clear_output(self):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Output cleared. Ready for new process.\n", "info")
    
    def process_file(self):
        file_path = self.file_path.get()
        
        if not file_path:
            messagebox.showerror("Error", "⚠️ Please select a CSV file first.")
            return
        
        if not os.path.exists(file_path):
            messagebox.showerror("Error", "⚠️ File does not exist. Please select a valid file.")
            self.file_path.set("")
            self.file_info_label.config(text="No file selected", fg="#7f8c8d")
            return
        
        # Clear previous output
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Processing file...\n", "info")
        self.root.update()
        
        try:
            files = separate_programmes(file_path)
            
            # Display success message
            self.output_text.insert(tk.END, f"\n✓ Success! Processing completed.\n\n", "success")
            self.output_text.insert(tk.END, f"CSV files created ({len(files)} file(s)):\n\n", "info")
            
            for i, (program_name, file_path) in enumerate(files, 1):
                self.output_text.insert(tk.END, f"{i}. {program_name}\n", "success")
            
            self.output_text.see(tk.END)
            messagebox.showinfo("✓ Success", f"File processed successfully!\n\n{len(files)} CSV file(s) created.")
            
        except FileNotFoundError as e:
            error_msg = f"✗ File Error: {str(e)}"
            self.output_text.insert(tk.END, error_msg + "\n", "error")
            self.output_text.see(tk.END)
            messagebox.showerror("File Error", error_msg)
            
        except Exception as e:
            error_msg = f"✗ Error: {str(e)}"
            self.output_text.insert(tk.END, error_msg + "\n", "error")
            self.output_text.see(tk.END)
            messagebox.showerror("Error", error_msg)

if __name__ == "__main__":
    root = tk.Tk()
    gui = ProgrammeSeparatorGUI(root)
    root.mainloop()