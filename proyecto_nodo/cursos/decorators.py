from django.shortcuts import redirect

def role_required(allowed_roles):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.session.get('usuario_id'):
                return redirect('login')
            rol = request.session.get('rol')
            if rol in allowed_roles:
                return view_func(request, *args, **kwargs)
            return redirect('login')
        return _wrapped_view
    return decorator