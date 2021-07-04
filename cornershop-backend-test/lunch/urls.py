from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from lunch.views import MenuCreateView, MenuUpdateView, LoginView, \
    LogoutView, OrdersView, OrderListView, DetailMenuView

urlpatterns = [
    path("", TemplateView.as_view(template_name="lunch/index.html"),
         name="index"),
    path("login", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("menu/add/", MenuCreateView.as_view(), name="menu-add"),
    path("menu/update/<int:pk>/", MenuUpdateView.as_view(),
         name="menu-update"),
    path("menu/<uuid:unique_id>/", DetailMenuView.as_view(), name="menu"),
    path("menu/", login_required(OrdersView.as_view(), login_url="/login"),
         name="menu"),
    path('orders-list/',
         login_required(OrderListView.as_view(), login_url='/login'),
         name='orders-list'),
]
