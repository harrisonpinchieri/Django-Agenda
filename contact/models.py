from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    nome = models.CharField('Categoria', max_length=50)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome


class Contact(models.Model):
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=50)
    phone = models.CharField('Telefone', max_length=50)
    # blank = true  caso não queira que seja obrigatório
    email = models.EmailField('Email', max_length=200)
    create_date = models.DateTimeField('Criação', auto_now_add=True)
    description = models.TextField('Descrição', blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True
                                 )
    owner = models.ForeignKey(User,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True
                              )

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.first_name
