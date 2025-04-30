import tkinter as tk
from tkinter import messagebox, ttk
from boleto import Palco, Platea, Galeria

class TeatroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Teatro Municipal")
        self.boletos = []

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('TCombobox', font=('Arial', 10))
        
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
     
        ttk.Label(self.main_frame, text="TEATRO MUNICIPAL", font=('Arial', 14, 'bold')).grid(
            row=0, column=0, columnspan=2, pady=(0, 20))
        
        ttk.Label(self.main_frame, text="Datos del Boleto").grid(
            row=1, column=0, sticky="w", pady=(0, 10))
        
        ttk.Label(self.main_frame, text="Tipo:").grid(row=2, column=0, sticky="w")
        self.tipo_boleto = ttk.Combobox(
            self.main_frame, 
            values=["Palco", "Platea", "Galería"],
            state="readonly")
        self.tipo_boleto.grid(row=2, column=1, pady=5, sticky="ew")
        self.tipo_boleto.current(0)
        
        ttk.Label(self.main_frame, text="Número:").grid(row=3, column=0, sticky="w")
        self.numero_entry = ttk.Entry(self.main_frame)
        self.numero_entry.grid(row=3, column=1, pady=5, sticky="ew")
        self.numero_entry.insert(0, "1")
        
        ttk.Label(self.main_frame, text="Días para el Evento:").grid(
            row=4, column=0, sticky="w")
        self.dias_entry = ttk.Entry(self.main_frame)
        self.dias_entry.grid(row=4, column=1, pady=5, sticky="ew")
        self.dias_entry.insert(0, "0")
        
        btn_frame = ttk.Frame(self.main_frame)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=20)
        
        ttk.Button(btn_frame, text="Vender", command=self.vender_boleto).pack(
            side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Salir", command=root.quit).pack(
            side=tk.LEFT, padx=5)
        
        
        self.info_label = ttk.Label(
            self.main_frame, 
            text="Número: -, Precio: -",
            font=('Arial', 10, 'bold'))
        self.info_label.grid(row=6, column=0, columnspan=2, pady=(20, 0))
        
        self.main_frame.columnconfigure(1, weight=1)
    
    def vender_boleto(self):
        try:
            numero = int(self.numero_entry.get())
            tipo = self.tipo_boleto.get()
            dias = int(self.dias_entry.get())
            
            if tipo == "Palco":
                boleto = Palco(numero)
            elif tipo == "Platea":
                boleto = Platea(numero, dias)
            elif tipo == "Galería":
                boleto = Galeria(numero, dias)
            else:
                messagebox.showerror("Error", "Seleccione un tipo de boleto válido")
                return
                
            self.boletos.append(boleto)
            self.info_label.config(text=str(boleto))
            messagebox.showinfo("Éxito", "Boleto vendido correctamente")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")

if __name__ == "__main__":
    root = tk.Tk()
    app = TeatroApp(root)
    root.mainloop()