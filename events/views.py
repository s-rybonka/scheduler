from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet

from events.utils import get_default_schema_responses
from events import models as events_models
from events import serializers as events_serializers


@method_decorator(
	name='list', decorator=swagger_auto_schema(
		responses=get_default_schema_responses({
			'200': events_serializers.EventModelSerializer,
		}),
		operation_id='event_list',
	)
)
@method_decorator(
	name='create', decorator=swagger_auto_schema(
		responses=get_default_schema_responses({
			'201': events_serializers.EventModelSerializer,
		}),
		operation_id='event_create',
	)
)
@method_decorator(
	name='retrieve', decorator=swagger_auto_schema(
		responses=get_default_schema_responses({
			'200': events_serializers.EventModelSerializer,
		}),
		operation_id='event_detail',
	)
)
@method_decorator(
	name='partial_update', decorator=swagger_auto_schema(
		responses=get_default_schema_responses({
			'200': events_serializers.EventModelSerializer,
		}),
		operation_id='event_update',
	)
)
@method_decorator(
	name='destroy', decorator=swagger_auto_schema(
		responses=get_default_schema_responses({
			'204': openapi.Response(
				'No content.',
			)
		}),
		operation_id='event_destroy',
	)
)
class EventModelViewSet(ModelViewSet):
	serializer_class = events_serializers.EventModelSerializer
	http_method_names = ['get', 'post', 'patch', 'delete']
	def create(self, request, *args, **kwargs):
		print(request.data)
		print('post')
		return super().create(request, *args, **kwargs)

	def destroy(self, request, *args, **kwargs):
		print(request.data)
		print('delete')
		return super().destroy(self, request, *args, **kwargs)

	def update(self, request, *args, **kwargs):
		print(request.data)
		print('patch')
		return super().update(request, *args, **kwargs)

	def get_queryset(self):
		return events_models.Event.objects.all()
