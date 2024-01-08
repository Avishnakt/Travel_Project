from django.http import HttpResponse
from django.shortcuts import render
from .models import Details
from .models import Reviews


# Create your views here.
def demo(request):
    take = Details.objects.all()
    rev = Reviews.objects.all()
    return render(request, 'index.html', {'obj': take, 'reviews': rev})

# def addition(request, ):
# global addn, mult, divide, subtract
# x = request.GET['Num1']
#   y = request.GET['Num2']
# if request.GET['dropdown'] == 'adding':
#   addn = int(x) + int(y)
# elif request.GET['dropdown'] == 'Multiplication':
#   mult = int(x) * int(y)
#  elif request.GET['dropdown'] == 'Division':
#   divide = int(x) / (int(y))
# elif request.GET['dropdown'] == 'Subtraction':
#   subtract = int(x) - int(y)

#   return render(request, 'add.html', {'res': addn, 'res2': mult, 'res3': divide, 'res4': subtract})
