from django.db import models


class Base(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    nome = models.CharField(max_length=50, unique=True )

    def __str__(self):
        return self.nome

class Projeto(Base):
    titulo = models.CharField(max_length=50, unique=True)
    descricao = models.TextField()
    link_github = models.URLField()
    link_demo = models.URLField(blank=True)
    destaque = models.BooleanField(default=False)    
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    tecnologia = models.ManyToManyField(Tecnologia)

    def __str__(self):
        return self.titulo
    

class Perfil(Base):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    lida = models.BooleanField(default=False)

class Contato(Base):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    lida = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome} - {self-self.email}"