from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}. {self.tag}'


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.id}. {self.title}'