from django.shortcuts import render, redirect # type: ignore
from .forms import ProdutoForm

def produto_new(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo produto no banco de dados
            return redirect('produto_success')  # Redireciona para uma página de sucesso
    else:
        form = ProdutoForm()
    return render(request, 'produto_new.html', {'form': form})

def produto_success(request):
    return render(request, 'produto_success.html')