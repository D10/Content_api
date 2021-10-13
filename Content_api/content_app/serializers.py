from collections import OrderedDict

from rest_framework import serializers

from .models import Page, Content, VideoContent, AudioContent, TextContent


# Сериализатор для списка контент-страниц
class PageListSerializer(serializers.ModelSerializer):

    # Достаем ссылку на каждую страницу
    def get_link(self, obj):
        return 'http://127.0.0.1:8000' + obj.get_absolute_url()

    link = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ('pk', 'link')


# Создаем классы-сериализаторы для каждого типа контента отдельно, чтобы после объединить их
# В общем классе сериализаторе, который уже подключим в сериализатор отдельной страницы
class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoContent
        fields = ('video_link', 'sub_link')


class AudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = AudioContent
        fields = ('bpm',)


class TextSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextContent
        fields = ('text',)


class ContentSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        result = super(ContentSerializer, self).to_representation(instance)
        return OrderedDict([key, result[key]] for key in result if result[key] is not None)

    video_content = VideoSerializer()
    audio_content = AudioSerializer()
    text_content = TextSerializer()

    class Meta:
        model = Content
        fields = ('id', 'counter', 'position', 'audio_content', 'video_content', 'text_content')


class PageDetailSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        result = super(PageDetailSerializer, self).to_representation(instance)
        print('==============', result['content'])
        result['content'] = sorted(result['content'], key=lambda x: x['position'])
        return result

    content = ContentSerializer(source='content.all', many=True)

    class Meta:
        model = Page
        fields = ('pk', 'title', 'content')
