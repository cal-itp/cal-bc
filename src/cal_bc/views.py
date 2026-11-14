from django.shortcuts import render


def custom_not_found_view(request, exception):
    if request.path.startswith('/admin/'):
        return render(request, '404.html', status=404)
    
    if request.user.is_authenticated:
        return render(request, '404_project.html', status=404)

    return render(request, '404_public.html', status=404)

def custom_server_error_view(request):
    if request.path.startswith('/admin/'):
        return render(request, '500.html', status=500)
    
    if request.user.is_authenticated:
        return render(request, '500_project.html', status=500)

    return render(request, '500_public.html', status=500)

