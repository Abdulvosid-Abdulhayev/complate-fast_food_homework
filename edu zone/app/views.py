from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data.get('user_id')
            password = form.cleaned_data.get('password')

            # Foydalanuvchini ID bo'yicha qidirish va tekshirish
            try:
                # `id` orqali foydalanuvchini topish
                user = User.objects.get(id=user_id)
                # Foydalanuvchini autentifikatsiya qilish (user_id bo'yicha username qidiriladi)
                user = authenticate(request, username=user.username, password=password)
                
                if user is not None:
                    login(request, user)
                    return redirect('home')  # Agar login muvaffaqiyatli bo'lsa, `home` sahifasiga yo'naltirish
                else:
                    messages.error(request, 'Noto‘g‘ri ID yoki parol')
            except User.DoesNotExist:
                # Agar user topilmasa, xatolik xabari
                messages.error(request, 'Bunday ID mavjud emas')
                return redirect('login')  # Login oynasiga qaytarish
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})




def index(request):
    return render(request, 'index.html')