from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ComLog
from django.contrib import messages
from .forms import ComLogForm
from contacts.models import Church, People
from django.http import JsonResponse
from django.db.models import Q
import logging
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

logger = logging.getLogger(__name__)
@method_decorator(login_required, name='dispatch')
class ComLogListView(ListView, LoginRequiredMixin):
    model = ComLog
    template_name = 'com_log/com_log_list.html'
    context_object_name = 'com_logs'
    paginate_by = 20

    def get_queryset(self):
        queryset = ComLog.objects.select_related('content_type').order_by('-date')
        logger.info(f"ComLog queryset count: {queryset.count()}")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['com_logs'] = [
            {
                'id': log.id,
                'name': log.get_contact_name(),
                'type': log.get_contact_type(),
                'communication_type': log.get_communication_type_display(),
                'notes': log.notes,
                'date': log.date,
            }
            for log in context['com_logs']
        ]
        logger.info(f"ComLog context count: {len(context['com_logs'])}")
        return context
@method_decorator(login_required, name='dispatch')
class ComLogDetailView(DetailView, LoginRequiredMixin):
    model = ComLog
    template_name = 'com_log/com_log_detail.html'
    context_object_name = 'com_log'
@method_decorator(login_required, name='dispatch')
class ComLogCreateView(LoginRequiredMixin, CreateView):
    model = ComLog
    form_class = ComLogForm
    template_name = 'com_log/com_log_form.html'
    success_url = reverse_lazy('com_log:list')

    def form_valid(self, form):
        logger.info(f"Form data: {form.cleaned_data}")
        try:
            self.object = form.save()
            logger.info(f"ComLog created: {self.object.id}")
            messages.success(self.request, 'Communication log created successfully.')
            return redirect(self.get_success_url())
        except Exception as e:
            logger.error(f"Error creating ComLog: {str(e)}")
            messages.error(self.request, 'An error occurred while creating the communication log.')
            return self.form_invalid(form)

    def form_invalid(self, form):
        logger.error(f"ComLog form invalid: {form.errors}")
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

def contact_search(request):
    contact_type = request.GET.get('type')
    query = request.GET.get('term', '')
    logger.info(f"Contact search: type={contact_type}, query={query}")

    results = []

    if contact_type == 'church':
        churches = Church.objects.filter(church_name__icontains=query)[:10]
        results = [{'id': church.id, 'value': church.church_name, 'label': church.church_name} for church in churches]
    elif contact_type == 'people':
        people = People.objects.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query)
        )[:10]
        results = [{'id': person.id, 'value': f"{person.first_name} {person.last_name}", 'label': f"{person.first_name} {person.last_name}"} for person in people]

    logger.info(f"Contact search results: {results}")
    return JsonResponse(results, safe=False)
@method_decorator(login_required, name='dispatch')
class ComLogUpdateView(UpdateView, LoginRequiredMixin):
    model = ComLog
    form_class = ComLogForm
    template_name = 'com_log/com_log_form.html'
    success_url = reverse_lazy('com_log:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
@method_decorator(login_required, name='dispatch')  
class ContactInteractionsListView(ListView, LoginRequiredMixin):
    model = ComLog
    template_name = 'com_log/contact_interactions_list.html'
    context_object_name = 'interactions'
    paginate_by = 20

    def get_queryset(self):
        contact_type = self.kwargs['contact_type']
        contact_id = self.kwargs['contact_id']

        if contact_type == 'person':
            contact = get_object_or_404(People, id=contact_id)
        elif contact_type == 'church':
            contact = get_object_or_404(Church, id=contact_id)
        else:
            raise ValueError("Invalid contact type")

        content_type = ContentType.objects.get_for_model(contact)
        return ComLog.objects.filter(content_type=content_type, object_id=contact.id).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contact_type = self.kwargs['contact_type']
        contact_id = self.kwargs['contact_id']

        if contact_type == 'person':
            contact = get_object_or_404(People, id=contact_id)
        elif contact_type == 'church':
            contact = get_object_or_404(Church, id=contact_id)

        context['contact'] = contact
        context['contact_type'] = contact_type
        return context
