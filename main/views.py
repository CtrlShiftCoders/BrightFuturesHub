from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    author = request.user
    print(author.username, author.email)
    return render(request, "main/index.html")