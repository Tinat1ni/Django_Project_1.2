from django.shortcuts import redirect
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.contrib.auth import logout

class LastActiveMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if not request.user.is_authenticated:
            if hasattr(view_func,'requires_login') and view_func.requires_login:
                return redirect(reverse('registration'))
            return None

        # if request.user.is_authenticated:
        #     request.user.last_active = timezone.now()
        #     request.user.save(update_fields=['last_active'])


        now = timezone.now()
        last_activity = request.session.get('last_activity')

        if last_activity:
            timeout_duration = 60
            if (now - last_activity).total_seconds() > timeout_duration:
                 logout(request)
                 return redirect(reverse('login'))

            request.session['last_activity'] = now
            request.user.last_active = now
            request.user.save(update_fields=['last_active'])


        return None


