from django.contrib import admin
from django.urls import path
from simp_web import views #추가

from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('설정할 url', views.뷰 이름, name='뷰 이름'),을 url 개수만큼 추가
    # 글 관련 url부터 추가함.
    path('simp_web/page', views.page, name='page'),
    path('simp_web/page/memo', views.memo, name='memo'),
    path('simp_web/page/memo/update', views.update, name='update'),
    path('simp_web/page/memo/delete', views.delete, name='delete'),
    path('simp_web/page/memo/create', views.create, name='create'),
]