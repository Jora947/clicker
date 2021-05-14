from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MainCycle(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    coins_count = models.IntegerField(default=0)
    click_power = models.IntegerField(default=1)

    def click(self):
        self.coins_count += self.click_power