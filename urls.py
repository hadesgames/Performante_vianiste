from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url( r'api/problems/(\d)+', 'eval.api.problems' ),
                       url( r'api/teams/(\d)+', 'eval.api.teams'),
                       url( r'api/tabel/(\d)+', 'eval.api.tabel'),
                       url( r'problems/(\d)+', 'eval.views.problems'),
                       url( r'teams/(\d)+', 'eval.views.teams'),
                       
    # Examples:
    # url(r'^$', 'Performante_vianiste.views.home', name='home'),
    # url(r'^Performante_vianiste/', include('Performante_vianiste.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
