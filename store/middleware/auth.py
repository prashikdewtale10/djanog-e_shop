from django.shortcuts import redirect
def auth_middleware(get_response):
    def middleware(request):
        returnUrl=request.META['PATH_INFO']
        print("Pritniyfgkgkfdnklfk=========",returnUrl)
        if not request.session.get('customer'):
            return redirect(f'login?return_Url={returnUrl}')


        response = get_response(request)
        return response

    return middleware