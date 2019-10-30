from datetime import datetime, timedelta
from django.shortcuts import render
from .xlsresponse import genPoItemXlsResponse, genProductXlsResponse

class ListResponse:

    def __init__(self, request):
        self.request = request

    def setMinDate(self, minDateText):
        if minDateText:
            self.minDate = datetime.strptime(minDateText, '%Y-%m-%d')
        else:
            self.minDate = datetime.now() + timedelta(days=-365)

    def setMaxDate(self, maxDateText):
        if maxDateText:
            self.maxDate = datetime.strptime(maxDateText, '%Y-%m-%d')
        else:
            self.maxDate = datetime.now() + timedelta(days=365)

    def setQuerySet(self, query_set):
        self.query_set = query_set

    def setQueryDescription(self, query_description):
        self.query_description = query_description

def genPoItemResponse(listResponse):
    if 'xls' in listResponse.request.GET:
        return genPoItemXlsResponse(listResponse)
    else:
        return render(listResponse.request, 'pomanager/list_PoItem.html', {'poitem_list': listResponse.query_set, 'query_description': listResponse.query_description, 'minDate': listResponse.minDate, 'maxDate': listResponse.maxDate})


def genProductResponse(listResponse):
    if 'xls' in listResponse.request.GET:
        return genProductXlsResponse(listResponse)
    else:
        return render(listResponse.request, 'pomanager/list_Product.html', {'product_list': listResponse.query_set, 'query_description': listResponse.query_description})
