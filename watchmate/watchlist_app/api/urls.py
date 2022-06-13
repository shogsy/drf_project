from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (WatchListAV,
                                     WatchListDetailAV,
                                     # StreamPlatformAV,
                                     # StreamPlatformDetailAV,
                                     StreamPlatformVS,
                                     ReviewList,
                                     ReviewDetail,
                                     ReviewCreate,
                                     WatchListGV,
                                     UserReview)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watchlist'),
    path('list2/', WatchListGV.as_view(), name='watchlist-new'),
    path('<int:pk>/', WatchListDetailAV.as_view(), name='watchlist-details'),
    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(),
    #      name='streamplatform-detail'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(),
         name='review-create'),
    path('<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-details'),
    path('reviews/', UserReview.as_view(),
         name='user-review-details'),
]
