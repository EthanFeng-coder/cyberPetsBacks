import json

from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseForbidden

SECRECT_VALUE = 'qwerasdf1234'
SECRECT_KEY = 'auth'
'''
    request body should be like:
        {
            "auth": "qwerasdf1234",
            ...
        }
'''


def viewFunc(request):
    '''
    :param request
    :return: HttpResponse
    '''
    # try:
    #     print(request.body)
    # except Exception as e:
    #     return HttpResponse('error')
    # print(request)
    print('test')
    return HttpResponse(json.dumps({'title': 'it\'s just a test'}))


#
#
# def search_post(request):
#     try:
#         question = POST_get(request, 'question')
#         #print(request)
#         answer_dict = SearchBasicRequest().search_request(request)
#         js = answer_dict
#         return HttpResponse(json.dumps(js, ensure_ascii=False), content_type="application/json,charset=utf-8")
#
#     except Exception as e:
#         zlogger.logger.error(e)
#     return HttpResponse(json.dumps(js, ensure_ascii=False), content_type="application/json,charset=utf-8")
#
#
# def search_get(request):
#     try:
#         uid = request.GET.get('uid')
#         cid = request.GET.get('cid')
#         question = request.GET.get('question')
#         page = request.GET.get('page')
#         print(uid)
#         # Assuming SearchBasicRequest().search_request(request) can handle the GET request as well
#         answer_dict = SearchBasicRequest().search_request_get(request)
#
#         js = answer_dict
#         return HttpResponse(json.dumps(js, ensure_ascii=False), content_type="application/json,charset=utf-8")
#
#     except Exception as e:
#         zlogger.logger.error(e)
#         js = {"error": str(e)}
#     return HttpResponse(json.dumps(js, ensure_ascii=False), content_type="application/json,charset=utf-8")

def connectView(request):
    """
    :param request: it should be a post reqeust
    :return:
    """

    if request.method == 'POST':
        body = request.body
        auth_key = ''
        try:
            auth_key = json.loads(body)[SECRECT_KEY]
        except Exception as e:
            return HttpResponseForbidden('Unauthorized')
        if auth_key != SECRECT_VALUE:
            return HttpResponseForbidden('Unauthorized')
        return HttpResponse(json.dumps({'message': 'success!'}))

    else:
        return HttpResponseNotAllowed('Method not allowed')
