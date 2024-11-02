from django.shortcuts import redirect
import time
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse

class SessionTimeoutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            session_last_activity = request.session.get('last_activity')

            if session_last_activity:
                elapsed_time = time.time() - session_last_activity

                if elapsed_time > 60:
                    request.session.flush()
                    return  redirect(reverse('user:login'))

            request.session['last_activity'] = time.time()

