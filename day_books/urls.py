from django.urls import path
from day_books import views as day_books_views

app_name = 'day_books'

urlpatterns = [
	path(
		'home/',
		day_books_views.HomeTemplateView.as_view(),
		name='home_page',
	),
	path(
		'calendar/',
		day_books_views.CalendarTemplateView.as_view(),
		name='calendar',
	)
]
