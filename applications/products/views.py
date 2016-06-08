from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    """
    Concrete view for listing a queryset or creating a model instance.
    based upon:
        CreateModelMixin:Create a model instance.
        ListModelMixin: List a queryset.
        GenericAPIView: Base class for all other generic views.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, *args, **kwargs):
        """
        Lists the products
        ---
            tags:
                - Product
            operationId: listProducts
        """
        return super(ProductListCreateView, self).list(*args, **kwargs)

    def create(self, *args, **kwargs):
        """
        Creates a single product
        ---
            tags:
                - Product
            operationId: createProducts
        """
        return super(ProductListCreateView, self).create(*args, **kwargs)


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Concrete view for retrieving, updating or deleting a model instance.
    Based upon:
    RetrieveModelMixin: Retrieve a model instance.
    UpdateModelMixin: Update a model instance.
    DestroyModelMixin: Destroy a model instance.
    GenericAPIView : Base class for all other generic views.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = None
    lookup_url_kwarg = "product_id"

    def retrieve(self, *args, **kwargs):
        """
        Retrieves a single Product by ID
        ---
            tags:
                - Product
            operationId: retrieveProduct
        """
        return super(ProductRetrieveUpdateDestroyView, self).retrieve(*args, **kwargs)

    def update(self, *args, **kwargs):
        """
        Updates a product
        ---
            tags:
                - Product
            operationId: updateProduct
        """
        return super(ProductRetrieveUpdateDestroyView, self).update(*args, **kwargs)

    def partial_update(self, *args, **kwargs):
        """
        Partially updates a product
        ---
            tags:
                - Product
            operationId: patchProduct
        """
        return super(ProductRetrieveUpdateDestroyView, self).partial_update(*args, **kwargs)

    def destroy(self, *args, **kwargs):
        """
        Destroys a product
        ---
            tags:
                - Product
            operationId: destroyProduct
        """
        return super(ProductRetrieveUpdateDestroyView, self).destroy(*args, **kwargs)
