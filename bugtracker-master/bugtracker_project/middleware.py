import logging
from django.contrib.auth import logout
from django.contrib.sessions.middleware import SessionMiddleware
from django.utils import timezone
from django.shortcuts import render

logger = logging.getLogger('middleware')

class AutoLogoutMiddleware(SessionMiddleware):
    def process_request(self, request):
        logger.debug("AutoLogoutMiddleware: Middleware is running.")
        if request.user.is_authenticated:
            current_time = timezone.now()
            last_activity_time = request.session.get('last_activity_time')

            if last_activity_time:
                time_difference = current_time - last_activity_time
                if time_difference.seconds > (1 * 60):  # 30 minutos de inactividad
                    logger.debug("AutoLogoutMiddleware: User will be logged out due to inactivity.")
                    return self.show_logout_warning(request)

            request.session['last_activity_time'] = current_time

    def show_logout_warning(self, request):
        # Puedes personalizar esta vista de advertencia como desees
        # Por ejemplo, puedes mostrar un mensaje emergente o redirigir a una página de advertencia
        return render(request, 'logout_warning.html')
