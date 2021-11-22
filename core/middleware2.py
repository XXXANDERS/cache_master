from django.http import HttpResponse


class FirstMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('We are in FirstMiddleware, before')
        # можно проверять логику приложений
        return HttpResponse('Ok')
        response = self.get_response(request)
        print('We are in FirstMiddleware, after')
        return response


class SecondMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('We are in SecondMiddleware, before')
        response = self.get_response(request)
        print('We are in SecondMiddleware, after')
        return response
