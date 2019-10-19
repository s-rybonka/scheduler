from dateutil import parser
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
			'start_date_time': '2019-12-12 10:00:00',
			'end_date_time': '2019-12-12 12:00:00',
		}

		response = self.client.post(
			self.end_list_url,
			data=payload,
		)
		data = response.data

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(payload['title'], data['title'])
		self.assertEqual(
			parser.parse(data['start_date_time'][:-6]),
			parser.parse(payload['start_date_time'])
		)
		self.assertEqual(
			parser.parse(data['end_date_time'][:-6]),
			parser.parse(payload['end_date_time'])
		)

	def test_create_event_failure(self):
		payload = {
			'title': '',
			'description': '',
			'start_date_time': '2019/12/12 10:00:00',
			'end_date_time': '2019/12/12 12:00:00',
		}

		response = self.client.post(
			self.end_list_url,
			data=payload,
		)
		data = response.data

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

		required_attrs = list(payload.keys())
		invalid_attrs = list(data.keys())

		self.assertEqual(required_attrs.sort(), invalid_attrs.sort())

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
		self.assertEqual(event.title, data['title'])
		self.assertEqual(event.description, data['description'])
		self.assertEqual(
			event.start_date_time,
			parser.parse(data['start_date_time'])
		)
		self.assertEqual(
			event.end_date_time,
			parser.parse(data['end_date_time'])
		)

	def test_update_event_success(self):
		event = mixer.blend(Event)
		payload = {
			'title': faker.sentence(
				nb_words=3,
				variable_nb_words=True,
				ext_word_list=None,
			),
			'description': faker.sentence(
				nb_words=3,
				variable_nb_words=True,
				ext_word_list=None,
			),
			'start_date_time': '2019-10-21 9:00:00',
			'end_date_time': '2019-10-22 11:00:00',
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
		self.assertEqual(payload['title'], data['title'])
		self.assertEqual(payload['description'], data['description'])
		self.assertEqual(
			parser.parse(payload['start_date_time']),
			parser.parse(data['start_date_time'][:-6]),
		)
		self.assertEqual(
			parser.parse(payload['end_date_time']),
			parser.parse(data['end_date_time'][:-6]),
		)

	def test_update_event_failure(self):
		event = mixer.blend(Event)
		payload = {
			'title': '',
			'description': '',
			'start_date_time': '2019-10-24 9:00:00',
			'end_date_time': '2019-10-23 11:00:00',
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

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

		required_attrs = list(payload.keys())
		invalid_attrs = list(data.keys())

		self.assertEqual(required_attrs.sort(), invalid_attrs.sort())


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
		self.assertFalse(response.data)

	def test_delete_event_failure(self):
		fake_event_id = 77
		end_detail_url = reverse(
			'api:events:event-detail',
			args=(fake_event_id,)
		)
		response = self.client.delete(
			end_detail_url
		)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

