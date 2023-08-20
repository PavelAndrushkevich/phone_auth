from django.urls import path

from .views import login, input_code, profile, InvitedUsersList

urlpatterns = [
    path('', login, name='login'),
    path('input-code/<int:user_id>/', input_code, name='input_code'),
    path('profile/<int:user_id>/', profile, name='profile'),
    path('api/invited-users/', InvitedUsersList.as_view(), name='invited-users-list'),
]
