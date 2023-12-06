from django import forms
from .models import Brand, Client, CommercialOrganization, Country, EstablishmentForm, Order, Product, Receipt, SalesPoint


# Создание списка, который будет отображать переданный параметр , а передавать ID записи
class CustomModelChoiceField(forms.ModelChoiceField):
    def __init__(self, queryset, label_field, **kwargs):
        self.label_field = label_field  # Отображаемый параметр
        super().__init__(queryset, **kwargs)

    def label_from_instance(self, obj):
        return getattr(obj, self.label_field)


# Создание списка, который будет отображать 3 переданных параметра, а передавать ID записи
class CustomTripleModelChoiceField(forms.ModelChoiceField):
    def __init__(self, queryset, label_field_1, label_field_2, label_field_3, **kwargs):
        # Отображаемые параметры
        self.label_field_1 = label_field_1
        self.label_field_2 = label_field_2
        self.label_field_3 = label_field_3
        super().__init__(queryset, **kwargs)

    def label_from_instance(self, obj):
        label_field_1 = getattr(obj, self.label_field_1)
        label_field_2 = getattr(obj, self.label_field_2)
        label_field_3 = getattr(obj, self.label_field_3)
        return f"{label_field_1} {label_field_2} {label_field_3}"


class BrandForm(forms.Form):
    name = forms.CharField(label="Название")


class ClientForm(forms.Form):
    name = forms.CharField(label="Имя")
    surname = forms.CharField(label="Фамилия")
    patronymic = forms.CharField(label="Отчество")
    birth = forms.DateField(label="Дата рождения", widget=forms.DateInput(attrs={'type': 'date'}))
    phone = forms.CharField(label="Номер телефона")


class CommercialOrganizationForm(forms.Form):
    name = forms.CharField(label="Название")
    link = forms.CharField(label="Ссылка")
    tin = forms.CharField(label="ИНН")
    establishment_form = CustomModelChoiceField(
        queryset=EstablishmentForm.objects.all(),
        label_field="form_name",
        label="Форма учреждения")


class CountryForm(forms.Form):
    name = forms.CharField(label="Название")


class EstablishmentFormForm(forms.Form):
    name = forms.CharField(label="Название")


class OrderForm(forms.Form):
    address = forms.CharField(label="Адрес доставки")
    status = forms.BooleanField(label="Статус заказа", widget=forms.CheckboxInput)
    date = forms.DateField(label="Дата доставки", widget=forms.DateInput(attrs={'type': 'date'}))
    client = CustomTripleModelChoiceField(
        queryset=Client.objects.all(),
        label_field_1="client_surname",
        label_field_2="client_name",
        label_field_3="client_patronymic",
        label="Клиент")
    sales_point = CustomModelChoiceField(
        queryset=SalesPoint.objects.all(),
        label_field="sales_point_address",
        label="Адрес торговой точки")


class ProductForm(forms.Form):
    type = forms.CharField(label="Тип товара")
    size = forms.FloatField(label="Размер(кг)")
    commercial_organization = CustomModelChoiceField(
        queryset=CommercialOrganization.objects.all(),
        label_field="organization_name",
        label="Коммерческая организация")
    brand = CustomModelChoiceField(
        queryset=Brand.objects.all(),
        label_field="brand_name",
        label="Брэнд")
    country = CustomModelChoiceField(
        queryset=Country.objects.all(),
        label_field="country_name",
        label="Страна")


class ReceiptForm(forms.Form):
    product_amount = forms.DecimalField(label="Количество товара")
    product_price = forms.CharField(label="Цена")
    order = CustomModelChoiceField(
        queryset=Order.objects.all(),
        label_field="order_date",
        label="Дата заказа")
    product = CustomModelChoiceField(
        queryset=Product.objects.all(),
        label_field="product_type",
        label="Тип товара")


class SalesPointForm(forms.Form):
    address = forms.CharField(label="Адрес")
    name = forms.CharField(label="Название")
    commercial_organization = CustomModelChoiceField(
        queryset=CommercialOrganization.objects.all(),
        label_field="organization_name",
        label="Коммерческая организация")
