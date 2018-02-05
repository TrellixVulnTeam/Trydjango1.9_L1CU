from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages

from .models import Post
from .forms import PostForm

# Create your views here.
def post_create(request):
	form=PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request,"Succesfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.success(request,"Not Successfully Created")
	context={"form":form}
	return render(request,"post_form.html",context)

def post_detail(request,id=None):
	#instance=Post.objects.get(id=3)
	instance=get_object_or_404(Post,id=id)
	#share_string=quote_plus(instance.content)
	context={"title":instance.title,"instance":instance,}#"share_string":share_string}
	return render(request,"post_detail.html",context)

def post_list(request):
	queryset=Post.objects.all()#.order_by("-timestamp")
	context={"title":"list","object_list":queryset}
	return render(request,"base.html",context)

def post_update(request,id=None):
	instance=get_object_or_404(Post,id=id)
	form=PostForm(request.POST or None,request.FILES or None,instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request,"Saved")
		return HttpResponseRedirect(instance.get_absolute_url())
	context={"title":instance.title,"instance":instance,"form":form}
	return render(request,"post_form.html",context)

def post_delete(request,id=None):
	instance=get_object_or_404(Post,id=id)
	instance.delete()
	messages.success(request,"Deleted")
	return redirect("list")
