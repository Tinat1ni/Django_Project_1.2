from django.shortcuts import redirect, render
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


class ErrorPages(MiddlewareMixin):
    def process_response(self, request, response):
        if response.status_code == 404:
            return self.custom_404_view(request)

        elif response.status_code == 500:
            return self.custom_500_view(request)

        return response

    def custom_404_view(self,request):
        context = {
            'error_message': '404'
        }
        return render(request, '404.html', context, status=404)

    def custom_500_view(self,request):
        context = {
            'error_message': '500'
        }
        return render(request, '500.html', context, status=500)