from django.db import models

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey('auth.User',related_name='todos',on_delete=models.CASCADE)
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField()
    completado = models.BooleanField(default=False)

    def _str_(self):
        return self.titulo

