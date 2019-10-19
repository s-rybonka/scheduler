from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from rest_framework.reverse import reverse


class Event(TimeStampedModel):
	title = models.CharField(
		max_length=200,
		verbose_name=_('title')
	)
	description = models.CharField(
		max_length=500,
		verbose_name=_('description'),
	)
	start_date_time = models.DateTimeField(
		verbose_name=_('start'),
	)
	end_date_time = models.DateTimeField(
		verbose_name=_('end'),
	)

	class Meta:
		verbose_name = _('Event')
		verbose_name_plural = _('Events')
		ordering = ('id',)

	def __str__(self):
		return self.title

	@property
	def relative_uri(self):
		return reverse(
			'api:events:event-detail',
			kwargs={
				'pk': self.pk
			}
		)
