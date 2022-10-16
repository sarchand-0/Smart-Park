from django.shortcuts import render, redirect
import pyrebase
from .decorators import allowed_users

config = {
    "apiKey": "AIzaSyDPuKnZ_W7X_NgcoTlGnzTMWI6ujl2rKyg",
    "authDomain": "parking-system-365621.firebaseapp.com",
    "databaseURL": "https://parking-system-365621-default-rtdb.firebaseio.com",
    "projectId": "parking-system-365621",
    "storageBucket": "parking-system-365621.appspot.com",
    "messagingSenderId": "514457351378",
    "appId": "1:514457351378:web:fd8054194b6cacd0d9e90b",
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def home(request):
    array = database.child('occupancy').get().val()
    slot = []
    state = []
    occupied = 0
    free = 0
    total_space = 0
    for i in range(len(array)):
        if array[i]['state'] == "occupied":
            occupied += 1
        else:
            free += 1
        state.append(array[i]['state'])
        slot.append((array[i]['slot']))
        total_space = i + 1

    print(state)
    print(slot)
    print(free)
    print(occupied)
    print("this is ", free)
    context = {'free': free, 'occupied': occupied, 'total_space': total_space}
    return render(request, 'park/home.html',context)
def AboutUs(request):
    return render(request, 'park/AboutUs.html')


@allowed_users(allowed_roles=['admin'])
def dashboard(request):
    array = database.child('occupancy').get().val()
    slot = []
    state = []
    occupied = 0
    free = 0
    total_space = 0
    for i in range(len(array)):
        if array[i]['state'] == "occupied":
            occupied += 1
        else:
            free += 1
        state.append(array[i]['state'])
        slot.append((array[i]['slot']))
        total_space = i+1

    print(state)
    print(slot)
    print(free)
    print(occupied)
    print("this is ", free)
    context = {'free':free, 'occupied':occupied,'total_space':total_space}
    return render(request,'park/Dashboard.html',context)

def Location1(request):
    a = database.child('occupancy').get().val()
    slot = []
    state = []
    occupied = 0
    free = 0
    total_space = 0
    for i in range(len(a)):
        if a[i]['state'] == "occupied":
            occupied += 1
        else:
            free += 1
        state.append(a[i]['state'])
        slot.append((a[i]['slot']))
        total_space = i + 1

    print(state)
    print(slot)
    print(free)
    print(occupied)
    print("this is ", free)
    context = {'state':state, 'slot':slot, 'free': free, 'occupied': occupied, 'total_space': total_space}

    return render(request, "park/Location1.html", context)
def Reserve(request):
    return render(request, 'park/Reserve.html')

def vid(request):
    return render(request, 'park/vid.html')
