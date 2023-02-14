from django.shortcuts import redirect
def auth_customer(func):
    def wrap(request, *args, **kwargs):
        if 'cust_id' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('common:customerlogin')
            
    return wrap