from django.db import models

# Create your models here.

class Topic(models.Model): # the parent class Model defines the basic functionality of a model
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)              # CharField is a piece of data made up of individual chars
                                                         # use it when you only need a small textfield
    date_added = models.DateTimeField(auto_now_add=True) # DateTimeField is a data type which stores a date and a time.
                                                         # 'auto_now_add' indicates this time is the present

    def __str__(self):
        """Return a string representation of the model"""
        return self.text

class Entry(models.Model):
    """Something specific learned in a topic"""
    topic = models.ForeignKey(Topic)                        # ForeignKey is a database term indicating a reference to
                                                            # something else in the database. The key is like a UUID, used
                                                            # to establish a connection between two pieces of data. IT IS USED
                                                            # FOR MANY-TO-ONE RELATIONSHIPS
    text = models.TextField()                               # NO SIZE LIMIT WOOT WOOT
    date_added = models.DateTimeField(auto_now_add=True)    # same as before ^^

    class Meta:                                             # nested class which holds extra information for managing the model
        verbose_name_plural = 'entries'                     # this tells Django what word to use when referring to more than one
                                                            # item. Otherwise, it would say "Entrys", which is why there is no
                                                            # meta class in Topic

    def __str__(self):
        """Return a string representation of the model"""
        if len(self.text) <= 50:
            return self.text
        else:
            return self.text[:50] + "..."                       # tells Django to only display the first 50 chars, and the ellipsis is
                                                            # to illustrate this point
