from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # 아무것도 입력되지 않았을경우 views모듈의 index()로
]