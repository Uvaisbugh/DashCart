from django.urls import path, include

from shop import views
app_name = 'shop'
urlpatterns = [
    # path('',views.index,name="index"),
    path('',views.allprodcat,name="allprodcat"),
    path('<slug:c_slug>/',views.allprodcat,name="products_by_category"),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProDetail,name="prodcategoryDetail"),
]
