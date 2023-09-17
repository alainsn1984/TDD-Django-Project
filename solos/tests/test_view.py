from django.test import TestCase, RequestFactory
from django.db.models import QuerySet
from solos.views import index
from solos.models import Solo

class IndexViewTestCase(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        self.drum_solo = Solo.objects.create(
            instrument='Guitar',
            artist='Ricardo Arjona',
            track='El Problema'
        )
        self.bass_solo = Solo.objects.create(
            instrument='saxphone',
            artist='Coltrane',
            track='Mr. PC'
        )
        
    def test_index_view_basic(self):
        """
            Test the index view return a 200 response
            and uses the correct template
        """
        request = self.factory.get('/')
        with self.assertTemplateUsed('solos/index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)
    
    def test_index_view_return_solos(self):
        """
            Test that the index view  will attempt to return
            solos if query parameters exits.
        """
        response = self.client.get('/', {'instruments':'drums'})
        solos = response.context['solos']
        self.assertIs(type(solos), QuerySet)
        self.assertEqual(len(solos), 1)
        self.assertEqual(solos[0].artist, 'Ricardo Arjona')