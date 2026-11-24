from django.test import TestCase

from .models import Post


class PostTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            titulo="Meu Primeiro Post!",
            corpo="Olá, mundo.",
        )

    def test_slug_gerado_do_titulo(self):
        self.assertEqual(self.post.slug, "meu-primeiro-post")

    def test_nasce_como_rascunho(self):
        self.assertEqual(self.post.status, Post.Status.RASCUNHO)

    def test_str_mostra_o_titulo(self):
        self.assertEqual(str(self.post), "Meu Primeiro Post!")