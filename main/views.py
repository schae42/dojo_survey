from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'index.html')

def result(request):
    context = {
        'name' : request.POST['name'],
        'location' : request.POST['location'],
        'language' : request.POST['language'],
        'comment' : request.POST['comment']
    }
    print(context)
    return render(request, 'result.html', context)
# requests to a server
# Get request - rendering an HTML, 
# POST request - sends information from the user
