from django.shortcuts import render ,redirect
from .models import Task

# Create your views here.
def home(request):
   if request.user.is_authenticated:
      if request.method == 'POST':
         name = request.POST['name']
         desc = request.POST['desc']
         user = request.user
         Task.objects.create(
            name=name,
            desc=desc,
            user=user
         )
         return redirect('home')
    
      all_tasks =Task.objects.filter(user=request.user)
      context = {
        'all_tasks': all_tasks
      }
      return render(request, 'home.html',context)
   else:
        return redirect('login')
   

   
def update_task(request,id):
    my_task = Task.objects.get(id=id, user=request.user)
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        my_task.name = name
        my_task.desc = desc
        my_task.save()
        return redirect('home')

    context = {
        'task': my_task
    }
    return render(request, 'update.html',context )

def delete_task(request,id):
    my_task = Task.objects.get(id=id, user=request.user)
    my_task.delete()
    return redirect('home')
