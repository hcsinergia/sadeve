from django.contrib.gis.gdal import feature
from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse

from django.shortcuts import render
from .models import Post
from marketing.models import Signup

from django.views.generic import TemplateView


from apps.slider_manager.models import slider


class Estatuto(TemplateView):
    template_name = 'estatuto.html'


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    # if query:
    #     for dato in query:
    #         print(dato)

    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_results.html', context)
  
def get_category_count():
    queryset = Post \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))

    # if queryset:
    #     for dato in queryset:
    #         print(Post.objects.values('categories__title'))

    return queryset



def index(request):

    queryset = slider.objects.all()
    
    featured = Post.objects.filter(featured=True).order_by('-timestamp')
    latest = Post.objects.order_by('-timestamp')
    #latest = Post.objects.order_by('-created_at')
    #latest = Post.objects.order_by('-created_on')
    #queryset = Post.objects.filter(status=1).order_by('-created_on')
    
    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
           
    context = {
        'featured_posts': featured,
        'latest': latest,
        'slider_data': queryset[0]
    }
    # print('imprimo:'+ str(queryset[0]))
    return render(request, 'index.html', context)


def contact(request):

    return render(request, 'contact-form.html')



def blog(request):
    category_count = get_category_count()
    #print(category_count)
    category_count = get_category_count() # categorias
    featured_posts = Post.objects.filter(featured=True).order_by('-timestamp') #destacados filtrados por el ultimo ingresado
    post_list = Post.objects.filter(is_post=True).order_by('-timestamp') #post filtrados por el ultimo ingresado
    

    # if post_list:
    #     for post in post_list:
    #         print(post)

    # if featured_posts:
    #     for destacado in featured_posts:
    #         print(destacado)

    paginator = Paginator(post_list, 4)#cantidad de paginas por post
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'featured': featured_posts,
        'page_request_var': page_request_var,
        'category_count': category_count
    }
    return render(request, 'blog.html', context)


def article(request):
    category_count = get_category_count()
    # featured_posts = Post.objects.filter(featured=True).order_by('-timestamp')[0:3]
    featured_posts = Post.objects.filter(featured=True).order_by('-timestamp')
    # post_list = Post.objects.filter(is_article=True).order_by('-timestamp')[0:3]
    post_list = Post.objects.filter(is_article=True).order_by('-timestamp')
    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        # paginated_queryset = paginator.page(1)
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'featured': featured_posts,
        'page_request_var': page_request_var,
        'category_count': category_count
    }
    return render(request, 'article.html', context)

def presentation(request):
    category_count = get_category_count()
    featured_posts = Post.objects.filter(featured=True).order_by('-timestamp')
    post_list = Post.objects.filter(is_presentation=True).order_by('-timestamp')
    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'featured': featured_posts,
        'page_request_var': page_request_var,
        'category_count': category_count
    }
    return render(request, 'presentation.html', context)


def post(request, id):
    category_count = get_category_count()
    featured_posts = Post.objects.filter(featured=True)
    post = get_object_or_404(Post, id=id)

    context = {

        'post': post,
        'featured': featured_posts,
        'category_count': category_count
    }
    return render(request, 'post.html', context)