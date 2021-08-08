import django_filters

from home.models import Post

class OrderFilter(django_filters.FilterSet):


    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }
        exclude = ['image', 'link', 'link_title'] 
