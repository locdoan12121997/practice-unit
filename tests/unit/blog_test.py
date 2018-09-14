from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Martin Blog', 'Martini Blogas')

        self.assertEqual('Martin Blog', b.title)
        self.assertEqual('Martini Blogas', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
