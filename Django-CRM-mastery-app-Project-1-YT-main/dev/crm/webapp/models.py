from django.db import models
from django.contrib.auth.models import User

class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.CharField(max_length=255)

    phone = models.CharField(max_length=20)

    address = models.CharField(max_length=300)

    city = models.CharField(max_length=255)

    province = models.CharField(max_length=200)

    country = models.CharField(max_length=125)
# models.py

from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Add other fields as needed

# models.py
from django.db import models
from django.contrib.auth.models import User

# models.py
from django.db import models
from django.contrib.auth.models import User

class Interaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Assuming Customer model exists
    interaction_type = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    notes = models.TextField()

    def __str__(self):
        return f"Interaction between {self.user.username} and {self.customer}"









