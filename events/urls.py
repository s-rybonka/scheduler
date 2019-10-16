from django.urls import include
from django.urls import path
from rest_framework import routers

from events import views as events_views

router = routers.SimpleRouter()

router.register(r'events', events_views.EventModelViewSet, basename='event')

app_name = 'events'

urlpatterns = [
	path('', include(router.urls)),
]
