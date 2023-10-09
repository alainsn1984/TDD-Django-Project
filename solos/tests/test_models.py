from django.test import TestCase

from solos.models import Solo

class SoloModelTestCase(TestCase):
    
    def setUp(self):
        self.solo  = Solo.objects.create(
            track='Jerusalem',
            artist='Bob Marley',
            instrument='Guitar'
        )
    
    def test_solo_basic(self):
        """Test the basic functionality of Solo
        """
        self.assertEqual(self.solo.artist, 'Bob Marley')
        
