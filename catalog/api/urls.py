from django.urls import include, path
from rest_framework import routers
from .views import BookInstanceViewSet, BookViewSet, AuthorViewSet, LanguageViewSet, GenreViewSet


router = routers.DefaultRouter()
router.register(r'Book', BookViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'language', LanguageViewSet)
router.register(r'genre', GenreViewSet)
router.register(r'BookInstance', BookInstanceViewSet)


urlpatterns = [
    path('', include(router.urls)),

]