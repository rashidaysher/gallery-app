from django.test import TestCase

# Create your tests here.
from .models import Category,Location,Image
import datetime as dt

class LocationTestCase(TestCase):
    def setUp(self):
        Location.objects.create(name='Kenya')
        self.name = Location(name='Kenya')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.name,Location))
        
class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='Food')
        self.name = Category(name='Food')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.name,Category))
    
class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.save()

        self.pic_category = Category(name='home')
        self.pic_category.save()

        self.picture_test = Image(id=1, picture='picture.jpg', description='this is a test picture', location=self.location,
                                pic_category=self.pic_category)

    def test_instance(self):
        self.assertTrue(isinstance(self.picture_test, Image))

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_update_picture(self):
        self.picture_test.save_image()
        self.picture_test.update_image(self.picture_test.id, 'picha/test.jpg')
        changed_img = Image.objects.filter(image='picha/test.jpg')
        self.assertTrue(len(changed_img) > 0)


    def test_save_image(self):
        self.picture_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.picture_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)


