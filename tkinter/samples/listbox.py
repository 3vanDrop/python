class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Lista en Tcl/Tk")
        
        # Crear una barra de deslizamiento con orientación vertical.
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        # Vincularla con la lista.
        self.listbox = tk.Listbox(self, yscrollcommand=scrollbar.set)
        
        # Insertar 20 elementos.
        for i in range(20):
            self.listbox.insert(tk.END, "Elemento {}".format(i))
        
        scrollbar.config(command=self.listbox.yview)
        # Ubicarla a la derecha.
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.pack()
        
        self.pack()
