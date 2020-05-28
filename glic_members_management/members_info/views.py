from django.shortcuts import render,redirect
from members_info.models import Profile
from members_info.forms import MemberForm
from django.contrib import messages
# Create your views here.
# fetch all data and display it inside home.html
def all_members(request):
    members = Profile.objects.all()
    context = {
        'members':members
    }
    return render(request,'home.html',context)

# fetch a single data using Id and display it more.html
def more_info(request,member_id):
    member = Profile.objects.get(pk=member_id)
    context = {
        'member': member
    }
    return render(request,'more.html',context)

# handle a form to add new member
def new_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'New Member added')
            return redirect('new_member')
    else:
        form = MemberForm()
    context = {
        'form': form
    }
    return render(request,'new.html',context)

# delete a single data
def delete_member(request,member_id):
    member = Profile.objects.get(pk=member_id)
    member.delete()
    return redirect('all_members')

# edit data 
def edit_member(request,member_id):
    if request.method == 'POST':
        member = Profile.objects.get(pk=member_id)
        form = MemberForm(request.POST,request.FILES,instance=member)
        if form.is_valid():
            form.save()
            return redirect('all_members')
    else:
        member = Profile.objects.get(pk=member_id)
        form = MemberForm(instance=member)
    context = {
        'form': form 
    }
    return render(request,'edit.html',context)