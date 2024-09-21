from django.db import models
from django.db.models import Sum
from django.utils import timezone

class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    @classmethod
    def get_top_5_customers(cls):
        six_months_ago = timezone.now() - timezone.timedelta(days=180)
        return (
            cls.objects
            .filter(order_date__gte=six_months_ago)
            .values('customer__name')
            .annotate(total_spent=Sum('total_amount'))
            .order_by('-total_spent')[:5]
        )

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"