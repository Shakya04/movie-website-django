from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Review
from .forms import ReviewForm
from django.shortcuts import redirect
from .apps import MovieSiteConfig
from rest_framework.views import APIView
from django.db.models import Avg
from sklearn.feature_extraction.text import TfidfVectorizer
from model_log_reg import tfidf_log_reg as tlr
import joblib

# Create your views here.


def home(request):
    allMovies = None
    query = request.GET.get("name")
    if query:
        allMovies = Movie.objects.filter(name__icontains=query)
    else:
        allMovies = Movie.objects.all()
    return render(request, "index.html", {"movies": allMovies})

def detailpage(request, id):
    detmovie = Movie.objects.get(id=id)
    reviews = Review.objects.filter(movie=id)
    average = reviews.aggregate(Avg("rating"))["rating__avg"]
    if average == None:
        average = 0
    average = round(average,2)
    context = {
        "movies": detmovie,
        "reviews": reviews,
        "average": average,
    }
    return render(request, "details.html", context)


def add_review(request, id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=id)
        if request.method == "POST":
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.movie = movie
                data.user = request.user
                data.comment = request.POST["comment"]
                data.rating = request.POST["rating"]
                text = [data.comment]
                sentiment, score = tlr.log_model(text)
                data.sentiment = sentiment
                data.score = score

                data.save()
                return redirect("movie_site:detail", id)
        else:
            form = ReviewForm()
        return render(request, "details.html", {"form": form})
    else:
        return redirect("accounts:login")


def edit_review(request, movie_id, review_id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=movie_id)
        review = Review.objects.get(movie=movie, id=review_id)
        if request.user == review.user:
            if request.method == "POST":
                form = ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    data = form.save(commit=False)
                    text = [data.comment]
                    sentiment, score = tlr.log_model(text)
                    data.sentiment = sentiment
                    data.score = score
                    if (data.rating > 10) or (data.rating < 0):
                        error = "Invalid Input ! Please input between the range of 0 to 10"
                        return render(request, "editreview.html",{"error": error, "form": form})
                    else:
                        data.save()
                        return redirect("movie_site:detail", movie_id)

            else:
                form = ReviewForm(instance=review)
            return render(request, "editreview.html", {"form": form})
        else:
            return redirect("movie_site:detail")
    else:
        return redirect("accounts:login")


def delete_review(request, movie_id, review_id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=movie_id)
        review = Review.objects.get(movie=movie, id=review_id)
        if request.user == review.user:
            review.delete()
        return redirect("movie_site:detail", movie_id)
    else:
        return redirect("accounts:login")


