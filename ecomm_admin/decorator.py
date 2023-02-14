from django.shortcuts import redirect
def auth_admin(func):
    def wrap(request, *args, **kwargs):
        if 'admin_id' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('common:adminlogin')
            
    return wrap