from django.shortcuts import get_object_or_404, render, redirect

from .models import PhoneBook


# главная страница со списком телефонов
def index(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]
    # создание HTML-страницы по шаблону index.html
    # с заданными параметрами latest_phone и message
    return render(
        request,
        "index.html",
        {
            "latest_phones":
                PhoneBook.objects.order_by('-reg_date')[:5],
            "message": message
        }
    )
