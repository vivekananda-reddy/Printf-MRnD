from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from webapp.forms import UserForm, PictureCreateForm
from webapp.models import Tour, Picture

@method_decorator(login_required,name='dispatch')
class Toursview(ListView):
    model=Tour

    def get_queryset(self):
        obj = Tour.objects.all().filter(owner=self.request.user)
        return obj



@method_decorator(login_required,name='dispatch')
class ToursDetails(DetailView):
    model=Tour

    def get_queryset(self):
        obj = Tour.objects.all().filter(owner=self.request.user)
        return obj


@method_decorator(login_required,name='dispatch')
class Tourscreate(CreateView):
    model=Tour
    fields=['date','location','details']

    def get_success_url(self):
        return reverse('toursdisplay')

    def get_queryset(self):
        obj = Tour.objects.all().filter(owner=self.request.user)
        return obj

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Tourscreate, self).form_valid(form)

@method_decorator(login_required,name='dispatch')
class ToursUpdate(UpdateView):
    model=Tour
    template_name = 'webapp/tour_update.html'
    fields=['date','location','details']

    def get_queryset(self):
        obj = Tour.objects.all().filter(owner=self.request.user)
        return obj

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ToursUpdate, self).form_valid(form)

@method_decorator(login_required,name='dispatch')
class ToursDelete(DeleteView):
    model=Tour
    success_url = reverse_lazy('toursdisplay')

    def get_queryset(self):
        obj = Tour.objects.all().filter(owner=self.request.user)
        return obj

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ToursDelete, self).form_valid(form)


@method_decorator(login_required,name='dispatch')
class PicturesCreate(CreateView):
    model=Picture
    form_class = PictureCreateForm

    def post(self,request,*args,**kwargs):
        self.object=None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        # the actual modification of the form
        form.instance.tour = Tour(kwargs['pk'])

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

#remove tour from fields and assign manually
    def get_success_url(self):
        return reverse('toursdetails',kwargs=self.kwargs)

    def get_queryset(self):
        obj = Picture.objects.all().filter(owner=self.request.user)
        return obj

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PicturesCreate, self).form_valid(form)

@method_decorator(login_required,name='dispatch')
class PictureDelete(DeleteView):
    model=Picture

    def get_success_url(self):
        temp={}
        temp['pk']=self.kwargs['tour_id']
        return reverse_lazy('toursdetails',kwargs=temp)

    def get_queryset(self):
        obj = Picture.objects.all().filter(owner=self.request.user)
        return obj

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PictureDelete, self).form_valid(form)



class UserFormView(View):
    form_class = UserForm
    template_name = 'webapp/registration_form.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('/login/')
        return render(request,self.template_name,{'form':form})


































