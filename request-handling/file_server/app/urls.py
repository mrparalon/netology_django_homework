from django.urls import path, re_path
from app.views import file_list, file_content
# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам


urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path('', file_list, name='file_list'),
    re_path(r'^(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})/', file_list, name='file_list'),
    path('<name>/', file_content, name='file_content'),
]
