from rest_framework import serializers
from stories.models import Recipe, Category, Tag, Story, Subscriber
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


User = get_user_model()

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'title',
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'image',
        )


class RecipeSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'image',
            'short_description',
            'long_description',
            'category',
            'author',
        )
    
    def validate(self, data):
        request = self.context.get('request')
        data['author'] = request.user
        return super().validate(data)


class RecipeReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'image',
            'short_description',
            'long_description',
            'category',
            'author',
            'tags',
        )


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    date_joined = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'confirm_password',
            'date_joined',

        )
    
    def validate(self, cleaned_data):
        # cleaned_data = super().validate()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise serializers.ValidationError(
                "Password and Confirm password does not match"
            )
        return cleaned_data

    def validate_password(self, password):
        # password = self.cleaned_data.get('password')
        # print(self.instance)
        try:
            validate_password(password, self.instance)
        except serializers.ValidationError as error:
            self.add_error('password', error)
        return password

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        confirm_password = validated_data.pop('confirm_password', None)
        instance = self.Meta.model(**validated_data)
        # User(first_name=first_name, last_name)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = (
            'id',
            'tags',
            'title',
            'image',
            'long_description',
            'category',
            'author',
            'created_at',
            'updated_at'
        )

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = (
            'email',
        )