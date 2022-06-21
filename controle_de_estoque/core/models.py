from django.db import models

class TimeStampedModel(models.Model):
    # Esta função atualiza a data
    # apenas quando algo é criado
    created = models.DateTimeField(
        'Criado em',
        auto_now_add=True,
        auto_now=False
    )
    # Atualiza a data e hora quando
    # modificamos um registro
    modified = models.DateTimeField(
        'Criado em',
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        abstract = True 
