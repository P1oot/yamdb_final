from django.shortcuts import get_object_or_404
from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Category
        lookup_fields = 'slug'

    def validate(self, data):
        if data == {}:
            raise serializers.ValidationError(
                'Данные не корректны')
        return data


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Genre
        lookup_field = 'slug'


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all(),
        many=False
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        read_only=False,
        queryset=Genre.objects.all(),
        many=True
    )
    rating = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'name', 'year', 'description', 'category', 'genre',
                  'rating')
        model = Title

    def get_rating(self, obj):
        title = Title.objects.get(id=obj.id)
        scors = []
        for review in title.reviews.all():
            scors = scors + [review.score]
        if not len(scors) == 0:
            return round(sum(scors) / len(scors))
        return None


class GetTitleSerializer(TitleSerializer):
    category = CategorySerializer(
        read_only=True,
        many=False
    )
    genre = GenreSerializer(many=True)


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'text', 'score', 'author', 'pub_date')
        model = Review

    def validate(self, data):
        id = (self.context['request'].parser_context['kwargs']['title_id'])
        title = get_object_or_404(Title, id=id)
        if (self.context['request'].method == 'POST'
            and Review.objects.filter(author=self.context['request'].user,
                                      title=title).exists()):
            raise serializers.ValidationError(
                'Можно оставить только один отзыв на произведение')
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment
