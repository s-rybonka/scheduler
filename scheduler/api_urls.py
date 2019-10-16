from django.conf import settings
from django.urls import re_path, path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
	openapi.Info(
		title=settings.API_DOC_SCHEMA_TITLE,
		default_version='v1',
		description=settings.API_DOC_SCHEMA_DESCRIPTION,
		contact=openapi.Contact(email=settings.API_DOC_SCHEMA_AUTHOR_EMAIL),
		terms_of_service=settings.API_DOC_SCHEMA_AGREEMENT_URL,
		license=openapi.License(name=settings.API_DOC_SCHEMA_LICENCE),
	),
	url='',
	public=True,
)

app_name = 'api'

urlpatterns = [
	path(
		'docs/',
		schema_view.with_ui('redoc', cache_timeout=0), name='docs'),
	re_path(
		r'^swagger(?P<format>\.json)/$',
		schema_view.without_ui(cache_timeout=0),
		name='schema_json'
	),
	path('', include('events.urls', namespace='events'))
]
