from django.shortcuts import render # type: ignore

# Create your views here.
# Define các hàm để trả về trang index.html
def get_home(request):
    return render(request,'index.html')
