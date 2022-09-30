from django.shortcuts import render, redirect
from .models import Review


# Create your views here.
def index(request):
    reviews = Review.objects.all()

    context = {
        "reviews": reviews,
    }

    return render(request, "moviepjt/index.html", context)


def new(request):

    return render(request, "moviepjt/new.html")


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")

    # DB에 저장
    Review.objects.create(title=title, content=content)

    context = {
        "title": title,
        "content": content,
    }
    return redirect("moviepjt:index")


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        "review": review,
    }
    return render(request, "moviepjt/detail.html", context)


def edit(request, pk):
    review = Review.objects.get(pk=pk)

    context = {
        "review": review,
    }

    return render(request, "moviepjt/edit.html", context)


def update(request, pk):
    review = Review.objects.get(pk=pk)

    title = request.GET.get("title")
    content = request.GET.get("content")

    review.title = title
    review.content = content

    review.save()

    return redirect("moviepjt:detail", review.pk)


def delete(request, pk):
    Review.objects.get(pk=pk).delete()

    return redirect("moviepjt:index")
