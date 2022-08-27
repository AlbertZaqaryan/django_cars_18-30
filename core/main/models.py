from django.db import models

# Create your models here.
class HomeSlider(models.Model):
    name1 = models.CharField('Slider name1', max_length=30)
    name2 = models.CharField('Slider name2', max_length=30)
    about = models.TextField('Slider about')
    img = models.ImageField('Slider image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeSlider'
        verbose_name_plural = 'HomeSliders'
