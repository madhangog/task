from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'form/post/list.html', {'posts': posts})

def post_new(request):
    # post = get_object_or_404(Post)
    post= Post.objects.last()
    profile_image = post.profile_image
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # post.save()
            Post.objects.create(name=post.name, email=post.email, phone=post.phone, profile_image=post.profile_image, video=post.video)
            return redirect('post_list')
    else:
        form = PostForm()
    context= {'imagefile': post.profile_image,
        'form': form
        }
    return render(request, 'form/post/signup_page.html', {'form': form, 'image': profile_image, "home_url": "logo.png"})

def view_post(request, post_id):
    post = Post.objects.get(id=post_id)

    return render(request, 'form/post/list.html', {'posts': post, 'imagefile': post.profile_image, 'videofile': post.profile_image})