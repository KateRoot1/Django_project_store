from django.urls import path
from myapp.views import(
    ProductListView, 
    ProductDetailView, 
    ProductDeleteView, 
    ProductCreateView,
    ProductUpdateView,
)

app_name = "myapp"

urlpatterns = [
    # http://127.0.0.1:8000/myapp/hello
#   path("", index, name='index'),
    path("", ProductListView.as_view(), name='index'),
#   path("<int:my_id>/", indexItem, name="detail"),
    path("<int:pk>/", ProductDetailView.as_view(), name="detail"),
    
#   path("additem/", add_item, name="add_item"),
    path("additem/", ProductCreateView.as_view(), name="add_item"),
#   path("updateitem/<int:my_id>/", update_item, name="update_item"),
    path('updateitem/<int:pk>/', ProductUpdateView.as_view(), name='update_item'),
#   path("deleteitem/<int:my_id>/", delete_item, name="delete_item"),
    path("deleteitem/<int:pk>/", ProductDeleteView.as_view(), name="delete_item"),

    # http://127.0.0.1:8000/myapp/contacts
]