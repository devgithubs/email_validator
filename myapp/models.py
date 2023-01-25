from django.db import models

# word model.
class Word(models.Model):
    text = models.EmailField(max_length=255, 
                blank=False, 
                null=False, 
                unique=True, 
                error_messages ={"unique":"Email already exists."})

    def __str__(self):
        return self.text


class EmailTest(models.Model):
    email = models.EmailField()
    test_conditions = models.CharField(max_length=255, choices=[
        ('yahoo', 'Yahoo'),
        ('gmail', 'Gmail'),
        ('hotmail', 'Hotmail'),
        ('valid', 'Valid')
    ])



    