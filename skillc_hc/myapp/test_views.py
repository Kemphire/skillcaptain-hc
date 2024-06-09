from django.test import TestCase, Client
from django.urls import reverse
from myapp.models import Profile

class ProfileCreationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("profile-get-or-create")
    
    def test_create_profile_with_missing_data(self):
        response = self.client.post(self.url, {"name":"himansh"})
        self.assertEquals(response.status_code,200)
        self.assertContains(response,"missing fields profile can't be created")
        self.assertEqual(Profile.objects.count(),0)
    
    def test_create_profile_with_all_data(self):
        response = self.client.post(self.url,{"name":"himansh","email":"himansh@gmail.com"})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Profile create sucessfully")
        self.assertEqual(Profile.objects.count(),1)
        profile_created = Profile.objects.first()
        self.assertEquals(profile_created.name,"himansh")
        self.assertEquals(profile_created.email,"himansh@gmail.com")

class PostDeletionTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile = Profile.objects.create(name="himansh",email="himansh@gmail.com")
        self.url = reverse("put-delete-get",kwargs={"pk":self.profile.pk})   

    def test_post_retrivial(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code,200)
        self.assertContains(response,self.profile.name)
        self.assertContains(response,self.profile.email)

    def test_post_delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(Profile.objects.count(),0)

    def test_post_update(self):
        response = self.client.patch(self.url,{"name":"shinchain"})
        self.assertEqual(response.status_code,200)
        self.assertEqual(Profile.objects.count(),1)
        self.assertEqual(Profile.objects.first().name,"shinchain")
        self.assertEqual(Profile.objects.first().email,self.profile.email)