
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from django.contrib.auth.models import User

# Create your views here.
a = User.objects.all()
print(a)

# new_user = User.objects.create(username= "RichaTakwar", first_name = "Richa", last_name= "Talwar", email = "talwar@gmail.com", password="talwar")
# print(new_user)




def signup(request):
    if request.method == 'POST':
        Username = request.POST.get("username")
        print(Username)
        FirstName = request.POST.get("first_name")
        print(FirstName)
        LastName = request.POST.get("last_name")
        print(LastName)
        EmailId = request.POST.get("email")
        print(EmailId)
        Password = request.POST.get("password")
        print(Password)

        x = User.objects.create(username=Username, first_name=FirstName, last_name=LastName, email = EmailId, password=Password)
        
        print('user created')
        return redirect('/')


    else:
        return render(request, 'app2/signup.html')
