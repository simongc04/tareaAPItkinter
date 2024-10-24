from typing import List

from models.APIResponse import APIResponse
from models.product import Product
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests

class ProductViewer:
    def __init__(self, productos):
        self.productos: List[Product] = productos
        self.indice_actual = 0
        self.root = tk.Tk()
        self.root.title("Producto Simon")
        self.root.config(bg="purple")

        self.crear_widgets()
        self.mostrar_productos()
        self.root.mainloop()

    def crear_widgets(self):
        # Título del producto
        self.titulo = ttk.Label(self.root, font=("Arial", 22), background="purple", foreground="white")
        self.titulo.pack(pady=0)

        # Buscador
        self.buscador = tk.Frame(self.root, bg="purple")
        self.buscador.pack(side="top", pady=10)

        self.entry_buscar = ttk.Entry(self.buscador)
        self.entry_buscar.pack(side="left")
        self.btn_buscar = ttk.Button(self.buscador, text="Buscar", command=self.abrir_ventana_busqueda)
        self.btn_buscar.pack(side="left", padx=10)

        # Categoría del producto
        self.categoria = ttk.Label(self.root, font=("Arial", 14), background="purple", foreground="white")
        self.categoria.pack(pady=0)

        # Precio del producto
        self.precio = ttk.Label(self.root, font=("Arial", 14), background="purple", foreground="white")
        self.precio.pack(pady=20)

        # Cargamos imagen
        self.imagen = ttk.Label(self.root, background="purple")
        self.imagen.pack(pady=5)

        # Descripción del producto
        self.descripcion = ttk.Label(self.root, text="Descripción:", font=("Arial", 16), background="purple",foreground="white")
        self.descripcion.pack(pady=5)

        self.descripcion_texto = ttk.Label(self.root, background="purple", foreground="white", wraplength=400)
        self.descripcion_texto.pack(pady=5)

        # Comentarios del producto
        self.comentarios = ttk.Label(self.root, text="Comentarios:", font=("Arial", 16), background="purple",foreground="white")
        self.comentarios.pack(pady=20)

        self.marco_comentarios = tk.Frame(self.root, bg="purple")
        self.marco_comentarios.pack()

        # Botones para navegar entre productos
        self.btn_anterior = ttk.Button(self.root, text="Anterior", command=self.mostrar_producto_anterior)
        self.btn_anterior.pack(side=tk.LEFT, padx=20, pady=20)

        self.btn_siguiente = ttk.Button(self.root, text="Siguiente", command=self.mostrar_siguiente_producto)
        self.btn_siguiente.pack(side=tk.RIGHT, padx=20, pady=20)



    def mostrar_productos(self):
        producto = self.productos[self.indice_actual]

        # Actualiza con información del producto
        self.titulo.config(text=producto.title)
        self.precio.config(text=f"Precio: ${producto.price}")
        self.descripcion_texto.config(text=producto.description)
        self.categoria.config(text=f"Categoría: {producto.category}")

        imagen_raw = requests.get(producto.thumbnail, stream=True).raw
        imagen_foto = Image.open(imagen_raw).resize((128, 128))
        imagen_tk = ImageTk.PhotoImage(imagen_foto)
        self.imagen.image = imagen_tk
        self.imagen.config(image=imagen_tk)

        # Limpia comentarios anteriores
        for widget in self.marco_comentarios.winfo_children():
            widget.destroy()

        # Muestra comentarios del producto
        for comentario in producto.reviews:
            etiqueta_comentario = ttk.Label(self.marco_comentarios, text=f"- {comentario.comment}", background="purple", foreground="white", wraplength=400)
            etiqueta_comentario.pack(padx=10)

    def mostrar_siguiente_producto(self):
        if self.indice_actual < len(self.productos) - 1:
            self.indice_actual += 1
            self.mostrar_productos()

    def mostrar_producto_anterior(self):
        if self.indice_actual > 0:
            self.indice_actual -= 1
            self.mostrar_productos()

    def abrir_ventana_busqueda(self):
        ventana_busqueda = tk.Toplevel(self.root)
        ventana_busqueda.title("Buscar Producto")
        ventana_busqueda.geometry("300x200")
