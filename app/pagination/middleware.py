class PaginationMiddleware(object):

    def process_request(self, request):
        try:
            request.page = int(request.REQUEST['page'])
        except (KeyError, ValueError, TypeError):
            request.page = 1
