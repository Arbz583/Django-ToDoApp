from rest_framework import serializers
from ...models import Task
from django.contrib.auth.models import User



class TaskSerializer(serializers.ModelSerializer):
    created_date = serializers.DateField(format=None, input_formats=None)
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url_api = serializers.SerializerMethodField(method_name="get_abs_url")
    user=serializers.SlugRelatedField(many=False, slug_field="username", read_only=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "user",
            "title",
            "complete",
            "snippet",
            "relative_url",
            "absolute_url_api",
            "updated_date",
            "created_date",
        ]
        read_only_fields = [
            "user",

        ]

    def get_abs_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snippet", None)
            rep.pop("relative_url", None)
            rep.pop("absolute_url_api", None)
        else:
            rep.pop("title", None)
        return rep

    def create(self, validated_data):

        validated_data["user"] = self.context.get("request").user
        return super().create(validated_data)
