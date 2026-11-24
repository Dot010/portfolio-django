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

        

class PostViewsTest(TestCase):
    def setUp(self):
        self.publicado = Post.objects.create(
            titulo="Post Publicado",
            corpo="Pode ler.",
            status=Post.Status.PUBLICADO,
        )
        self.rascunho = Post.objects.create(
            titulo="Post Rascunho",
            corpo="Ainda não.",
        )

    def test_lista_mostra_so_publicados(self):
        resposta = self.client.get("/blog/")
        self.assertContains(resposta, "Post Publicado")
        self.assertNotContains(resposta, "Post Rascunho")

    def test_detalhe_do_publicado_abre(self):
        resposta = self.client.get("/blog/post-publicado/")
        self.assertEqual(resposta.status_code, 200)

    def test_detalhe_do_rascunho_da_404(self):
        resposta = self.client.get("/blog/post-rascunho/")
        self.assertEqual(resposta.status_code, 404)