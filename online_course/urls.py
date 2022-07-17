from rest_framework.routers import SimpleRouter

from online_course.views import ChapterViewSet, EpisodeViewSet, OnlineCourseViewSet

router = SimpleRouter()
router.register('chapter', ChapterViewSet, basename='chapter')
router.register('episode', EpisodeViewSet)
router.register('online_course', OnlineCourseViewSet)
urlpatterns = router.urls
