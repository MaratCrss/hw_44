from django.shortcuts import render
import random
# Create your views here.
def play_game(request):
    combination = [3, 5, 7, 8]
    if request.method == "GET":
        context = {
            "result": None,
            "message": "message",
        }
        return render(request, 'index.html')
