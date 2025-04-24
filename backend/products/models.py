from django.db import models
from users.models import User

class Product(models.Model):
    STATUS_CHOICES = [
        ('on_sale', '판매중'),
        ('reserved', '예약중'),
        ('sold', '판매완료'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='on_sale')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
