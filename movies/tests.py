from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


from.models import Movie
# from .forms import NameForm

# Create your tests here.


class MovieTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test', email='test@test.com',
            password='test@12345'
        )
        self.movie = Movie.objects.create(
            name="Test",
            user=self.user,
            description='test',
        )

    def test_list_status(self):
        url = reverse("movie_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_template(self):
        url = reverse("movie_list")
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'movies/movie_list.html')

    def test_str_method(self):
        self.assertEqual(str(self.movie), 'Test')

    def test_detail_view(self):
        url = reverse('movie_detail', args=[self.movie.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/movie_detail.html')

    def test_create_view(self):
        url = reverse('movie_create')
        data = {
            "name": "Test Create",
            "user": self.user.id,
            "description": "test desc",
        }
        response = self.client.post(path=url, data=data, follow=True)
        self.assertTemplateUsed(response, 'movies/movie_list.html')
        self.assertEqual(len(Movie.objects.all()), 2)
        self.assertRedirects(response, reverse('movie_list'))

    # def test_my_view(self):
    #     data = {
    #     ‘param’: ‘fiesta’
    #     }
    #     response = self.client.post(reverse(‘my - view), data)
    #     assertEqual(response, ‘fiesta’)
    # def test_update_view(self):
    #     data = {
    #         "name": "Test Update",
    #         # "user": self.user.id,
    #         "description": "test desc update",
    #     }
    #
    #     url = reverse('movie_update', args=[self.movie.id])
    #     # movie_name = data['name']
    #     # movie_name = self.movie.name
    #     # print(movie_name)
    #     # response = self.client.put(url, kwargs={"description": "desc"})
    #     response = self.client.put(path=url, data=data, follow=True)
    #
    #     print(response.content)
    #     # response = self.client.post(path=url, data=data, follow=True)
    #     self.assertTemplateUsed(response, 'movies/movie_update.html')
    #     # self.assertRedirects(response, reverse('movie_update', args=[1]))
    #     self.assertEqual(self.movie.description, 'test desc')

    def test_update_view(self):
        data = {
            "name": "Test Update",
            "user": self.user.id,
            "description": "test desc update",
        }

        url = reverse('movie_update', args=[self.movie.id])
        movie_name = self.movie.name
        response = self.client.put(path=url, data=data, follow=True)
        # print(response.content)
        # response = self.client.post(path=url, data=data, follow=True)
        self.assertTemplateUsed(response, 'movies/movie_update.html')
        # self.assertRedirects(response, reverse('movie_update', args=[self.user.id]))
        # self.assertEqual(self.movie.description, 'test desc')

    def test_delete_view(self):
        url = reverse('movie_delete', args=[self.movie.id])
        response = self.client.post(path=url, follow=True)
        self.assertTemplateUsed(response, "movies/movie_list.html")
        self.assertRedirects(response, reverse("movie_list"))

    def test_string_repr(self):
        movie = Movie(name="test")
        self.assertEqual(str(movie), movie.name)

    def test_fields(self):
        self.assertEqual(self.movie.name, 'Test')
        self.assertEqual(self.movie.user, self.user)
        self.assertEqual(self.movie.description, 'test')
