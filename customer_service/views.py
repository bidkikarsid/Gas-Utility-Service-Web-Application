

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest, Customer, SupportRepresentative
from .forms import ServiceRequestForm

def home_view(request):
    return HttpResponse("Welcome to the Gas Utility Service Application")

def home_view(request):
    return render(request, 'home.html')  # Render a template


@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer
            service_request.save()
            return redirect('track_requests')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/submit_request.html', {'form': form})

@login_required
def track_requests(request):
    requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'customer_service/track_requests.html', {'requests': requests})

@login_required
def manage_requests(request):
    if request.user.supportrepresentative:
        assigned_requests = request.user.supportrepresentative.assigned_requests.all()
        return render(request, 'customer_service/manage_requests.html', {'requests': assigned_requests})
    else:
        return redirect('home')
