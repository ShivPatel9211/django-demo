from django.shortcuts import render , HttpResponse , redirect
from . models import Contact ,Blog_post , Comment
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from math import ceil
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout
    
# Create your views here.
def home(request):
    return render (request, 'home.html')


def contact(request):
    if request.method == 'POST':
        fullname=request.POST['fullname']
        email=request.POST['email'] 
        phone=request.POST['phone']
        message=request.POST['message']
        address=request.POST['address']
        if len(fullname) < 10:
            messages.warning(request,'Your full name should be more then 10 character ')
            return redirect('contact')
        elif len(phone) < 10:
            messages.warning(request,'Your phone no should be of 10 digit ')
            return redirect('contact')
        else:
            cont = Contact(Fullname=fullname,email=email,phone=phone,address=address,message=message)
            cont.save()
            messages.success(request,"you are successfully sumbited the form")
    return render (request, 'contact.html')

def blog(request):
    allpost = Blog_post.objects.all()
    lenght_of_blog=len(allpost)
    # paginator = Paginator(allpost, 2) # Show 25 contacts per page.
    no_of_post= 2
    page = request.GET.get('page')
    if page is None:
        page=1
    else:
        page =int(page)
    allpost= allpost[(page-1)*no_of_post:page*no_of_post]
    if page > 1:
        prev=page-1
    else:
        prev=None
    if page < ceil(lenght_of_blog/no_of_post):
        nxt=page+1
    else:
        nxt = None


    # page_obj = paginator.get_page(page)

    context = {
        'allpost':allpost,
        'prev':prev,
        'nxt':nxt
        # 'page_obj':page_obj
    }

    return render(request,'blog.html',context)

def search(request):
    if request.method == 'GET':
        query = request.GET['query']
        if len(query) > 100:
            allpost=[];
        elif query is not None:
            # lookups= Q(title__icontains=query) | Q(author__icontains=query)
            # results= Blog_post.objects.filter(lookups).distinct()
            posttitile = Blog_post.objects.filter(title__icontains = query)
            postauthor = Blog_post.objects.filter(author__icontains = query)
            postcontent = Blog_post.objects.filter(content__icontains = query)
            allpost = posttitile.union(postauthor,postcontent)
        # else:
        #     msg = "No result found"
        searchcontext ={
                    # "allpost":results,
                    "allpost":allpost,
                     "query":query
                }

    return render(request, 'search.html',searchcontext , )

def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username ,password= password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid username or password')
            return redirect('login')
    return render(request,'login.html')

def logout_user(request):
     logout(request)
     messages.success(request,'You have successfully logout')
     return redirect('home')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if 'check' in request.POST:
            pass
        else:
            messages.warning(request,'Check box is not checked , plz agree terms and condition ')
            return redirect('signup')
        if password == cpassword:
            user_obj= User.objects.filter(username=username).first()
            if user_obj is not None:
                messages.warning(request,'User of this username is already exit')
                return redirect('signup')
            # print(username)
            # print(email)
            # print(password)
            else:
                blog_user = User.objects.create_user(username=username,email=email,password=password)
                blog_user.save()
                messages.success(request,'Your account is successfully created, do login your account')
                return redirect('login')
        else:
            messages.warning(request,'Your password are not matching')
            return redirect('signup')
    return render(request,'signup.html')

def comment(request):
    if request.method=="POST":
        comment = request.POST['comment']
        sno= request.POST['sno']
        post =Blog_post.objects.get(sno=sno)
        user=request.user
        comment=Comment(post=post, comment=comment,user=user)
        comment.save()
        return redirect(f'/postdetail/{post.slug}')


def postdetail(request,slug):
    detail=Blog_post.objects.filter(slug=slug).first()
    comment = Comment.objects.filter(post=detail)
    context ={
        'detail':detail,
        'comment':comment
    }
    return render(request,'postdetail.html',context)

def postblog(request):
    return render(request,'postblog.html')