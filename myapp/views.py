from django.shortcuts import render # type: ignore

def index(request):
    # context = {'user_name': 'John Doe'}  # Data passed to the template
    return render(request, 'myapp/index.html')
