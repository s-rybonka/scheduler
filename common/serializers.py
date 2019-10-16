from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
	detail = serializers.CharField(label=_('detail'), required=False)
