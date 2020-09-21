from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Pharacter, MoviePharacter, Planet, Movie
from api.serializers import PharacterSerializers, MoviePharacterSerializers

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def pharacter_list(request):
    """
    List all code pharacter, or create a new pharacter.
    """
    if request.method == 'GET':
        pharacter = Pharacter.objects.all()
        serializer = PharacterSerializers(pharacter, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':        
        data = JSONParser().parse(request)  
        if 'name_pharacter' in data:
            result=[]
            find_pharacter = Pharacter.objects.filter(name__contains=str(data['name_pharacter'])).values()
            mp_mv = []
            for find_info in find_pharacter:
                list_mp_ph = MoviePharacter.objects.filter(pharacters_id=find_info['id']).values()
                if len(list_mp_ph)>0:
                    for info_list in list_mp_ph:                    
                        mv_ = Movie.objects.filter(id=info_list['movie_id']).values()
                        pl_ = Planet.objects.filter(movie_planet_id=info_list['movie_id']).values()
                        json_mov = mv_[0]
                        json_mov['planet'] = pl_
                        mp_mv.append(json_mov)

                inf_char = find_info
                inf_char['movie'] = mp_mv
                
                result = {
                    "pharacters": inf_char
                } 
                        
            
            return JSONResponse(result, status=200)

        if len(data['movie_pharacters']) > 0:
            val = 0
            data_ph = {
                "name": str(data['name'])
            }
            #print(data)
            find_pharacter = Pharacter.objects.filter(name__contains=str(data['name'])).values()
            if len(find_pharacter)>0:
                return JSONResponse(['character is already registered'], status=400)
            result={}
            serializer = PharacterSerializers(data=data_ph)
            if serializer.is_valid():
                serializer.save()
                ph_id = serializer.data['pk']
                mp_mv = []
                for item in range(len(data['movie_pharacters'])):                    
                    data_mp = {
                        "pharacters_id": ph_id,
                        "movie_id": data['movie_pharacters'][item]
                    }
                    
                    serializer_mp = MoviePharacterSerializers(data=data_mp)
                    if serializer_mp.is_valid():
                        serializer_mp.save()
                        #mp.append(serializer_mp.data)
                        mv_ = Movie.objects.filter(id=data['movie_pharacters'][item]).values()
                        pl_ = Planet.objects.filter(movie_planet_id=data['movie_pharacters'][item]).values()
                        json_mov = mv_[0]
                        json_mov['planet'] = pl_
                    else:
                        return JSONResponse(serializer_mp.errors, status=400) 
                    
                    mp_mv.append(json_mov)
                    
                inf_char = serializer.data   
                inf_char['movie'] = mp_mv 
                result= {
                    "pharacters": inf_char
                }    
                return JSONResponse(result, status=201)
                                
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def pharacter_detail(request, pk):
    """
    Retrieve, update or delete a pharacter.
    """
    try:
        pharacter = Pharacter.objects.get(pk=pk)
    except pharacter.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PharacterSerializers(pharacter)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PharacterSerializers(pharacter, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pharacter.delete()
        return HttpResponse(status=204)