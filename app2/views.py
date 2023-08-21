from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test_post(request):
    print(request.method) #获取请求中的使用的HTTP方式(POST/GET)
    print(request.POST.get('username'))
    return render(request,'2/test_post.html')\

def test_get(request):
    print(request.get_host()) #域名+端口
    print(request.get_full_path()) #全部路径，包含参数
    print(request.path) #获取访问文件路径，不含参数
    print(request.get_full_path())#获取访问文件路径，包含参数
    print(request.method) #获取请求中的使用的HTTP方式(POST/GET)
    print(request.GET) #获取GET请求的参数
    print(request.META["HTTP_USER_AGENT"]) #用户浏览器的user-agent字符串
    print(request.META["REMOTE_ADDR"]) #客户端IP
    print(request.GET.get('username'))#获取get参数
    return HttpResponse("")