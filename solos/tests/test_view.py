from django.test import TestCase, RequestFactory
from django.db.models import QuerySet
from solos.views import index, SoloDetailView
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
        self.assertEqual(len(solos), 2)
        self.assertEqual(solos[0].artist, 'Ricardo Arjona')
        
class SoloViewTest(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
    
    def test_base(self):
        """Test that a solo view return a 200 response, uses
           the correct template and has a correct context
        """
        request = self.factory.get('/solos/1/')
        response = SoloDetailView.as_view()(request, self.drum_solo.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual( response.context_data['solo'].artist,'Rich' )
        with self.assertTemplateUsed('solos/solo_detail.html'):
            response.render()
