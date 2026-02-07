from typing import TYPE_CHECKING

from django.db import models
from django.contrib.auth import get_user_model
from sells.models.items import ItemCarrito

User = get_user_model()


class Cart(models.Model):
    
    if TYPE_CHECKING:
        id: int

    cliente = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="carritos"
    )
    items = models.ManyToManyField(
        ItemCarrito,
        blank=True
    )
    creado = models.DateTimeField(
        auto_now_add=True
    )
    actualizado = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"

    def __str__(self) -> str:
        return f"Carrito #{self.id} - {self.cliente}"

    # --- Dominio ---
    def agregar_producto(self, producto, cantidad: int = 1) -> None:
        item, _ = ItemCarrito.objects.get_or_create(
            producto=producto
        )
        item.cantidad += cantidad
        item.save()
        self.items.add(item)

    def quitar_producto(self, producto) -> None:
        self.items.filter(producto=producto).delete()

    def calcular_total(self):
        return sum(item.subtotal() for item in self.items.all())
