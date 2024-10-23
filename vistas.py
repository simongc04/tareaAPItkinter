from models.product import Product
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from dataclass_wizard import fromdict
from models.APIResponse import APIResponse
from models.product import Product

def mostrar_producto(producto: Product):
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Producto Simon")
    root.geometry("512x512")
    root.config(bg="purple")


    label_title = tk.Label(root, text=producto.title, font=("Arial", 22),bg="purple" ,fg="white")
    label_title.pack(pady=10)

    label_price = tk.Label(root, text=f"Precio: ${producto.price}", font=("Arial", 14),bg="purple" ,fg="white")
    label_price.pack(pady=5)








    label_reviews = tk.Label(root, text="Comentarios:", font=("Arial", 16), bg="purple", fg="white")
    label_reviews.pack(pady=20)

    for review in producto.reviews:
        label_review = tk.Label(root, text=f"- {review.comment}",  bg="purple", fg="white")
        label_review.pack(padx=10)

    root.mainloop()