## users - foydalanovchilar

foydalanovchilar bilan ishlaymiz

user > models.py
<details>

<summary>user > models.py</summary>

```ruby
   puts "Hello World"
```

</details>
<details>

<summary> email or username</summary>

## users>decorators.py
Djangodagi dekorativlar:
Men ushbu qo'llanmada dekorator yozyapman, chunki biz bir xil funktsiyani bir nechta funktsiyalarda ishlatamiz. Bu sizning ichkarida takrorlanadigan kod yozishni oldini oladi. Agar siz mening oldingi darsliklarimga rioya qilgan bo'lsangiz, biz tizimdan chiqishdan oldin foydalanuvchi tizimga kirganligini tekshirish uchun dekorativlardan foydalanganmiz; biz @login_required dan foydalandik. Hozir biz boshqa funksiyalarga kirishdan oldin foydalanuvchi foydalanuvchiga kirganligini tekshirmoqchimiz.

yaratish uchun
 Python Decorator funktsiyasi, biz funktsiyani argument sifatida qabul qiladigan tashqi funktsiyani yaratamiz. Bezatilgan funktsiyani o'rab turgan ichki funksiya ham mavjud. Python-ning asosiy dekoratori uchun sintaksis:
```pyton
from django.shortcuts import redirect

def user_not_authenticated(function=None, redirect_url='/'):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_url)
                
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    if function:
        return decorator(function)

    return decorator
```
```python
# /users/backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

UserModel = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
            return
        except UserModel.MultipleObjectsReturned:
            user = UserModel.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).order_by('id').first()

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
```
```python
# /users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, UserLoginForm
from .decorators import user_not_authenticated

# Create your views here.
@user_not_authenticated
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"New account created: {user.username}")
            return redirect('/')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="users/register.html",
        context={"form": form}

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("homepage")

@user_not_authenticated
def custom_login(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("homepage")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="users/login.html",
        context={"form": form}
        )
```

</details>
