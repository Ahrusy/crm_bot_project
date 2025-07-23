from django.db import models

class Agent(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, default='Менеджер')
    deals_in_progress = models.PositiveIntegerField(default=0)
    current_month_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
