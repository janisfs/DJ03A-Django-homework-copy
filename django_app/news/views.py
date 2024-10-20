from django.shortcuts import render
from .models import News_post

# Create your views here.
def news_home(request):
    news = News_post.objects.all() # Получаем все новости из базы данных
    return render(request, 'news/news_home.html', {'news': news})  # путь к файлу шаблона
