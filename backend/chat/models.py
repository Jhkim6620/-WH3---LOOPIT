# chat/models.py
from django.db import models
from django.conf import settings
from products.models import Product

User = settings.AUTH_USER_MODEL

class ChatRoom(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chatrooms_as_buyer')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chatrooms_as_seller')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='chat_rooms')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('buyer', 'seller', 'product')

    def __str__(self):
        return f"{self.buyer} ↔ {self.seller} - {self.product.title}"


class ChatMessage(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.message[:20]}"
