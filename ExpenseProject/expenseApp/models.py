from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.
class Expense(models.Model):
    CATEGORY_CHOICES=[
        ('food','Food'),
        ('bill','Bill'),
        ('fuel','Fuel')
    ]
    PAYMENT_CHOICES=[
        ('UPI','UPI'),
        ('card','Card')
    ]
    title=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=8, decimal_places=2)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    category=models.CharField(max_length=10,choices=CATEGORY_CHOICES,default='food')
    payment=models.CharField(max_length=10,choices=PAYMENT_CHOICES,default='UPI')
    
    def __str__(self):
        return f"{self.title} - {self.amount}"