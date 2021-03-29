from django.shortcuts import render, get_object_or_404
from . models import Movie
from . forms import MovieForm
from django.contrib.auth.decorators import login_required
# Create your views here. 

def index(request):
    return render(request, 'List/index.html')

def movies(request):
    movie_list=Movie.objects.all()
    return render(request, 'List/movies.html', {'movie_list' : movie_list})

def moviedetails(request, id):
    movie=get_object_or_404(Movie, pk=id)
    review=movie.mreview
    title=movie.mtitle
    date=movie.mdate
    rating=movie.mrating
    context={
        'movie' : movie,
        'review' : review,
        'title' : title,
        'date' : date,
        'rating' : rating,
    } 
    return render(request, 'List/moviedetails.html', context=context)

@login_required
def newMovie(request):
     form=MovieForm
     if request.method=='POST':
          form=MovieForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MovieForm()
     else:
          form=MovieForm()
     return render(request, 'List/newMovie.html', {'form': form})

def loginmessage(request):
    return render(request, 'List/loginmessage.html')

def logoutmessage(request):
    return render(request, 'List/logoutmessage.html')