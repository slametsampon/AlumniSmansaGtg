from django.test import TestCase
from django.contrib.auth import get_user_model


class AlumniSmansaUserTest(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'will', 
            email = 'will@email.com', 
            address = 'maron', 
            mobile_number = '0811-3323-706', 
            bio = 'short bio', 
            password = 'test123')
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@email.com')
        self.assertEqual(user.address, 'maron')
        self.assertEqual(user.mobile_number, '0811-3323-706')
        self.assertEqual(user.bio, 'short bio')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
        
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username = 'willSuper', 
            email = 'willSuper@email.com', 
            address = 'maron', 
            mobile_number = '0811-3323-706', 
            bio = 'short bio', 
            password = 'test123')
        self.assertEqual(admin_user.username, 'willSuper')
        self.assertEqual(admin_user.email, 'willSuper@email.com')
        self.assertEqual(admin_user.email, 'willSuper@email.com')
        self.assertEqual(admin_user.address, 'maron')
        self.assertEqual(admin_user.mobile_number, '0811-3323-706')
        self.assertEqual(admin_user.bio, 'short bio')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        
        
