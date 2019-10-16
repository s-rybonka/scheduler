from rest_framework import serializers

from events.models import Event


class EventModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = (
			'title', 'description', 'start_date', 'end_date', 'start_time',
			'end_time'
		)
