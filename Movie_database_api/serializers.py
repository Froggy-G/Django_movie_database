from rest_framework import serializers
from .models import Movie, Rating


class MovieListSerializer(serializers.ModelSerializer):
    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()
    rating_count = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = ("id", "title", "rating_user", "middle_star", "rating_count")


class MovieDetailSerializer(serializers.ModelSerializer):
    directors = serializers.SlugRelatedField(
        slug_field="name", read_only="True", many="True"
    )
    actors = serializers.SlugRelatedField(
        slug_field="name", read_only="True", many="True"
    )
    genre = serializers.SlugRelatedField(
        slug_field="name", read_only="True", many="True"
    )

    class Meta:
        model = Movie
        fields = "__all__"


class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("star", "movie")

    def create(self, validated_data):
        rating, _ = Rating.objects.update_or_create(
            user_id=validated_data.get("user_id", None),
            movie=validated_data.get("movie", None),
            defaults={"star": validated_data.get("star")},
        )
        return rating
