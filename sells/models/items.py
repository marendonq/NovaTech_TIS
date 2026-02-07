from django.db import models
from inventory.models.product import Product


class ItemCarrito(models.Model):
    producto = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    cantidad = models.PositiveIntegerField(
        default=1
    )

    class Meta:
        verbose_name = "Item de carrito"
        verbose_name_plural = "Items de carrito"

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

    def subtotal(self):
        return self.producto.precio * self.cantidad
