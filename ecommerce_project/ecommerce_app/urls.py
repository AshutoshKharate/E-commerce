from rest_framework import routers
from .views import ProductViewSet, CategoryViewSet, OrderItemViewSet, UserViewSet

router = routers.DefaultRouter()

router.register(r'createuser', UserViewSet, basename='createuser')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'orderitem', OrderItemViewSet, basename='orderitem')

urlpatterns = router.urls
