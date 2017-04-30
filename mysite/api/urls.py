from django.conf.urls import url

from firstapp.views import PostListView, PostView, UserListView, DadosPagamentoListView, DadosPessoaisListView

helper_patterns = [
    url(r'^posts/$', PostListView.as_view(), name='posts'),
    url(r'^posts/(?P<pk>[0-9]+)/$', PostView.as_view(), name='get_post'),
    url(r'^user/$', UserListView.as_view(), name='user'),
    url(r'^pay/$', DadosPagamentoListView.as_view(), name='pay'),
    url(r'^info/$', DadosPessoaisListView.as_view(), name='info'),
]

urlpatterns = helper_patterns