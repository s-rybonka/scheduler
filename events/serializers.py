from django.utils import timezone as dj_timezone
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
			'id', 'title', 'description', 'start_date_time', 'end_date_time', 'abs_uri',
		)
		extra_kwargs = {
			'start_date_time': {
				'error_messages': {
					'invalid': _(
						'Invalid datetime. Supported format: YYYY-MM-DD HH:mm'
					)
				}
			},
			'end_date_time': {
				'error_messages': {
					'invalid': _(
						'Invalid datetime. Supported format: YYYY-MM-DD HH:mm'
					)
				}
			}
		}

	def validate(self, attrs):
		start_date_time = attrs.get('start_date_time')
		end_date_time = attrs.get('end_date_time')
		if start_date_time < dj_timezone.now():
			raise serializers.ValidationError({
				'start_date_time': _(
					'Value must contains future date and/or time.'
				)
			})
		elif start_date_time >= end_date_time:
			raise serializers.ValidationError({
				'start_date_time': _(
					'Value must be less then event date and/or time.'
				)
			})
		return attrs

	def get_abs_uri(self, event):
		if 'request' in self.context:
			request = self.context['request']
			detail_uri = request.build_absolute_uri(
				event.detail_uri
			)
		else:
			detail_uri = ''
		return detail_uri
