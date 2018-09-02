from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
import random
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from . import models

class RegisterUser(CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'cadastrousuario.html'

class RegisterWord(CreateView):
    model = models.Word
    template_name = 'cadastropalavra.html'
    success_url = reverse_lazy('home')
    fields = ['word', 'clue']

class CreateMatch(ListView):
    model = models.Match
    template_name = 'partida.html'
    def post(self, form):
        if (models.Match.objects.filter(user_id = self.request.user.pk)):
            partida_user = models.Match.objects.get(user_id = self.request.user.pk)
            if (partida_user.status == 1):
                models.Match.objects.filter(user_id=self.request.user.pk).delete()
                palavras = models.Word.objects.all()
                list_id = []
                for x in palavras:
                    list_id.append(x.id)
                id_selecionado = random.choice(list_id)
                print (id_selecionado)
                palavraObj = models.Word.objects.get(id = id_selecionado)
                criacao = models.Match.objects.create(user_id=self.request.user.pk, word=palavraObj, status=2)
                criacao.save()
                return HttpResponseRedirect('/partida/')
            elif (partida_user.status == 2):
                return HttpResponseRedirect('/')
        else:
            palavras = models.Word.objects.all()
            list_id = []
            for x in palavras:
                list_id.append(x.id)
            id_selecionado = random.choice(list_id)
            print (id_selecionado)
            palavraObj = models.Word.objects.get(id = id_selecionado)
            criacao = models.Match.objects.create(user_id=self.request.user.pk, word=palavraObj, status=2)
            criacao.save()
            return HttpResponseRedirect('/partida/')

class GameMatch(ListView):
    model = models.Match
    template_name = 'jogo.html'
    def get_context_data(self, **kwargs):
        kwargs['match'] = models.Match.objects.filter(user_id = self.request.user.pk)
        return super(GameMatch, self).get_context_data(**kwargs)

# class MatchEmAndamento(ListView):