from django.db import models

# Create your models here.
class MainCycle(models.Model):
    coins_count = models.IntegerField(default=0)
    click_power = models.IntegerField(default=1)

    def click(self):
        self.coins_count += self.click_power