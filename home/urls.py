from django.urls import path,include
from .views import YoutubeVideosSubtitles, GroupLayout

urlpatterns = [

	path('vdtitle/', YoutubeVideosSubtitles.as_view(), name = 'YoutubeVideosSubtitles'),
	path('grouptitle/', GroupLayout.as_view(), name = 'GroupLayout')

]
