from django.urls import path
from . import views
urlpatterns = [
    path('', views.mainHome),
    path('news', views.NewSpisok, name='newspisok'),
    path('news/<int:idnew>', views.NewSite, name='newsite'),
    path('sveden/<slug:slug>', views.InfPOO, name='infpoosite'),
    path('main/<slug:slug>', views.Main, name='mainsite'),
    path('entrant/<slug:slug>', views.Entrant, name='entrantsite'),
    path('student/<slug:slug>', views.Student, name='studentsite'),
    path('graduate/<slug:slug>', views.Graduate, name='infv'),
    path('teacher/<slug:slug>', views.Teacher, name='teachersite'),
    path('panl/<slug:slug>', views.MenuPanel, name='panels'),
    path('findelement', views.FindElement, name='findelement'),
    path('driving-directions', views.DrivDiric, name='drivdiric'),
    path('card-info-site', views.CardInfoSite, name='cardinfosite'),
    path('d-site/<slug:slug>', views.DopSite, name='dopsite'),
    path('jsonpost', views.PostJson, name='postjson'),
]
