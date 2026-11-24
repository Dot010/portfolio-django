from django.test import TestCase

from .models import Categoria, Contato, Projeto, Tecnologia


class CategoriaTest(TestCase):
    def test_str_mostra_o_nome(self):
        categoria = Categoria.objects.create(nome="Backend")
        self.assertEqual(str(categoria), "Backend")


class TecnologiaTest(TestCase):
    def test_str_mostra_o_nome(self):
        tecnologia = Tecnologia.objects.create(nome="Django")
        self.assertEqual(str(tecnologia), "Django")


class ProjetoTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Backend")
        self.django = Tecnologia.objects.create(nome="Django")
        self.projeto = Projeto.objects.create(
            titulo="Mini ERP",
            descricao="Sistema para mercadinho",
            link_github="https://github.com/Dot010/mini-erp-mercadinho",
            categoria=self.categoria,
        )
        self.projeto.tecnologia.add(self.django)

    def test_str_mostra_o_titulo(self):
        self.assertEqual(str(self.projeto), "Mini ERP")

    def test_destaque_comeca_falso(self):
        self.assertFalse(self.projeto.destaque)

    def test_projeto_tem_a_tecnologia(self):
        self.assertIn(self.django, self.projeto.tecnologia.all())

    def test_datas_preenchidas_sozinhas(self):
        self.assertIsNotNone(self.projeto.criado_em)
        self.assertIsNotNone(self.projeto.atualizado_em)


class ContatoTest(TestCase):
    def test_str_mostra_nome_e_email(self):
        contato = Contato.objects.create(
            nome="Ana",
            email="ana@email.com",
            mensagem="Oi!",
        )
        self.assertEqual(str(contato), "Ana - ana@email.com")