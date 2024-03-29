from django.shortcuts import render,redirect
from .models import student
# Create your views here.
def home(request):
    return render(request,'home.html')

def add_details(request):
    if request.method == "POST":
        dname = request.POST.get('name')
        dphone = request.POST.get('phone')
        dmail = request.POST.get('mail')
        data = student(name=dname, phone=dphone, email=dmail)
        data.save()
        return redirect('form')
       
def form(request):
    stu = student.objects.all()
    context = {'stu': stu}
    return render(request, 'form.html', context)


def remove_cart_items(request, stu_uid):
    try:
        stu_obj = student.objects.get(uid=stu_uid)
        stu_obj.delete()
        return redirect('/form/')
    except Exception as e:
        print(e)

def update(request, stu_uid):
    obj = student.objects.get(uid=stu_uid)
    context = {'obj': obj}
    return render(request, 'update.html', context)

def update_form(request, stu_uid):
    if request.method == "POST":
        uname = request.POST.get('name')
        uphone = request.POST.get('phone')
        umail = request.POST.get('mail')
        obj = student.objects.filter(uid=stu_uid).update(name=uname, phone=uphone, email=umail)
        return redirect('form')