
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Projeto
from .form import ProjetoForm


def lista_projetos(request):
    projetos = Projeto.objects.all()

    return render(
        request,
        "core/lista_projetos.html",
        {"projetos": projetos}
    )


def criar_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Projeto cadastrado com sucesso!"
            )
            return redirect("lista_projetos")
    else:
        form = ProjetoForm()

    return render(
        request,
        "core/form_projeto.html",
        {"form": form, "titulo": "Cadastrar Projeto"}
    )


def editar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == "POST":
        form = ProjetoForm(request.POST, instance=projeto)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Projeto atualizado com sucesso!"
            )
            return redirect("lista_projetos")
    else:
        form = ProjetoForm(instance=projeto)

    return render(
        request,
        "core/form_projeto.html",
        {"form": form, "titulo": "Editar Projeto"}
    )


def excluir_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == "POST":
        projeto.delete()
        messages.success(
            request,
            "Projeto excluído com sucesso!"
        )
        return redirect("lista_projetos")

    return render(
        request,
        "core/confirmar_exclusao.html",
        {"projeto": projeto}
    )