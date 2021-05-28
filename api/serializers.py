from rest_framework.serializers import ModelSerializer
from .models import MainCycle, Boost

class MainCycleSerializer(ModelSerializer):
    class Meta:
        model = MainCycle
        fields = '__all__'

class BoostSerializer(ModelSerializer):
    class Meta:
        model = Boost
        fields = ['id', 'power', 'price', 'level', 'boost_type']