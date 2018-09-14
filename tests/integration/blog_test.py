from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('Test', 'Test author')
        b.create_post('Test Post', 'Test Content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test Content')

    def test_blog_repr(self):
        b = Blog('Test', 'Test author')

        self.assertEqual(str(b), 'Test by Test author (0 posts)')

    def test_json_with_posts(self):
        b = Blog('Test', 'Test author')
        b.create_post('Test Post', 'Test Content')

        expected = {
            'title': 'Test',
            'author': 'Test author',
            'posts': [
                {
                    'title': 'Test Post',
                    'content': 'Test Content'
                }
            ]
        }
        self.assertDictEqual(b.json(), expected)

    def test_json_no_posts(self):
        b = Blog('Test', 'Test author')

        expected = {
            'title': b.title,
            'author': b.author,
            'posts': [],
        }

        self.assertDictEqual(b.json(), expected)
