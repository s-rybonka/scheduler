from django.views.generic import TemplateView


class CalendarTemplateView(TemplateView):
	template_name = 'day_books/calendar.html'