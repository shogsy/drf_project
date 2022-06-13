from rest_framework.pagination import (PageNumberPagination,
                                       LimitOffsetPagination,
                                       CursorPagination)


class WatchListPagination(PageNumberPagination):
    page_size = 5
    # page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 50


class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 6
    max_page_size = 10


class WatchListCPagination(CursorPagination):
    page_size = 5
    ordering = 'created'
