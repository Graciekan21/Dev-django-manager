from django.shortcuts import render

# Create your views here.
def get_tasktracker_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'tasktracker/tasktracker_list.html', context)

