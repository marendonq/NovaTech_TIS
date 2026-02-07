from typing import TYPE_CHECKING

from django.db import models
from django.contrib.auth import get_user_model
from sells.models.items import ItemCarrito

User = get_user_model()


class Orden(models.Model):

    if TYPE_CHECKING:
        id: int

    ESTADO_PENDIENTE = "PENDIENTE"
    ESTADO_PAGADA = "PAGADA"
    ESTADO_CANCELADA = "CANCELADA"

    ESTADOS = (
        (ESTADO_PENDIENTE, "Pendiente"),
        (ESTADO_PAGADA, "Pagada"),
        (ESTADO_CANCELADA, "Cancelada"),
    )

    cliente = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="ordenes"
    )
    items = models.ManyToManyField(ItemCarrito)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default=ESTADO_PENDIENTE
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Órdenes"
        ordering = ["-fecha"]

    def __str__(self) -> str:
        return f"Orden #{self.id} - {self.cliente}"

    # --- Dominio ---
    def calcular_total(self) -> None:
        self.total = sum(item.subtotal() for item in self.items.all())
        self.save(update_fields=["total"])

    def cambiar_estado(self, nuevo_estado: str) -> None:
        self.estado = nuevo_estado
        self.save(update_fields=["estado"])
