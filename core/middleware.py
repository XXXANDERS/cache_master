from django.http import HttpResponse


class FirstMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('We are in FirstMiddleware, before')
        response = self.get_response(request)
        print('We are in FirstMiddleware, after')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('PROCESS VIEW!!!')
        print(request)
        print(view_func)
        print(view_args)
        print(view_kwargs)
        pass

    def process_exception(self, request, exception):
        # здесь мы можем сделать логирование или ещё что
        print(f'Exception is {exception}')
        # return None
        return HttpResponse('Exception!')


class SecondMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('We are in SecondMiddleware, before')
        response = self.get_response(request)
        print('We are in SecondMiddleware, after')
        return response
