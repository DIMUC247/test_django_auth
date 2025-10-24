from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.views.decorators.http import require_GET, require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import PlannerForm
from .models import Planner
from PhoneBook.models import Contact

# Create your views here.

@require_GET
def get_add_form(request: HttpRequest):
    return render(request, "add_meet.html", dict(form=PlannerForm()))


@require_POST
def add_planner(request: HttpRequest):
    form = PlannerForm(data=request.POST)
    if form.is_valid():
        planner: Planner = form.save(commit=False)
        planner.user = request.user
        planner.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Зустріч успішно додана!")
        return redirect("planners")

    messages.add_message(request=request, level=messages.ERROR, message="Форма заповнена некоректно!")
    return render(request, "add_meet.html", dict(form=form))


@require_GET
@login_required
def get_planners(request: HttpRequest):
    planners = Planner.objects.filter(user=request.user).all()
    return render(request, "planners.html", dict(planners=planners))


class PlannerView(ListView):
    def get(self,request:HttpRequest):
        current_page = request.GET.get("page",1)
        paginator = Paginator(Planner.objects.filter(user=request.user).all(),2)
        page_obj = paginator.get_page(current_page)
        return render(request, "planners_view.html", dict(page_obj=page_obj))


@login_required
def get_planners_with_me(request: HttpRequest):
    current_page = request.GET.get("page",1)
    planners_obj = Planner.objects.filter(
        contact__first_name=request.user.first_name,
        contact__last_name=request.user.last_name
        ).all()
    paginator = Paginator(planners_obj, 2)
    planners = paginator.get_page(current_page)
    return render(request, "planners_with_me.html", dict(planners=planners))


@require_GET
@login_required
def accept_meet(request: HttpRequest,meet_id:int):
    meet = Planner.objects.filter(pk=meet_id,
            contact__first_name=request.user.first_name,
            contact__last_name=request.user.last_name
        ).first()
    meet.accepted = True
    meet.save()
    return redirect("planners_with_me")


@require_GET
@login_required
def reject_meet(request:HttpRequest,meet_id:int):
    meet = Planner.objects.filter(
            pk=meet_id,
            contact__first_name=request.user.first_name,
            contact__last_name=request.user.last_name
        ).first()
    meet.accepted = False
    meet.save()
    return redirect("planners_with_me")