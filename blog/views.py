from django.shortcuts import render
from models import Item
import datetime

# Create your views here.
# Titlepage

navigation = [
				{'urlname':'#', 'text':'home', 'icon':'glyphicon glyphicon-home'},
				{'urlname':'blog:blog_index', 'text':'blog', 'icon':'glyphicon glyphicon-pencil'},
			]



# Blog views
def blog_index(request):
    items = Item.objects.order_by("-publish_date")
    now = datetime.datetime.now()
    return render(request, 'blog/index.html', {"items": items, 'navitems':navigation})

def post_detail(request, post_id):
    item = Item.objects.get(pk=post_id)
    return render(request,'blog/post.html', {"item": item, 'navitems':navigation})


def develop(request):
	return render(request, 'blog/titlepage1.html', {'navitems': navigation})