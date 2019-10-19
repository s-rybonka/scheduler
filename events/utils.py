from drf_yasg import openapi

from events.serializers import MessageSerializer


def get_default_schema_responses(success_response):
    responses = {
        '400': openapi.Response(
            'Bad request.',
            schema=MessageSerializer,
        ),
        '404': openapi.Response(
            'Not found.',
            schema=MessageSerializer,
        ),
        '405': openapi.Response(
            'Method not allowed.',
            schema=MessageSerializer,
        ),
    }
    responses = responses.copy()
    responses.update(success_response)
    return responses