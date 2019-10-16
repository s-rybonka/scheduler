from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class Event(TimeStampedModel):
	title = models.CharField(
		max_length=200,
		verbose_name=_('title')
	)
	description = models.CharField(
		max_length=500,
		verbose_name=_('description'),
	)
	start_date = models.DateField(
		verbose_name=_('start date'),
	)
	end_date = models.DateField(
		verbose_name=_('end date'),
	)
	start_time = models.TimeField(
		verbose_name=_('start time'),
	)
	end_time = models.TimeField(
		verbose_name=_('end time'),
	)

	class Meta:
		verbose_name = _('Event')
		verbose_name_plural = _('Events')
		ordering = ('id',)

	def __str__(self):
		return self.title
