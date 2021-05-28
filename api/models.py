from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MainCycle(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    coins_count = models.IntegerField(default=0)
    click_power = models.IntegerField(default=1)
    auto_click_power = models.IntegerField(default=0)
    level = models.IntegerField(default=0)

    def click(self):
        self.coins_count += self.click_power

        if self.coins_count > self.is_level_up():
            self.level += 1
            return True
        return False

    def is_level_up(self):
        # 0 > 1000; 1 > 2000; 2 > 5000 ...
        return (self.level**2+1)*1000


class Boost(models.Model):
    main_cycle = models.ForeignKey(MainCycle, null=False, on_delete=models.CASCADE)
    power = models.IntegerField(default=1)
    price = models.IntegerField(default=10)
    level = models.IntegerField(default=0)
    boost_type = models.IntegerField(default=0)

    def update_boost(self):
        if self.main_cycle.coins_count < self.price:
            return False
        
        self.main_cycle.coins_count -= self.price
        self.level += 1
        self.power *= 2
        self.price *= 5

        if self.boost_type == 1:
            self.main_cycle.auto_click_power += self.power
            self.price *= 5
        elif self.boost_type == 0:
            self.main_cycle.click_power += self.power

        self.main_cycle.save()

        return self

