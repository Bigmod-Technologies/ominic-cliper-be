from rest_framework import status, viewsets
from rest_framework.response import Response

# authentication
from rest_framework.permissions import IsAuthenticated

# pagination
from rest_framework.pagination import LimitOffsetPagination

# filter search sort
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# serializer
from .serializers import BlogTagSerializers, BlogSerializers, BlogDetailsSerializers

# model
from .models import Blog, Tag


# utils
from drf_standardized_errors.openapi import AutoSchema
from drf_standardized_errors.handler import exception_handler
from drf_spectacular.utils import extend_schema


class DefaultPagination(LimitOffsetPagination):
    default_limit = 50
    limit_query_param = "limit"
    offset_query_param = "offset"
    max_limit = 50


# Create your views here.


@extend_schema(tags=["Blog Tag"])
class BlogTagView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogTagSerializers
    queryset = Tag.objects.all()
    pagination_class = DefaultPagination
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]

    filterset_fields = {
        "name": ["exact"],
    }
    search_fields = ["name"]
    ordering_fields = ["id"]

    schema = AutoSchema()

    def get_exception_handler(self):
        return exception_handler

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = []
        return super().get_permissions()

    def list(self, request):
        page = self.paginate_queryset(self.filter_queryset(self.get_queryset()))
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        serializer = self.get_serializer(
            self.get_object(), data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.user.is_active = False
        instance.user.save()
        return Response(
            {"status": "Removed Permanently"}, status=status.HTTP_204_NO_CONTENT
        )


@extend_schema(tags=["Blogs"])
class BlogView(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializers
    queryset = Blog.objects.all()
    pagination_class = DefaultPagination
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]

    filterset_fields = {
        "title": ["exact"],
    }
    search_fields = ["title"]
    ordering_fields = ["upload_time"]

    schema = AutoSchema()

    def get_exception_handler(self):
        return exception_handler

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BlogDetailsSerializers
        return super().get_serializer_class()

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = []
        return super().get_permissions()

    def list(self, request):
        page = self.paginate_queryset(self.filter_queryset(self.get_queryset()))
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(writer=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        serializer = self.get_serializer(
            self.get_object(), data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.user.is_active = False
        instance.user.save()
        return Response(
            {"status": "Removed Permanently"}, status=status.HTTP_204_NO_CONTENT
        )
