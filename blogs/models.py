from django.db import models

# Create your models here.
class BlogPost(models.Model):
    '''A blog'''
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Return a string representation of the model.'''
        return self.title

    def __str__(self):
        '''Return a string representation of the model.'''    
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text