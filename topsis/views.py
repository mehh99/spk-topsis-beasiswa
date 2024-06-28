import numpy as np

from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse

from topsis.forms import DataForm
from topsis.models import Data
from topsis.topsis import Topsis
from datetime import datetime

# def index(request, year=None):
#     if year is None:
#         year = datetime.now().year
#     else:
#         year = int(year)
    
#     data = Data.objects.filter(tahun=year)
    
#     field_names = [f.verbose_name for f in Data._meta.get_fields()]
#     weights = [5, 3, 3, 3, 4, 4]
#     criterias = np.array([True, True, True, True, True, True])
#     arr = []
#     for d in data:
#         arr.append(
#             [
#                 [d.kondisi_ekonomi],
#                 [d.kondisi_rumah],
#                 [d.pekerjaan],
#                 [d.penghasilan],
#                 [d.tanggungan],
#                 [d.keterangan],
#             ]
#         )

#     evaluation_matrix = np.array(arr)
#     t = Topsis(evaluation_matrix, weights, criterias)
#     t.calc()

#     for i, d in enumerate(data):
#         d.best_distance = t.best_distance[i]
#         d.worst_distance = t.worst_distance[i]
#         d.worst_similarity = t.worst_similarity[i]
#         d.worst_similarity_rank = t.rank_to_worst_similarity()[i]
#         d.best_similarity = t.best_similarity[i]
#         d.best_similarity_rank = t.rank_to_best_similarity()[i]
#         d.weighted_normalized = t.weighted_normalized[i]
#         #1 
#         d.evaluation_matrix = t.evaluation_matrix[i]
#         d.normalized_decision = t.normalized_decision[i]  # Normalisation matrix

#         # d.ci_plus = t.calculate_ci_plus()[i]
    
#     available_years = Data.objects.values_list('tahun', flat=True).distinct()

#     context = {
#         "data": data,
#         "field_names": field_names,
#         "selected_year": int(year),
#         "available_years": available_years,
#     }

#     return render(request, "index.html", context)
def index(request):
    year = request.GET.get('year', None)
    
    if year is None:
        year = datetime.now().year
    else:
        year = int(year)
    
    data = Data.objects.filter(tahun=str(year))
    
    field_names = [f.verbose_name for f in Data._meta.get_fields()]
    weights = [5, 3, 3, 3, 4, 4]
    criterias = np.array([True, True, True, True, True, True])
    arr = []
    for d in data:
        arr.append(
            [
                [d.surat_keterangan_tidak_mampu],
                [d.kondisi_rumah],
                [d.keaktifan_ekstrakurikuler],
                [d.penghasilan],
                [d.tanggungan],
                [d.keterangan],
            ]
        )

    evaluation_matrix = np.array(arr)
    t = Topsis(evaluation_matrix, weights, criterias)
    t.calc()

    for i, d in enumerate(data):
        d.best_distance = t.best_distance[i]
        d.worst_distance = t.worst_distance[i]
        d.worst_similarity = t.worst_similarity[i]
        d.worst_similarity_rank = t.rank_to_worst_similarity()[i]
        d.best_similarity = t.best_similarity[i]
        d.best_similarity_rank = t.rank_to_best_similarity()[i]
        d.weighted_normalized = t.weighted_normalized[i]
        #1 
        d.evaluation_matrix = t.evaluation_matrix[i]
        d.normalized_decision = t.normalized_decision[i]  # Normalisation matrix

        # d.ci_plus = t.calculate_ci_plus()[i]
    
    available_years = Data.objects.values_list('tahun', flat=True).distinct()

    context = {
        "data": data,
        "field_names": field_names,
        "selected_year": int(year),
        "available_years": available_years,
    }

    return render(request, "index.html", context)

def edit(request, id):
    category = get_object_or_404(Data, id=id)
    form = DataForm(instance=category)
    context = {
        'form': form,
        'category': category,  # Sertakan category dalam konteks
    }
    return render(request, 'topsis_edit.html', context)



# Perbaikan pada fungsi update
def update(request, id):
    category = get_object_or_404(Data, id=id)
    if request.method == 'POST':
        form = DataForm(request.POST, instance=category)  # Gunakan instance=category untuk mengisi form dengan data yang sudah ada
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))  # Redirect ke halaman utama setelah berhasil diperbarui
    else:
        form = DataForm(instance=category)  # Gunakan instance=category untuk mengisi form dengan data yang sudah ada

    context = {
        'form': form,  # Gunakan form yang sudah diisi dengan data objek category
    }
    return render(request, 'topsis_edit.html', context)


# Perbaikan pada fungsi delete

def delete (request,id):
    category = get_object_or_404(Data,id=id)
    category.delete()
    return redirect('index')
# def analysis(request):
#     data = Data.objects.all()
#     weights = [5, 3, 3, 3, 4, 4]
#     criteria = np.array([True, True, True, True, True, True])
#     arr = []
#     for d in data:
#         arr.append(
#             [
#                 [d.kondisi_ekonomi],
#                 [d.kondisi_rumah],
#                 [d.pekerjaan],
#                 [d.penghasilan],
#                 [d.tanggungan],
#                 [d.keterangan],

#             ]
#         )

#     evaluation_matrix = np.array(arr)
#     t = Topsis(evaluation_matrix, weights, criteria)
#     t.calc()

#     for i, d in enumerate(data):
#         d.best_distance = t.best_distance[i]
#         d.worst_distance = t.worst_distance[i]
#         d.worst_similarity = t.worst_similarity[i]
#         d.worst_similarity_rank = t.rank_to_worst_similarity()[i]
#         d.best_similarity = t.best_similarity[i]
#         d.best_similarity_rank = t.rank_to_best_similarity()[i]
#         d.weighted_normalized = t.weighted_normalized[i]
        
#         #1 
#         d.evaluation_matrix = t.evaluation_matrix[i]
#         d.normalized_decision = t.normalized_decision[i]
#         # d.ci_plus = t.calculate_ci_plus()[i]

#     context = {"data": data}

#     return render(request, "analysis.html", context)

# def analysis_wakil(request):
#     data = Data.objects.all()
#     weights = [5, 3, 3, 3, 4, 4]
#     criteria = np.array([True, True, True, True, True, True])
#     arr = []
#     for d in data:
#         arr.append(
#             [
#                 [d.kondisi_ekonomi],
#                 [d.kondisi_rumah],
#                 [d.pekerjaan],
#                 [d.penghasilan],
#                 [d.tanggungan],
#                 [d.keterangan],

#             ]
#         )

#     evaluation_matrix = np.array(arr)
#     t = Topsis(evaluation_matrix, weights, criteria)
#     t.calc()

#     for i, d in enumerate(data):
#         d.best_distance = t.best_distance[i]
#         d.worst_distance = t.worst_distance[i]
#         d.worst_similarity = t.worst_similarity[i]
#         d.worst_similarity_rank = t.rank_to_worst_similarity()[i]
#         d.best_similarity = t.best_similarity[i]
#         d.best_similarity_rank = t.rank_to_best_similarity()[i]
#         d.weighted_normalized = t.weighted_normalized[i]
        
#         #1 
#         d.evaluation_matrix = t.evaluation_matrix[i]
#         d.normalized_decision = t.normalized_decision[i]
#         # d.ci_plus = t.calculate_ci_plus()[i]

#     context = {"data": data}

#     return render(request, "analysis_wakil.html", context)
# views.py

def analysis(request):
    selected_year = request.GET.get('year', None)

    if selected_year is None:
        selected_year = datetime.now().year
    else:
        selected_year = int(selected_year)

    data = Data.objects.filter(tahun=selected_year)
    
    weights = [5, 3, 3, 3, 4, 4]
    criteria = np.array([True, True, True, True, True, True])
    arr = []
    for d in data:
        arr.append(
            [
                [d.surat_keterangan_tidak_mampu],
                [d.kondisi_rumah],
                [d.keaktifan_ekstrakurikuler],
                [d.penghasilan],
                [d.tanggungan],
                [d.keterangan],
            ]
        )

    evaluation_matrix = np.array(arr)
    t = Topsis(evaluation_matrix, weights, criteria)
    t.calc()

    for i, d in enumerate(data):
        d.best_distance = t.best_distance[i]
        d.worst_distance = t.worst_distance[i]
        d.worst_similarity = t.worst_similarity[i]
        d.worst_similarity_rank = t.rank_to_worst_similarity()[i]
        d.best_similarity = t.best_similarity[i]
        d.best_similarity_rank = t.rank_to_best_similarity()[i]
        d.weighted_normalized = t.weighted_normalized[i]
        
        d.evaluation_matrix = t.evaluation_matrix[i]
        d.normalized_decision = t.normalized_decision[i]

    available_years = Data.objects.values_list('tahun', flat=True).distinct()

    context = {
        "data": data,
        "selected_year": int(selected_year),
        "available_years": available_years,
    }

    return render(request, "analysis.html", context)


# views.py

def analysis_wakil(request):
    selected_year = request.GET.get('year', None)

    if selected_year is None:
        selected_year = datetime.now().year
    else:
        selected_year = int(selected_year)

    data = Data.objects.filter(tahun=selected_year)
    
    weights = [5, 3, 3, 3, 4, 4]
    criteria = np.array([True, True, True, True, True, True])
    arr = []
    for d in data:
        arr.append(
            [
                [d.surat_keterangan_tidak_mampu],
                [d.kondisi_rumah],
                [d.keaktifan_ekstrakurikuler],
                [d.penghasilan],
                [d.tanggungan],
                [d.keterangan],
            ]
        )

    evaluation_matrix = np.array(arr)
    t = Topsis(evaluation_matrix, weights, criteria)
    t.calc()

    for i, d in enumerate(data):
        d.best_distance = t.best_distance[i]
        d.worst_distance = t.worst_distance[i]
        d.worst_similarity = t.worst_similarity[i]
        d.worst_similarity_rank = t.rank_to_worst_similarity()[i]
        d.best_similarity = t.best_similarity[i]
        d.best_similarity_rank = t.rank_to_best_similarity()[i]
        d.weighted_normalized = t.weighted_normalized[i]
        
        d.evaluation_matrix = t.evaluation_matrix[i]
        d.normalized_decision = t.normalized_decision[i]

    available_years = Data.objects.values_list('tahun', flat=True).distinct()

    context = {
        "data": data,
        "selected_year": int(selected_year),
        "available_years": available_years,
    }

    return render(request, "analysis_wakil.html", context)



def input(request):

    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = DataForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect(redirect_to=reverse("index"))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DataForm()

    context = {"form": form}

    return render(request, "input.html", context)