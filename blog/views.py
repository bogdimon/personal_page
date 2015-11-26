from django.shortcuts import render
from models import Item
import datetime

# Create your views here.
# Titlepage



# Blog views
def blog_index(request):
    items = Item.objects.order_by("-publish_date")
    now = datetime.datetime.now()
    return render(request, 'blog/index.html', {"items": items, "year": now.year, "cur_page": "blog_index"})

def post_detail(request, post_id):
    item = Item.objects.get(pk=post_id)
    return render(request,'blog/post.html', {"item": item, "cur_page": "blog_index"})


def develop(request):
	return render(request, 'blog/titlepage1.html')