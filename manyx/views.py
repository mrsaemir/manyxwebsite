import json
from rest_framework import viewsets
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import Http404
from django.http import HttpResponseRedirect
from .serializers import ManyxUserCommonSerializer, ManyxUserAdminSerializer
from .models import ManyxUser, SocialReferCounter
from .mixins import AnonymousUserMixin, AdminMixin


class ManyxUserViewSet(AnonymousUserMixin, viewsets.ReadOnlyModelViewSet):
    queryset = ManyxUser.objects.all()
    serializer_class = ManyxUserCommonSerializer
    lookup_field = 'username'


class ManyxUserAdminViewSet(AdminMixin, viewsets.ModelViewSet):
    queryset = ManyxUser.objects.all()
    serializer_class = ManyxUserAdminSerializer
    lookup_field = 'username'


# a function that tries to match each request to available social accounts
# of each person.
def social_refer_counter(request, username, social_service):
    # assuring data validation
    from django.contrib.auth import get_user_model
    ManyxUserModel = get_user_model()
    if request.method == 'GET':
        try:
            user = ManyxUserModel.objects.get(username=username)
        except ObjectDoesNotExist:
            raise Http404
        # getting user's social info
        social_info = user.social
        if social_info.get(social_service):
            refer = SocialReferCounter()
            refer.add_record(
                             user=user,
                             account=social_service,
                             account_id=social_info[social_service]
                             )
            # if a requested resource matches in database,
            # user will be redirected to target url.
            return HttpResponseRedirect(social_info[social_service])
        else:
            raise Http404