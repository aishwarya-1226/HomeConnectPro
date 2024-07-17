from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views


from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/create/', views.create_property, name='create_property'),
    path('properties/<int:property_id>/', views.property_detail, name='property_detail'),
    path('properties/promote/<int:property_id>/', views.promote_property, name='promote_property'),
    path('inquiries/', views.inquiry_list, name='inquiry_list'),
    path('inquiries/<int:inquiry_id>/', views.inquiry_detail, name='inquiry_detail'),
    path('inquiries/create/<int:property_id>/', views.create_inquiry, name='create_inquiry'),
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/create/<int:property_id>/', views.create_review, name='create_review'),
    path('search/', views.search, name='search'),
    path('properties/<int:property_id>/reviews/', views.review_list, name='review_list'),
    path('properties/<int:property_id>/reviews/create/', views.create_review, name='create_review'),
    path('property_purchaser/reviews/', views.property_purchaser_reviews, name='property_purchaser_reviews'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



