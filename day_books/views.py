from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
	template_name = 'day_books/home.html'


class CalendarTemplateView(TemplateView):
	template_name = 'day_books/calendar.html'