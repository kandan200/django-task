from django import forms
from .models import Post

class BlogForms(form):
            class Meta:
                        model= Post
                        fields =[
                                    'title',
                                    'text',
                                    'created_date',
                                    'publisheddate',
                        ]