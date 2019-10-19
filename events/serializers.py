from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from events.models import Event


class MessageSerializer(serializers.Serializer):
	detail = serializers.CharField(label=_('detail'), required=False)


class EventModelSerializer(serializers.ModelSerializer):
	abs_uri = serializers.SerializerMethodField()
	class Meta:
		model = Event
		fields = (
			'id', 'title', 'description', 'start_date_time', 'end_date_time' ,'abs_uri',
		)

	def get_abs_uri(self, event):
		if 'request' in self.context:
			request = self.context['request']
			detail_uri = request.build_absolute_uri(
				event.relative_uri
			)
		else:
			detail_uri = ''
		return detail_uri