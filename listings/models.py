from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True
    )
    slug = models.SlugField(
        max_length=100,
        unique=True
    )
    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Register(models.Model):
    category = models.ForeignKey(
        Category,
        related_name = 'registers',
        on_delete = models.CASCADE
)
    price = models.IntegerField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', 'price',)

    def __str__(self):
        return self.created