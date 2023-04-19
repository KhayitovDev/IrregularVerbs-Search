from django.db import models


class Word(models.Model):
    first_form=models.CharField(max_length=255)
    second_form=models.CharField(max_length=255)
    third_form=models.CharField(max_length=255)
    translation=models.CharField(max_length=255, blank=True)
    example_first=models.TextField(blank=True)
    example_second=models.TextField(blank=True)
    example_third=models.TextField(blank=True)
    url=models.URLField(blank=True)


    def __str__(self) -> str:
        return self.first_form
    
    class Meta:
        ordering=['-first_form']

    
