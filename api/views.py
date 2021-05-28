from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MainCycle, Boost
from .serializers import MainCycleSerializer, BoostSerializer

# Create your views here.
def index(request):
    user = User.objects.filter(id=request.user.id).first()
    if user == None:
        return redirect('login')

    maincycle = MainCycle.objects.get(user=request.user)
    boosts = Boost.objects.filter(main_cycle=maincycle)

    return render(request, 'index.html', {
        'main_cycle': maincycle,
        'boosts': boosts,
    })


@api_view(['GET'])
def call_click(request):
    maincycle = MainCycle.objects.get(user=request.user)
    is_level_up = maincycle.click()
    maincycle.save()

    if is_level_up:
        boost_type = 0
        if maincycle.level % 3 == 0:
            boost_type = 1

        boost = Boost(main_cycle=maincycle, power=maincycle.level*20, price=maincycle.level*50, boost_type=boost_type)
        boost.save()

        return Response({
            'main_cycle': MainCycleSerializer(maincycle).data,
            'boost': BoostSerializer(boost).data,
        })
    
    return Response({
        'main_cycle': MainCycleSerializer(maincycle).data
    })


@api_view(['POST'])
def update_boost(request):
    boost_id = request.data['boost_id']
    
    boost = Boost.objects.get(id=boost_id)
    boost.update_boost()
    boost.save()

    main_cycle = MainCycle.objects.get(user=request.user)

    return Response({
        'main_cycle': MainCycleSerializer(main_cycle).data,
        'boost': BoostSerializer(boost).data,
    })


@api_view(['POST'])
def update_coins(request):
    coins = request.data['coins']
    main_cycle = MainCycle.objects.get(user=request.user)
    main_cycle.coins_count = coins
    main_cycle.save()

    return Response({'success': 'coins was updated'}, status=200)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            main_cycle = MainCycle()
            main_cycle.user = user
            main_cycle.save()

            boost = Boost(main_cycle=main_cycle)
            boost.save()

            return redirect('login')
        else:
            return render(request, 'registration/register.html', {'form': form})


    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})