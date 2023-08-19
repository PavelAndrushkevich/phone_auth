from django.shortcuts import render, redirect
from .models import UserProfile, AuthCode
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.authentication import TokenAuthentication
def login(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        user_profile, created = UserProfile.objects.get_or_create(phone_number=phone_number)
        auth_code, created = AuthCode.objects.get_or_create(user_profile=user_profile, defaults={'code': '1234'})
        # Simulate code sending delay here (1-2 seconds)
        return redirect('input_code', user_id=user_profile.id)
    return render(request, 'login.html')

def input_code(request, user_id):
    user_profile = UserProfile.objects.get(pk=user_id)
    if request.method == 'POST':
        code = request.POST.get('code')
        auth_code = AuthCode.objects.get(user_profile=user_profile)
        if code == auth_code.code:
            user_profile.is_authenticated = True
            user_profile.save()
            return redirect('profile', user_id=user_profile.id)
        return render(request, 'input_code.html', {'error': 'Invalid code'})
    return render(request, 'input_code.html')



def profile(request, user_id):
    user_profile = UserProfile.objects.get(pk=user_id)

    if request.method == 'POST':
        external_invite_code = request.POST.get('external_invite_code')
        if external_invite_code:
            try:
                invited_user = UserProfile.objects.get(invite_code=external_invite_code)
                if invited_user != user_profile:
                    user_profile.activated_invite_code = external_invite_code
                    user_profile.save()
            except UserProfile.DoesNotExist:
                pass

    return render(request, 'profile.html', {'user_profile': user_profile})


class InvitedUsersList(generics.ListAPIView):
    serializer_class = UserProfileSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_profile = self.request.user.userprofile_set.first()
        if user_profile:
            return UserProfile.objects.filter(activated_invite_code=user_profile.invite_code)
        return UserProfile.objects.none()