from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=12)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo