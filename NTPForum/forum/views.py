from django.shortcuts import render, redirect
from . import models


def homeView(response):
    renderDict = {}
    renderDict['threads'] = models.Thread.objects.all()
    return render(response, "home.html", renderDict)


def threadView(response, idx=-1):
    if response.method == "POST":
        if response.user.is_authenticated:
            if response.POST.get("submit"):
                # TODO: Add data validation.
                models.Thread.objects.filter(id=idx).first().post_set.create(
                    author=response.user,
                    text=response.POST.get("text")
                )
                return redirect(f"/thread/{idx}")
        else:
            return redirect('/login/')

    renderDict = {}
    renderDict['thread'] = models.Thread.objects.filter(id=idx).first()
    return render(response, "threadDetails.html", renderDict)


def createThreadView(response):
    if response.user.is_authenticated:
        if response.method == "POST":
            if response.POST.get("submit"):
                # TODO: Add data validation.
                newThread = response.user.thread_set.create(
                    title=response.POST.get("title"),
                    text=response.POST.get("text")
                )
                return redirect(f"/thread/{newThread.id}")

        renderDict = {}
        return render(response, "threadAdd.html", renderDict)
    else:
        return redirect('/login/')
