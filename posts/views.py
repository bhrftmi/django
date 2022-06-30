from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect ,HttpResponseNotFound

from .models import post , comment
from django.shortcuts import render
from .forms import PostForm
from django.views import generic

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET','POST'])
def index(request):
    #return HttpResponse("</h>this is postview<h>")
    return Response({'name': 'Wiliiam'})

def post_list(request):
    posts = post.objects.all()
    context = {'posts': posts}
    return render(request,'posts/post_list.html',context=context)

class PostList(generic.ListView):
    queryset = post.objects.all()
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'




def post_detail(request, post_id):
    '''try:
        Post = post.objects.get(pk=post_id)
    except post.DoesNotExist:
        return HttpResponseNotFound('Post does not exist!')
    '''  #or
    Post = get_object_or_404(post,pk=post_id ) #404 werroe if post does not exis
    comments = comment.objects.filter(post=Post)
    context = {'post': Post , 'comments':comments}
    return render(request,'posts/post_detail.html',context=context)


class PostDetail(generic.DetailView):
    model = post
    template_name = 'posts/post_detail.html'
    def get_context_data(self, **kwargs): #for multiple context
        context = super(PostDetail,self).get_context_data()
        context['comments'] = comment.objects.filter(post=kwargs["object"].pk)
        return context



def post_create(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts/')
    else:
        form = PostForm()
    return render(request,'posts/post_create.html', {'form':form})