from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.all_news, name='allNews'),
    path('/today', views.news_today, name='newsToday'),
    path('archives/<str:date>', views.past_days_news, name='pastNews'),
    path('search/', views.search_results, name='search_results'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('logout/', views.logout, name='logout'),
    path('accounts/login', views.login, name='login'),
    path('new/article', views.new_article, name='new-article'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
