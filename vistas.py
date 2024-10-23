from models.product import Product
import tkinter as tk


def mostrar_producto(producto: Product):
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Producto Simon")
    root.geometry("512x512")
    root.config(bg="purple")

    # Título del producto
    label_title = tk.Label(root, text=producto.title, font=("Arial", 22), bg="purple", fg="white")
    label_title.pack(pady=10)

    # Precio del producto
    label_price = tk.Label(root, text=f"Precio: ${producto.price:.2f}", font=("Arial", 14), bg="purple", fg="white")
    label_price.pack(pady=5)

    # Descripción del producto
    label_description = tk.Label(root, text="Descripción:", font=("Arial", 16), bg="purple", fg="white")
    label_description.pack(pady=5)

    label_description_text = tk.Label(root, text=producto.description, bg="purple", fg="white", wraplength=400)
    label_description_text.pack(pady=5)

    # Categoría del producto
    label_category = tk.Label(root, text=f"Categoría: {producto.category}", font=("Arial", 14), bg="purple", fg="white")
    label_category.pack(pady=5)

    # Comentarios del producto
    label_reviews = tk.Label(root, text="Comentarios:", font=("Arial", 16), bg="purple", fg="white")
    label_reviews.pack(pady=20)

    for review in producto.reviews:
        label_review = tk.Label(root, text=f"- {review.comment}", bg="purple", fg="white", wraplength=400)
        label_review.pack(padx=10)

    root.mainloop()





    root.mainloop()