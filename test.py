import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

def select_pdf():
    # PDF dosyası seçme
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        process_pdf(file_path)

def process_pdf(file_path):
    try:
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            total_characters = 0
            limit = 1000000
            reached_page = None
            
            # PDF sayfalarını gezerek karakter sayısını hesapla
            for page_num in range(len(pdf_reader.pages)):
                page_text = pdf_reader.pages[page_num].extract_text()
                total_characters += len(page_text)
                
                # 1 milyon karaktere ulaşınca durdur
                if total_characters >= limit:
                    reached_page = page_num + 1
                    break
            
            if reached_page:
                messagebox.showinfo("Sonuç", f"1 milyon karakter {reached_page}. sayfada doldu.")
            else:
                messagebox.showinfo("Sonuç", f"Toplam karakter sayısı: {total_characters}")
    
    except Exception as e:
        messagebox.showerror("Hata", f"PDF işlenirken bir hata oluştu: {str(e)}")

# Ana pencereyi oluştur
root = tk.Tk()
root.title("PDF Seç ve İşle")
root.geometry("300x150")

# PDF seçme butonu
select_button = tk.Button(root, text="PDF Seç", command=select_pdf)  # command parametresi düzeltildi
select_button.pack(pady=20)

# Pencereyi başlat
root.mainloop()
