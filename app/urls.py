from django.urls import path
from app.views import index, cadastrar_bloco

urlpatterns = [
    path('', index, name='index'),
    path('bloco/cadastrar', cadastrar_bloco, name='cadastrar'),
]
