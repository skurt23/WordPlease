from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from articles.models import Article
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from articles.forms import ArticleForm

# Create your views here.


class HomeView(View):

    def get(self, request):
        """
        Renderiza el home con un listado de los artículos más recientes
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        # Recupero todos los artículos de la base de datos y los ordena
        article = Article.objects.order_by('-publication_date').select_related('author')
        now = timezone.now()
        context = {'article_list': article[:10], 'now': now}
        return render(request, 'articles/home.html', context)


class BlogsView(View):

    def get(self, request):
        """
        Renderiza el listado de los blogs de usuarios disponibles
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        # Recupero los usuarios de la base de datos y los ordeno alfabéticamente
        blog = User.objects.order_by('-username')
        context = {'blogs_list': blog[:10]}
        return render(request, 'articles/blogs.html', context)


class BlogDetailView(View):

    def get(self, request, username):
        """
        Renderiza los artículos paginados de un usuario
        :param request: objeto HttpRequest con los datos de la petición
        :param username: username del autor del artículo a recuperar
        :return: objeto HttpResponse con los datos de la respuesta
        """
        now = timezone.now()
        # Recupero los artículos del usuario correspondiente y les aplico una paginación
        articles = Article.objects.filter(author__username=username).order_by('-publication_date')
        paginator = Paginator(articles, 5)
        page = request.GET.get('page')

        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)

        context = {'article_list': articles, 'username': username, 'now': now}
        return render(request, 'articles/blog_detail.html', context)


class ArticleDetailView(View):

    def get(self, request, username, pk):
        """
        Renderiza el detalle de un artículo
        :param request: objeto HttpRequest con los datos de la petición
        :param username: username del autor del artículo a recuperar
        :param pk: clave primaria del artículo a recuperar
        :return: objeto HttpResponse con los datos de la respuesta
        """
        # Recupero el artículo para mostrarlo
        article = Article.objects.filter(author__username=username, pk=pk)
        context = {'article': article[0], 'username': username}
        return render(request, 'articles/article_detail.html', context)


class ArticleCreationView(View):

    @method_decorator(login_required())
    def get(self, request):
        """
        Presenta el formulario para crear un artículo
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        message = None
        article_form = ArticleForm()
        context = {'form': article_form, 'message': message}
        return render(request, 'articles/article_creation.html', context)

    @method_decorator(login_required())
    def post(self, request):
        """
        Presenta el formulario para crear un artículo, valida el formulario y crea el artículo si todo ha ido bien
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        message = None
        article_user = Article(author=request.user)
        article_form = ArticleForm(request.POST, instance=article_user)
        if article_form.is_valid():
            article = article_form.save()
            article_form = ArticleForm()
            message = 'Artículo creado correctamente.Puedes ver tu artículo haciendo click <a href="{0}">aquí</a>'.format(
                reverse('article_detail', args=[article.author.username, article.pk])
            )

        context = {'form': article_form, 'message': message}
        return render(request, 'articles/article_creation.html', context)





