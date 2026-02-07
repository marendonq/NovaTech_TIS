from django.db import models
from decimal import Decimal


class Product(models.Model):
    nombre = models.CharField(
        max_length=150,
        verbose_name="Nombre del producto"
    )
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    descripcion = models.TextField(
        blank=True
    )
    stock = models.PositiveIntegerField(
        default=0
    )
    categoria = models.CharField(
        max_length=100
    )
    creado = models.DateTimeField(
        auto_now_add=True
    )
    actualizado = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} (${self.precio})"

    # --- Dominio ---
    def hay_stock(self, cantidad=1) -> bool:
        return self.stock >= cantidad

    def actualizar_precio(self, nuevo_precio: Decimal):
        self.precio = nuevo_precio
        self.save(update_fields=["precio"])
