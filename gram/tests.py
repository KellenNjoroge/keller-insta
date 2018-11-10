from django.test import TestCase
from .models import *
# Create your tests here.

class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(username = 'Keller ', email = 'kell@kell.com', password = 'passwadd')
        self.ras = Profile(bio = 'A python Programmer',contact = '054234444', user = self.user)

    def tearDown(self):
        self.user.delete()
        self.ras.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.ras,Profile))
        self.assertTrue(isinstance(self.user,User))

    # def test_save(self):
    #     self.ras.create_user_profile()
    #     self.ras.save_user_profile(self.user)
    #     users = Profile.objects.all()
    #     self.assertTrue(len(users)>0)


class ImageTest(TestCase):
    def setUp(self):
        self.user = User(username='Ras_Kwesi', email='ras@ras.com', password='passwadd')
        self.ras = Profile(bio='A python Programmer', contact='054234444', user=self.user)
        self.one = Image(caption = 'You only live once', image='YOLO', profile=self.user, likes=2)

    def tearDown(self):
        self.user.delete()
        self.ras.delete()
        self.one.delete()

    def test_save(self):
        self.one.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
