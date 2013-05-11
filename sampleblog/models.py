# coding=utf-8
from django.db import models
from django.core.urlresolvers import reverse_lazy
from django.core.validators import MinLengthValidator
from django.utils.text import Truncator


class Post(models.Model):
    """ Blog post """
    title = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    contents = models.TextField()
    date_published = models.DateTimeField('Published', auto_now_add=True)
    
    class Meta:
        ordering = ['-date_published']
    
    def __unicode__(self):
        return '%s (%s)' % (self.title, self.date_published)
    
    def get_absolute_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.pk})
    
    def get_title_shortened(self):
        return Truncator(self.title).chars(50)
    get_title_shortened.short_description = 'Title'
    
    def get_excerpts(self):
        return Truncator(self.contents).words(100, html=True)
    get_excerpts.short_description = 'Excerpts'
