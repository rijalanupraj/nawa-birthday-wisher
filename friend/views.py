# External Import
from django.shortcuts import render
# import datetime
from django.utils import timezone

# Internal Import
from friend.models import Friend


def homerender(request):
    today_date = timezone.now().date()
    today_birthdays = Friend.objects.filter(
        dob=today_date, is_active=True).order_by('-importance_level')
    print(today_birthdays)
    context = {
        'birthdays': today_birthdays,
    }
    return render(request, 'friend/home-page.html', context)
