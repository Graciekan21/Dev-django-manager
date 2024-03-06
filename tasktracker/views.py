from django.shortcuts import render

# Create your views here.
def get_tasktracker_list(request):
    return render(request, 'tasktracker/tasktracker_list.html')

