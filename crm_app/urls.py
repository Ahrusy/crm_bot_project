from django.urls import path
from .views import AgentInfoView  # импортируем только нужный класс

urlpatterns = [
    path('agent/<int:telegram_id>/', AgentInfoView.as_view(), name='agent-info'),
    # убираем дублирование и несуществующий маршрут
    # path('api/user-info/', views.get_user_info, name='user_info'),  # убираем, т.к. функции нет
]
