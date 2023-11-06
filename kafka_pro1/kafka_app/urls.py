from .views import GetInput,ProduceData
from django.urls import path


urlpatterns = [
    path('input/', GetInput.as_view()),
    path('produce/', ProduceData.as_view())
]