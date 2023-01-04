from django.urls import path
from . import views
app_name = "homepage"
urlpatterns = [
    path('', views.TrangChu, name = "trangchu"),
    path("result/", views.KetQua, name = 'ketqua' )
]
