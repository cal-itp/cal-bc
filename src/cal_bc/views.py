from django.shortcuts import render

def custom_not_found_view(request, exception):
    if request.path.startswith('/admin/'):
        return render(request, '404.html', status=404)
    
    if request.user.is_authenticated:
        return render(request, '404_project.html', status=404)

    return render(request, '404_public.html', status=404)

