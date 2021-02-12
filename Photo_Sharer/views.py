from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
#from .forms import ImageForm
from .models import Image
# Create your views here.


def home(request):
    context = {
        'images': Image.objects.all()
    }
    return render(request, 'Photo_Sharer/home.html', context)


class ImageListView(ListView):
    model = Image
    template_name = 'Photo_Sharer/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'images'
    ordering = ['-date_posted']
    paginate_by = 5


class UserImageListView(ListView):
    model = Image
    template_name = 'Photo_Sharer/user_images.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'images'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Image.objects.filter(author=user).order_by('-date_posted')


class ImageDetailView(DetailView):
    model = Image


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    fields = ['title', 'photo']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ImageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Image
    fields = ['title', 'photo']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        image = self.get_object()
        if self.request.user == image.author:
            return True
        return False


class ImageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Image
    success_url = '/'

    def test_func(self):
        image = self.get_object()
        if self.request.user == image.author:
            return True
        return False
