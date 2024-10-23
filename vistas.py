from models.product import Product
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

class ProductViewer:
    def __init__(self, productos):
        self.productos = productos
        self.indice_actual = 0
        self.root = tk.Tk()
        self.root.title("Producto Simon")
        self.root.geometry("512x512")
        self.root.config(bg="purple")

        self.crear_widgets()
        self.mostrar_productos()
        self.root.mainloop()

    def crear_widgets(self):
        # Título del producto
        self.titulo = tk.Label(self.root, font=("Arial", 22), bg="purple", fg="white")
        self.titulo.pack(pady=0)

        # Categoría del producto
        self.categoria = tk.Label(self.root, font=("Arial", 14), bg="purple", fg="white")
        self.categoria.pack(pady=0)

        # Precio del producto
        self.precio = tk.Label(self.root, font=("Arial", 14), bg="purple", fg="white")
        self.precio.pack(pady=20)

        # Descripción del producto
        self.descripcion = tk.Label(self.root, text="Descripción:", font=("Arial", 16), bg="purple", fg="white")
        self.descripcion.pack(pady=5)

        self.descripcion_texto = tk.Label(self.root, bg="purple", fg="white", wraplength=400)
        self.descripcion_texto.pack(pady=5)

        # Comentarios del producto
        self.comentarios = tk.Label(self.root, text="Comentarios:", font=("Arial", 16), bg="purple", fg="white")
        self.comentarios.pack(pady=20)

        self.marco_comentarios = tk.Frame(self.root, bg="purple")
        self.marco_comentarios.pack()

        # Botones para navegar entre productos
        self.btn_anterior = tk.Button(self.root, text="Anterior", command=self.mostrar_producto_anterior)
        self.btn_anterior.pack(side=tk.LEFT, padx=20, pady=20)

        self.btn_siguiente = tk.Button(self.root, text="Siguiente", command=self.mostrar_siguiente_producto)
        self.btn_siguiente.pack(side=tk.RIGHT, padx=20, pady=20)

    def mostrar_productos(self):
        producto = self.productos[self.indice_actual]

        # Actualiza con información del producto
        self.titulo.config(text=producto.title)
        self.precio.config(text=f"Precio: ${producto.price}")
        self.descripcion_texto.config(text=producto.description)
        self.categoria.config(text=f"Categoría: {producto.category}")

        # Limpia comentarios anteriores
        for widget in self.marco_comentarios.winfo_children():
            widget.destroy()

        # Muestra comentarios del producto
        for comentario in producto.reviews:
            etiqueta_comentario = tk.Label(self.marco_comentarios, text=f"- {comentario.comment}", bg="purple", fg="white", wraplength=400)
            etiqueta_comentario.pack(padx=10)

    def mostrar_siguiente_producto(self):
        # Cambia al siguiente producto
        if self.indice_actual < len(self.productos) - 1:
            self.indice_actual += 1
            self.mostrar_productos()

    def mostrar_producto_anterior(self):
        # Cambia al producto anterior
        if self.indice_actual > 0:
            self.indice_actual -= 1
            self.mostrar_productos()
