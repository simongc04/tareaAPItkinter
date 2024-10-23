from models.product import Product
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

class ProductViewer:
    def __init__(self, products):
        self.products = products
        self.current_index = 0
        self.root = tk.Tk()
        self.root.title("Producto Simon")
        self.root.geometry("512x512")
        self.root.config(bg="purple")

        self.create_widgets()
        self.mostrar_productos()
        self.root.mainloop()

    def create_widgets(self):
        # Título del producto
        self.label_title = tk.Label(self.root, font=("Arial", 22), bg="purple", fg="white")
        self.label_title.pack(pady=0)
        # Categoría del producto
        self.label_category = tk.Label(self.root, font=("Arial", 14), bg="purple", fg="white")
        self.label_category.pack(pady=0)

        # Precio del producto
        self.label_price = tk.Label(self.root, font=("Arial", 14), bg="purple", fg="white")
        self.label_price.pack(pady=20)

        # Descripción del producto
        self.label_description = tk.Label(self.root, text="Descripción:", font=("Arial", 16), bg="purple", fg="white")
        self.label_description.pack(pady=5)

        self.label_description_text = tk.Label(self.root, bg="purple", fg="white", wraplength=400)
        self.label_description_text.pack(pady=5)


        # Comentarios del producto
        self.label_reviews = tk.Label(self.root, text="Comentarios:", font=("Arial", 16), bg="purple", fg="white")
        self.label_reviews.pack(pady=20)

        self.review_frame = tk.Frame(self.root, bg="purple")
        self.review_frame.pack()


        # Botones para navegar entre productos
        self.btn_prev = tk.Button(self.root, text="Anterior", command=self.mostrar_producto_anterior)
        self.btn_prev.pack(side=tk.LEFT, padx=20, pady=20)

        self.btn_next = tk.Button(self.root, text="Siguiente", command=self.mostrar_siguiente_producto)
        self.btn_next.pack(side=tk.RIGHT, padx=20, pady=20)

    def mostrar_productos(self):
        producto = self.products[self.current_index]

        # Actualiza las etiquetas con la información del producto
        self.label_title.config(text=producto.title)
        self.label_price.config(text=f"Precio: ${producto.price}")
        self.label_description_text.config(text=producto.description)
        self.label_category.config(text=f"Categoría: {producto.category}")

        # Limpia comentarios anteriores
        for widget in self.review_frame.winfo_children():
            widget.destroy()

        # Muestra comentarios del producto
        for review in producto.reviews:
            label_review = tk.Label(self.review_frame, text=f"- {review.comment}", bg="purple", fg="white",wraplength=400)
            label_review.pack(padx=10)


    def mostrar_siguiente_producto(self):
        # Cambia al siguiente producto
        if self.current_index < len(self.products) - 1:
            self.current_index += 1
            self.mostrar_productos()

    def mostrar_producto_anterior(self):
        # Cambia al producto anterior
        if self.current_index > 0:
            self.current_index -= 1
            self.mostrar_productos()

