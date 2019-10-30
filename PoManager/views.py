from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponse
from datetime import datetime, timedelta

from .models import Product, PoItem
from .pomanager_response import ListResponse, genPoItemResponse, genProductResponse

from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

class AchView(generic.ListView):

    def get_queryset(self):
        return Product.objects.all()


# @login_required
# @permission_required('pomanager.view_poitem')
def listPoItemFromPoNum(request, po_num, minDateText=None, maxDateText=None):
    listResponse = ListResponse(request)
    listResponse.setMinDate(minDateText)
    listResponse.setMaxDate(maxDateText)
    listResponse.setQuerySet( PoItem.objects.filter(po__num__icontains = po_num).filter(due_date__gte=listResponse.minDate).filter(due_date__lte=listResponse.maxDate) )
    listResponse.setQueryDescription( "PO item(s) that contain '%s' in their PO #" % (po_num) )
    return genPoItemResponse(listResponse)

def listPoItemFromPn(request, pn, minDateText=None, maxDateText=None):
    listResponse = ListResponse(request)
    listResponse.setMinDate(minDateText)
    listResponse.setMaxDate(maxDateText)
    listResponse.setQuerySet( PoItem.objects.filter(revision__product__pn__icontains = pn).filter(due_date__gte=listResponse.minDate).filter(due_date__lte=listResponse.maxDate) )
    listResponse.setQueryDescription( "PO item(s) that contain '%s' in their P/N" % (pn) )
    return genPoItemResponse(listResponse)

def listPoItemFromDescription(request, description, minDateText=None, maxDateText=None):
    listResponse = ListResponse(request)
    listResponse.setMinDate(minDateText)
    listResponse.setMaxDate(maxDateText)
    listResponse.setQuerySet( PoItem.objects.filter(revision__product__description__icontains = description).filter(due_date__gte=listResponse.minDate).filter(due_date__lte=listResponse.maxDate) )
    listResponse.setQueryDescription( "PO item(s) that contain(s) '%s' in their description" % (description) )
    return genPoItemResponse(listResponse)

def listProductFromPn(request, pn):
    listResponse = ListResponse(request)
    listResponse.setQuerySet( Product.objects.filter(pn__icontains = pn) )
    listResponse.setQueryDescription( "Product(s) that contain(s) '%s' in their P/N" % (pn))
    return genProductResponse(listResponse)

def listProductFromDescription(request, description):
    listResponse = ListResponse(request)
    listResponse.setQuerySet( Product.objects.filter(description__icontains = description) )
    listResponse.setQueryDescription( "Product(s) that contain(s) '%s' in their description" % (description))
    return genProductResponse(listResponse)


def test_ach(request, une_valeur):
    return HttpResponse("%s" %une_valeur)
