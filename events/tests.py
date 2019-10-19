from django.urls import reverse
from mixer.backend.django import faker
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APITestCase as DRF_APITestCase

from events.models import Event


class EventAPITestCase(DRF_APITestCase):

	@classmethod
	def setUpTestData(cls):
		cls.end_list_url = reverse('api:events:event-list')

	def test_create_event_success(self):
		payload = {
			'title': faker.sentence(
				nb_words=4,
				variable_nb_words=True,
				ext_word_list=None,
			),
			'description': faker.sentence(
				nb_words=10,
				variable_nb_words=True,
				ext_word_list=None,
			),
			'start_date_time': '2019-12-12 10:00',
			'end_date_time': '2019-12-12 12:00',
		}
		response = self.client.post(
			self.end_list_url,
			data=payload,
		)
		data = response.data

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(data['title'], payload['title'])
		self.assertEqual(data['description'], payload['description'])

	def test_get_event_list_success(self):
		mixer.cycle(50).blend(Event)
		response = self.client.get(
			self.end_list_url
		)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), Event.objects.count())

	def test_get_event_detail_success(self):
		event = mixer.blend(Event)
		end_detail_url = reverse(
			'api:events:event-detail',
			args=(event.id,)
		)
		response = self.client.get(end_detail_url)
		data = response.data

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(data['title'], event.title)
		self.assertEqual(data['description'], event.description)

	def test_update_event_success(self):
		event = mixer.blend(Event)
		payload = {
			'title': faker.sentence(
				nb_words=3,
				variable_nb_words=True,
				ext_word_list=None,
			),
		}
		end_detail_url = reverse(
			'api:events:event-detail',
			args=(event.id,)
		)
		response = self.client.patch(
			end_detail_url,
			data=payload
		)
		data = response.data

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(data['title'], payload['title'])
		self.assertEqual(data['description'], event.description)

	def test_delete_event_success(self):
		event = mixer.blend(Event)
		end_detail_url = reverse(
			'api:events:event-detail',
			args=(event.id,)
		)
		response = self.client.delete(
			end_detail_url
		)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
