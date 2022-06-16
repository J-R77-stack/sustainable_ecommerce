from django.db import models

class ContactUs(models.Model):

    class Meta:
        verbose_name_plural = 'Contact Us'

    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.email
