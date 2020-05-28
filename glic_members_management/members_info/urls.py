from django.urls import path
from members_info import views

urlpatterns = [
    path('info', views.all_members, name='all_members'),
    path('more/<member_id>',views.more_info,name='more_info'),
    path('delete/<member_id>',views.delete_member,name='delete_member'),
    path('edit/<member_id>',views.edit_member,name='edit_member'),
    path('new',views.new_member,name='new_member')
]
