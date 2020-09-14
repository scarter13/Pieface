from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from tastypie.utils.timezone import now


class Whatever(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Entry(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=now)
    title = models.CharField(max_length=200)
    slug = models.TextField()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        #for automatic slug generation
        if not self.slug:
            self.slug = slugify(self.title)[:50]

        return super(Entry, self).save(*args, **kwargs)

"""
Note that def __unicode__ is recommended development practice.  It takes the place of a __str__ method, which is used to create a readable name that can be displayed; most notably, on the Django admin site as the value inserted into a template when it displays an object.  Unicode, unlike str, will convert the result correctly to a UTF-8 encoded string object.  For more information, check out the docs at https://docs.djangoproject.com/en/1.8/ref/models/instances/#unicode
"""