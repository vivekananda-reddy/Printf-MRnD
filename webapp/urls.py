from django.conf.urls import url
from webapp import classviews

urlpatterns=[
        url(r'^display/$',classviews.Toursview.as_view(),name="toursdisplay"),
        url(r'^display/(?P<pk>[0-9]+)/$',classviews.ToursDetails.as_view(),name="toursdetails"),
        url(r'^create/$',classviews.Tourscreate.as_view(),name="tourscreate"),
        url(r'^display/update/(?P<pk>[0-9]+)/$',classviews.ToursUpdate.as_view(),name='tourupdate'),
        url(r'^display/(?P<pk>[0-9]+)/delete/$',classviews.ToursDelete.as_view(),name='tourdelete'),
        url(r'^display/(?P<pk>[0-9]+)/pictures/create/$',classviews.PicturesCreate.as_view(),name='picurescreate'),
        url(r'^display/(?P<tour_id>[0-9]+)/picturedelete/(?P<pk>[0-9]+)/$',classviews.PictureDelete.as_view(),name='picturedelete'),
]