from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from stories.models import Recipe
from api.serializers import RecipeReadSerializer, RecipeSerializer, RegisterSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT


@api_view(('GET', 'POST',))
def recipes(request):
    if request.method == 'GET':
        recipe_list = Recipe.objects.all()
        serializer = RecipeReadSerializer(recipe_list, context={ 'request' : request, }, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.user and request.user.is_authenticated and request.method == 'POST':
        recipe_data = request.data
        serializer = RecipeSerializer(data=recipe_data, context={ 'request' : request, },)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,  status=HTTP_201_CREATED)
    else:
        raise PermissionDenied 


@api_view(('POST',))
def registration(request):
    if request.method == 'POST':
        user_data = request.data
        serializer = RegisterSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)



@api_view(('GET', 'PUT', 'PATCH', 'DELETE'))
def recipe_detail(request, recipe_id):
    if request.method == 'GET':
        recipe = get_object_or_404(Recipe, id=recipe_id)
        # recipe = Recipe.objects.filter(pk=recipe_id).first()
        # if not recipe:
        #     return Response({ 'detail': f'Recipe with {recipe_id} id/pk not founded' })
        serializer = RecipeReadSerializer(recipe, context={'request': request})
        return Response(serializer.data, status=HTTP_200_OK)
    if request.method == 'PUT':
        recipe_data = request.data
        recipe = Recipe.objects.get(pk=recipe_id)
        serializer = RecipeSerializer(data=recipe_data, instance=recipe, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)
    if request.method == 'PATCH':
        recipe_data = request.data
        recipe = Recipe.objects.get(pk=recipe_id)
        serializer = RecipeSerializer(data=recipe_data, instance=recipe, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)
    if request.method == 'DELETE':
        recipe = Recipe.objects.get(pk=recipe_id).delete()
        return Response(status=HTTP_204_NO_CONTENT)


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        register_serializer = RegisterSerializer(user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'user_data': register_serializer.data,
            
        })