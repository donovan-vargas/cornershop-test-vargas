import datetime

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import FormView, RedirectView
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from employees.models import Employee
from lunch.forms import MenuForm, OrderForm
from lunch.models import Menu, MenuOptions, Orders


class LoginView(FormView):
    """
    A class to represent a LoginView implements FormView
    login users.
    ...

    Attributes
    ----------
    form_class : AuthenticationForm
        generic auth form
    template_name :
    success_url :
        return template when request code 200
    """
    form_class = AuthenticationForm
    template_name = "lunch/login.html"
    success_url = reverse_lazy("index")

    def dispatch(self, request, *args, **kwargs):
        """
        Override dispatch method
        dispatch request method
        :param request:
        :param args:
        :param kwargs:
        :return: LoginView
        """
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Override form_valid method
        Validation form AuthenticationForm
        :param form:
        :return: LoginView
        """
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    """
    A class to represent a LogoutView implements RedirectView
    logout users.
    ...

    Attributes
    ----------
    pattern_name :
        pattern view
    """
    pattern_name = "login"

    def get(self, request, *args, **kwargs):
        """
        Override get method
        to logout and return view
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


@method_decorator(login_required(login_url="/login"), name="dispatch")
@method_decorator(
    permission_required("menu.can_create_menu", login_url="/login"),
    name="dispatch")
class MenuCreateView(CreateView, ListView):
    """
    A class to represent a MenuCreateView implements CreateView and ListView
    login users.
    User must be logged
    User must to have menu.can_create_menu permission
    ...

    Attributes
    ----------
    model : Model class
        model class to save update and delete methods
    context_object_name : context
        context data for template
    form_class : Form
        Form to create Menu and MenuOptions items
    """
    model = Menu
    context_object_name = "menu_list"
    form_class = MenuForm
    success_url = reverse_lazy("menu-add")

    def post(self, request, *args, **kwargs):
        """
        Override post method
        Save Menu and MenuOptions items
        :param request:
        :param args:
        :param kwargs:
        :return: template
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            options = request.POST.getlist('option')
            print(options)
            form.instance.menu_user = self.request.user
            date = self.request.POST.get("date")
            if not Menu.objects.filter(date=date, active=True).exists():
                self.object = form.save()
                for option in options:
                    MenuOptions(
                        menu=self.object,
                        option=option
                    ).save()
                messages.success(request, "Menu creado")
                return HttpResponseRedirect(self.get_success_url())
            else:
                messages.success(request, "Ya hay un meno para esa fecha")
        return render(request, "lunch/menu_form.html", {"form": form})


class DetailMenuView(DetailView):
    model = Menu
    slug_url_kwarg = "unique_id"
    slug_field = "unique_id"
    template_name = "lunch/menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context.get('menu').date != datetime.date.today():
            raise Http404("Menu no activo para hoy.")
        return context


@method_decorator(
    permission_required("menu.can_edit_menu", login_url="/login"),
    name="dispatch")
class MenuUpdateView(UpdateView):
    """
    A class to represent a OrdersView implements CreateView
    Get order list options for today.
    ...

    Attributes
    ----------
    model : Menu
        Model to update
    form_class: MenuForm
        Form for template
    success_url: menu-add
        url success request
    """
    model = Menu
    context_object_name = "menu_list"
    form_class = MenuForm
    success_url = reverse_lazy("menu-add")

    def post(self, request, *args, **kwargs):
        """
        Override post method
        Save Menu and MenuOptions items
        :param request:
        :param args:
        :param kwargs:
        :return: template
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            options = request.POST.getlist('option')
            menu = self.get_object()
            super(MenuUpdateView, self).post(request, *args, **kwargs)
            menu_options = list(
                MenuOptions.objects.filter(menu=menu, active=True))
            for count, value in enumerate(options):
                menu_options[count].option = value
            MenuOptions.objects.bulk_update(menu_options, ["option"])
            messages.success(request, "Menu creado")
            return HttpResponseRedirect(self.get_success_url())
        return render(request, "lunch/menu_form.html", {"form": form})


class OrdersView(CreateView):
    """
    A class to represent a OrdersView implements CreateView
    Get order list options for today.
    ...

    Attributes
    ----------
    model : Orders
        Model to save
    form_class: OrderForm
        Form for template
    """
    model = Orders
    form_class = OrderForm

    def get_context_data(self, **kwargs):
        """
        Override get_context_data method
        to get today orders
        :param kwargs:
        :return:
        """
        self.object_list = self.model.objects.filter(
            created=datetime.datetime.today(), active=True)
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        """
        Override post method
        To get Orders and identify user request
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if self.request.user.is_authenticated:
            user = self.request.user
            user_employee = Employee.objects.get_or_404(employee=user,
                                                        active=True)
            form = self.form_class(request.POST)
            if form.is_valid():
                form.instance.employee = user_employee
                self.object = form.save()
                messages.success(request,
                                 "Hola {}".format(
                                     user_employee.employee.username))
                messages.success(request, "Tu orden ha sido recibida")
        return render(request, "lunch/orders_form.html", {"form": form})

    def get(self, request, *args, **kwargs):
        """
        Override get method
        to return form and uuid
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        form = OrderForm()
        uuid = self.kwargs.get("unique_id")
        return render(request, "lunch/orders_form.html",
                      {"uuid": uuid, "form": form})


@method_decorator(
    permission_required("orders.can_see_orders", login_url="/login"),
    name="dispatch")
class OrderListView(ListView):
    """
    A class to represent a OrderListView implements ListView
    Get orders list for today.
    ...

    Attributes
    ----------
    model : Orders
        Model to save
    form_class: OrderForm
        Form for template
    """
    model = Orders
    context_object_name = "orders_list"
