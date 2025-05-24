from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)

    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        """
        This function tells Django that the ultimate location of a Post entry is 
        its post_detail view which is posts/<int:pk>

        So that every time a new post is created, the function will be called 

        Reverse is a very handy utility function Django provides us to reference an object by its URL
        template name, in this case post_detail.
        In this case, the template for post_details requires a primary key argument: path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
        """
        return reverse('post_detail', args=[str(self.id)])