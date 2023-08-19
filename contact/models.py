from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=50)
    phone = models.CharField('Telefone', max_length=50)
    # blank = true  caso não queira que seja obrigatório
    email = models.EmailField('Email', max_length=200)
    create_date = models.DateTimeField('Criação', auto_now_add=True)
    description = models.TextField('Descrição', blank=True)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.first_name
