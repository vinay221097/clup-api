from django.db import models

# Create your models here.


class Position(models.Model):

    address = models.CharField(max_length=100, null=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    def __str__(self):
        return self.address

    def natural_key(self):
        return {"address": self.address, "lat": self.latitude, "lon": self.longitude}


class Store(models.Model):
    store_id = models.IntegerField(primary_key=True)
    location = models.OneToOneField(Position, on_delete=models.CASCADE)
    max_customers = models.IntegerField()
    current_customers = models.IntegerField()
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name + " at " + str(self.location.address)


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25, null=True)
    phone_number = models.CharField(max_length=13, unique=True)
    email_address = models.CharField(max_length=30, null=True)
    isManager = models.BooleanField(default=False)
    managed_store_id = models.ManyToManyField(Store, default=[])

    def __str__(self):
        return self.phone_number


class Ticket(models.Model):
    ticket_id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status_choices = (('New', 'New'), ('Scanned', 'Scanned'), ('Completed', 'Completed'))
    status = models.CharField(max_length=10, choices=status_choices, default='New')
    time_of_request = models.DateTimeField()
    time_of_entry = models.DateTimeField(null=True, blank=True)
    time_of_exit = models.DateTimeField(null=True, blank=True)
    assigned_to_user = models.ForeignKey(to=User, to_field="user_id", on_delete=models.CASCADE)
    assigned_to_store = models.ForeignKey(Store, to_field="store_id", on_delete=models.CASCADE)
    categories_to_visit = models.CharField(max_length=150, null=True, blank=True, default='groceries')

    def __str__(self):
        return str(self.assigned_to_user.phone_number)+""+str(self.time_of_request)


class BookingSlot(models.Model):
    slot_number = models.IntegerField()
    slot_date = models.DateField()
    slot_store = models.ForeignKey(Store, to_field="store_id", on_delete=models.CASCADE)
    customers_in_slot = models.IntegerField(default=0)

    def __str__(self):
        return str(self.slot_date) + "  "+str(self.slot_number)
