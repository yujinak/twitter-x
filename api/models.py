from django.db import models
from django.contrib.auth.models import User

# class Tweet(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.CharField(max_length=280)
#     created_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField( # 1:1, cada user tem 1 profile
        User, 
        on_delete=models.CASCADE # se o user for deletado, o mesmo acontece com o profile
        )
    follows = models.ManyToManyField(
        'self',
        related_name='followed_by',
        symmetrical=False, # uma pessoa que segue não necessariamente precisa seguir
        blank=True # pode não seguir ninguém
    )
    