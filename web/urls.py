from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("register/",SignUpView.as_view(),name="signup"),
    path("login/",SignInView.as_view(),name="signin"),
    path("index/",IndexView.as_view(),name="index"),
    path("posts/<int:id>/comment/add/",add_comments,name="add-comments"),
    path("post/<int:id>/like/add/",like_posts,name="add-like"),
    path("logout/",signout_view,name="logout"),
    path("add_post/",AddPost.as_view(),name="add-post"),
    path("profile/",ProfileView.as_view(),name="profile"),
    path("post/<int:id>/remove/",profile_delete_view,name="post-delete"),
    path("index/comment/<int:id>/remove",comment_delete_view,name="comment-del"),
    path("post/update/",edit_profile,name="edit-profile"),
    path("people/", ListPeopleView.as_view(), name="people"),
    path("user/<int:id>/follower/add", add_follower, name="add-follower"),
    path("profile/add/",AddProfileView.as_view(),name="profilepic"),
    path("profile/<int:id>/edit/",EditprofileView.as_view(),name="edit-pic"),
    path("frinds/",FollowingView.as_view(),name="following")


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
