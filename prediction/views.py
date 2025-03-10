from django.shortcuts import render,redirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import SignupForm, LoginForm
from .models import CustomUser
from django.contrib.auth.hashers import make_password, check_password


def home(request):
    return render(request,'home.html')



# View for user registration (signup)
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            # Create user instance
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            image = form.cleaned_data['image']
            password = form.cleaned_data['password']
            
            # Encrypt the password
            hashed_password = make_password(password)
            
            # Save user to database
            user = CustomUser(username=username, email=email, age=age, image=image, password=hashed_password)
            user.save()
            messages.success(request, "User registered successfully!")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# View for user login (signin)
def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user = CustomUser.objects.get(username=username)
                if check_password(password, user.password):  # Check if password matches
                    # Perform custom login (e.g., using session or token)
                    request.session['user_id'] = user.id  # Save user ID to session
                    messages.success(request, f"Welcome back, {username}!")
                    return redirect('landing')
                else:
                    messages.error(request, "Invalid password.")
            except CustomUser.DoesNotExist:
                messages.error(request, "Invalid username.")
    else:
        form = LoginForm()
    return render(request, 'signin.html', {'form': form})

# View for landing page after login
def landing(request):
    # Check if user is logged in
    if 'user_id' not in request.session:
        return redirect('login')  # Redirect to login if user is not authenticated
    
    user = CustomUser.objects.get(id=request.session['user_id'])
    return render(request, 'landing.html', {'user': user})


