# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.conf import settings
from django.http import Http404
from myapp import logger

from .models import Document
from .forms import DocumentForm
from .logger import *
from django.core import serializers



def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            logger.info("successfully uploaded")

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))

    else:
        form = DocumentForm()  # A empty, unbound form
        logger.info("form is loaded successfully")

    # Load documents for the list page
    documents = Document.objects.all()
    data = serializers.serialize('json', documents)
    logger.info(data)

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
)

def test(request):
    content = {}
    logger.info("success")
    return render_to_response('test.html',context_instance=RequestContext(request))

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            logger.info("successfully downloaded")
            return response
    logger.error("please verify again")
    raise Http404
def address(request):
    documents = Document.objects.all()
    context = {'documents': documents}
    return render(request,'address.html',context)