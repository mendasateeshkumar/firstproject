from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from .models import Employee
from .models import Books

# Create your views here.
def display(request):
    return render(request,'input.html')

def signup(request):
    return render(request,'output.html')

def main(request):
    return render(request,'main.html')

def update(request):
    return render(request,'update.html')

def delete(request):
    return render(request,'delete.html')

def retrive(request):
    return render(request,'retrive.html')










def info(request):
    if request.method=='POST':
        a=request.POST['name']
        b=request.POST['phno']
        c=request.POST['mail']
        d=request.POST['password']

        dept=Employee(emp_name=a, emp_phno=b, emp_mailid=c, emp_password=d)
        dept.save()
        return render(request,'input.html')



def details(request):
    if request.method=='POST':
        x=request.POST['upload']

    book=Books(Book_name=x)
    book.save()
    return HttpResponse('Book uploaded succesfully')


def modify(request):
    context={}
    if request.method=='POST':
        p=request.POST['booknum']
        q=request.POST['newbook']

        n=Books.objects.get(id=p)

        n.Book_name=q
        n.save()
        context['msg']='successfully updated'
        return render(request,'update.html',context)


def showdelete(request):
    if request.method=='POST':
        rs=request.POST['deletenew']
        bkk=Books.objects.filter(Book_name=rs)
        bkk.delete()
        return HttpResponse('Deleted your book successfully')



def retrivedata(request):
    context={}
    if request.method=='POST':
        zz=request.POST['retrivebook']
        bookk=Books.objects.get(id=zz)
        print(bookk)
        context['bookdetails']=bookk
        return render(request,'retrive.html',context)


