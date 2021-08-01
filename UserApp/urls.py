from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('Categories/<cid>',views.showCategories),
    path('filter-by-price-high-to-low',views.filterByPrice_hl),
    path('filter-by-price-low-to-high',views.filterByPrice_lh),
    path('filter-by-name-a-z',views.filterByName_AZ),
    path('filter-by-name-z-a',views.filterByName_ZA),
    path('ProductDetails/<pid>',views.showProduct),
    path('AddToCart',views.addToCart),
    path('ShowCart',views.showCart),
    path('ShowBuild',views.showBuild),
    path('profile',views.showProfile),
    path('edit-profile',views.editProfile),
    path('contact_us',views.contactUS),
    path('search',views.searchProduct)
]
