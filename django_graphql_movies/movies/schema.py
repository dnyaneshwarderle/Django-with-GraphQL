import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from django_graphql_movies.movies.models import  Movies, Watchlist
from django_graphql_movies.movies.credientials import  config
import requests
 

class MoviesType(DjangoObjectType):
    class Meta:
        model = Movies

class WatchListType(DjangoObjectType):
    class Meta:
        model = Watchlist

class Query(ObjectType):
    movie = graphene.Field(MoviesType, id=graphene.Int())
    movies= graphene.List(MoviesType)
    watchlist= graphene.List(WatchListType)
    def resolve_movie(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            input1=Movies.objects.get(id=id)
            print(input1.title)
            movie_instance = Watchlist(
                id=input1.id,
                title=input1.title,
                poster_path=input1.poster_path,
                backdrop_path=input1.backdrop_path,
                original_language=input1.original_language,
                original_title=input1.original_title,
                overview=input1.overview,
                release_date=input1.release_date,
                popularity=input1.popularity,
                vote_count=input1.vote_count,
                video=input1.video,
                adult=input1.adult,
                genre_ids=input1.genre_ids,
            )
           
            movie_instance.save()
            return input1
            

        return None
    

    def resolve_movies(self, info, **kwargs):
        
        return Movies.objects.all()

    def resolve_watchlist(self, info, **kwargs):
        input2=Watchlist.objects.all()
        # print(data[0].id)
        allList=[]
        for input1 in input2:
            print(input1.title)
            allList.append({'id':input1.id,
                'codename':input1.codename,
                'title':input1.title,
                'poster_path':input1.poster_path,
                'backdrop_path':input1.backdrop_path,
                'original_language':input1.original_language,
                'original_title':input1.original_title,
                'overview':input1.overview,
                'release_date':input1.release_date,
                'popularity':input1.popularity,
                'vote_count':input1.vote_count,
                'video':input1.video,
                'adult':input1.adult,
                'genre_ids':input1.genre_ids})
        print(allList)
        return input2

class MovieInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    poster_path = graphene.String()
    codename =  graphene.String()

class PupularMovie(graphene.Mutation):
    class Arguments:
        input = MovieInput(required=True)

    ok = graphene.Boolean()
    movie = graphene.Field(MoviesType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        actors = []
        response = requests.get('https://api.themoviedb.org/3/movie/popular?api_key='+config.api_key+'&language=en-US&page=1')
        geodata = response.json()
        print(geodata)
        results= geodata['results']
        for input1 in results: 
            movie_instance = Movies(
                id=input1['id'],
                title=input1['title'],
                poster_path=input1['poster_path'],
                backdrop_path=input1['backdrop_path'],
                original_language=input1['original_language'],
                original_title=input1['original_title'],
                overview=input1['overview'],
                release_date=input1['release_date'],
                popularity=input1['popularity'],
                vote_count=input1['vote_count'],
                video=input1['video'],
                adult=input1['adult'],
                genre_ids=input1['genre_ids'],
            )
           
            movie_instance.save()
        return PupularMovie(ok=ok, movie=movie_instance)

class UpcomingMovie(graphene.Mutation):
    class Arguments:
        input = MovieInput(required=True)

    ok = graphene.Boolean()
    movie = graphene.Field(MoviesType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        actors = []
        response = requests.get('https://api.themoviedb.org/3/movie/upcoming?api_key='+config.api_key+'&language=en-US&page=1')
        geodata = response.json()
        results= geodata['results']
        for input1 in results: 
            movie_instance = Movies(
                id=input1['id'],
                title=input1['title'],
                poster_path=input1['poster_path'],
                backdrop_path=input1['backdrop_path'],
                original_language=input1['original_language'],
                original_title=input1['original_title'],
                overview=input1['overview'],
                release_date=input1['release_date'],
                popularity=input1['popularity'],
                vote_count=input1['vote_count'],
                video=input1['video'],
                adult=input1['adult'],
                genre_ids=input1['genre_ids'],
            )
           
            movie_instance.save()
        return UpcomingMovie(ok=ok, movie=movie_instance)

class LatestMovie(graphene.Mutation):
    class Arguments:
        input = MovieInput(required=True)

    ok = graphene.Boolean()
    movie = graphene.Field(MoviesType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        actors = []
        response = requests.get('https://api.themoviedb.org/3/movie/latest?api_key='+config.api_key+'&language=en-US')
        input1 = response.json()
        print(input1)
        movie_instance = Movies(
            id=input1['id'],
            title=input1['title'],
            poster_path=input1['poster_path'],
            backdrop_path=input1['backdrop_path'],
            original_language=input1['original_language'],
            original_title=input1['original_title'],
            overview=input1['overview'],
            release_date=input1['release_date'],
            popularity=input1['popularity'],
            vote_count=input1['vote_count'],
            video=input1['video'],
            adult=input1['adult'],
            genre_ids=input1['genres'],
        )
        
        movie_instance.save()
        return LatestMovie(ok=ok, movie=movie_instance)

class CreateWatchList(graphene.Mutation):
    class Arguments:
        input = MovieInput(required=True)

    ok = graphene.Boolean()
    movie = graphene.Field(WatchListType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        input1=Movies.objects.get(id=input.id)       
        movie_instance = Watchlist(
            codename=input.codename,
            id=input1.id,
            title=input1.title,
            poster_path=input1.poster_path,
            backdrop_path=input1.backdrop_path,
            original_language=input1.original_language,
            original_title=input1.original_title,
            overview=input1.overview,
            release_date=input1.release_date,
            popularity=input1.popularity,
            vote_count=input1.vote_count,
            video=input1.video,
            adult=input1.adult,
            genre_ids=input1.genre_ids,
        )
        
        movie_instance.save()
        return CreateWatchList(ok=ok, movie=movie_instance)


class Mutation(graphene.ObjectType):
    popular_movie = PupularMovie.Field()
    upcoming_movie = UpcomingMovie.Field()
    latest_movie = LatestMovie.Field()
    watch_list = CreateWatchList.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
