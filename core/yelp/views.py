from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Restaurant, Tag

# Create your views here.
def homepage(request):
    if request.method == "GET":
        restaurants = Restaurant.objects.all()
        all_tags = set([tag.tag_field for tag in Tag.objects.all()])
        context = {
                    "restaurants": restaurants,
                    "all_tags": all_tags
                   }
        return render(request, "index.html", context)
    else:
        return HttpResponse("Invalid, only GET method is allowed")
    
class TagFilterListView(ListView):
    model = Restaurant
    template_name = "index.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(TagFilterListView, self).get_context_data(*args, **kwargs)
        tag_t = self.request.GET.get("category", "").lower()
        tag = Tag.objects.get(tag_field = tag_t)
        results = Restaurant.objects.filter(tag=tag)
        context["restaurants"] = results
        return context

class PostDetailView(DetailView):
    model = Restaurant
    template_name = "post_detail.html"
    context_object_name = "object"


# from django.db.models import Q
# from myapp.models import MyModel
# # Assuming you have a ‘tags’ field in your model representing the tags
# tag1 = ‘tag1’
# tag2 = ‘tag2’
# # Filtering the model by multiple tags
# result = MyModel.objects.filter(Q(tags__contains=tag1) | Q(tags__contains=tag2))
# # Accessing the filtered results
# for item in result:
#     # Do something with the filtered items
#     print(item)