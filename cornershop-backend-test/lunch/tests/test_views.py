from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status


class MenuViewsTestCalls(TestCase):
    def setUp(self):
        """
        Setup menu views test
        """
        self.user = User.objects.create_user(
            username='nora', email='nora@nora.com', password='top_secret')

    def test_call_view_deny_anonymous(self):
        """
         menu add login test
        """
        response = self.client.get('/menu/add/', follow=True)
        self.assertRedirects(response, '/login?next=/menu/add/')

    def test_call_view_load(self):
        """
        menu template test
        """
        self.client.login(username='nora', password='top_secret')
        response = self.client.get('/menu/add/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lunch/index.html')

    def test_call_view_permision(self):
        """test permission"""
        self.client.login(username='nora', password='top_secret')
        form_data = {'name': 'menu1', 'message': 'que tal'}
        response = self.client.post('/menu/add/', form_data)
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)
