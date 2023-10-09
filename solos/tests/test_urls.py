from django.test import TestCase
from django.urls  import resolve


from solos.views import index, SoloDetailView


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
        view = resolve('/solos/1/') 
        self.assertEqual(view.func.__name__, SoloDetailView.as_view().__name__)
        self.assertEqual(view.kwargs['pk'], '1')