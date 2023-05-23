from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    print('!'*1000)
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p'
