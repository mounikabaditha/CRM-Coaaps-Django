from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth # type: ignore
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Record

from django.contrib import messages





# - Homepage 

def home(request):

    return render(request, 'webapp/index.html')


# - Register a user

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Account created successfully!")

            return redirect("my-login")

    context = {'form':form}

    return render(request, 'webapp/register.html', context=context)


# - Login a user

def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

    context = {'form':form}

    return render(request, 'webapp/my-login.html', context=context)


# - Dashboard

@login_required(login_url='my-login')
def dashboard(request):

    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, 'webapp/dashboard.html', context=context)

def sales_overview(request):
    # Your view logic here
    return render(request, 'webapp/sales_overview.html')


# - Create a record 

@login_required(login_url='my-login')
def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'webapp/create-record.html', context=context)


# - Update a record 

@login_required(login_url='my-login')
def update_record(request, pk):

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")

            return redirect("dashboard")
        
    context = {'form':form}

    return render(request, 'webapp/update-record.html', context=context)


# - Read / View a singular record

@login_required(login_url='my-login')
def singular_record(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'webapp/view-record.html', context=context)


# - Delete a record

@login_required(login_url='my-login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("dashboard")



# - User logout

def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("my-login")
# views.py

from django.shortcuts import render

def sales_management(request):
    # Add your sales management logic here
    return render(request, 'webapp/sales_management.html')

def service_management(request):
    # Add your service management logic here
    return render(request, 'webapp/service_management.html')
# views.py
from django.shortcuts import render, redirect
from .forms import InteractionForm
from .models import Interaction

def add_interaction(request):
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            interaction = form.save(commit=False)
            interaction.user = request.user
            interaction.save()
            return redirect('dashboard')  # Redirect to dashboard or any other appropriate page
    else:
        form = InteractionForm()
    return render(request, 'webapp/add_interaction.html', {'form': form})

def interaction_history(request):
    interactions = Interaction.objects.filter(user=request.user).order_by('-date_time')
    return render(request, 'webapp/interaction_history.html', {'interactions': interactions})
# views.py
from django.shortcuts import render, redirect
from .forms import InteractionForm

from django.shortcuts import render, redirect
from .forms import InteractionForm

def interaction_tracking(request):
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success URL after saving the interaction
    else:
        form = InteractionForm()
    return render(request, 'webapp/interaction_tracking.html', {'form': form})





