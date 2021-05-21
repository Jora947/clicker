from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MainCycle(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    coins_count = models.IntegerField(default=0)
    click_power = models.IntegerField(default=1)

    def click(self):
        self.coins_count += self.click_power


class Boost(models.Model):
    main_cycle = models.ForeignKey(MainCycle, null=False, on_delete=models.CASCADE)
    power = models.IntegerField(default=1)
    price = models.IntegerField(default=10)
    level = models.IntegerField(default=0)

    def update_boost(self):
        if self.main_cycle.coins_count < self.price:
            return False
        
        self.main_cycle.coins_count -= self.price
        self.main_cycle.click_power += self.power
        self.main_cycle.save()

        self.level += 1
        self.power *= 2
        self.price *= 5

        return self