from rest_framework import routers

from feed.views import FeedListView

DRFRouter = routers.DefaultRouter()
DRFRouter.register(r"feeds", FeedListView)
