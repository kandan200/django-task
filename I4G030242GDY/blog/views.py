from django.views.generic.edit import CreateView
from .models import Post, Push

class bblogview(CreateView):
            model = Post
            fields =[
                        'title',
                        'text',
                        'created_date',
                        'publisheddate',
            ]
template = 'home.html'
# Create your views here.
