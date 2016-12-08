from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/Start_page.html', {})
