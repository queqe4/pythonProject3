from django.shortcuts import render
from .models import Category

def show_menu(request):
    return render(request, "menu.html", {'category': Category.objects.all()})
# Create your views here.


def index(request):
    latest_question_list = Category.objects.order_by('-name')[:3]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)