from django.contrib.auth.decorators import user_passes_test

def roles_required(roles):
    def decorator(view_func):
        @user_passes_test(lambda user: user.groups.filter(name__in=roles).exists())
        def wrapper(request, *args, **kwargs):
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator