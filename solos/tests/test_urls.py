from django.test import TestCase
from django.urls  import resolve


from solos.views import index


class SolosURLsTestCase(TestCase):
    
    def test_root_url_uses_index_view(self):
        """
            Test that the root of the site resolves to the
            correct view function
        """
        root = resolve('/')
        self.assertEqual(root.func, index)
        
    def test_solo_detail_url(self):
        """Test that url for SoloDetail resolves 
           to the correct view function
        """
        solo_detail = resolve('/solos/1') 
        self.assertEqual(solo_detail.func.__name__, 'SoloDetailView')
        self.assertDictEqual(solo_detail.kwargs['pk'], '1')