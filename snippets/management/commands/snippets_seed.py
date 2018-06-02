from django.core.management.base import BaseCommand
from django.utils.six import BytesIO

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class Command(BaseCommand):
    help = 'seed snippets'

    def handle(self, *args, **options):
        Snippet.objects.all().delete()
        print(repr(SnippetSerializer()))

        snippet = Snippet(code='foo = "bar"\n')
        snippet.save()

        snippet = Snippet(code='print "hello, world"\n')
        snippet.save()

        serializer = SnippetSerializer(snippet)
        print('serializer.data')
        print(serializer.data)

        content = JSONRenderer().render(serializer.data)
        print('content')
        print(content)

        stream = BytesIO(content)
        print('stream')
        print(stream)
        data = JSONParser().parse(stream)
        print('data')
        print(data)

        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            print('serializer.validated_data')
            print(serializer.validated_data)
            serializer.save()

        serializers = SnippetSerializer(Snippet.objects.all(), many=True)
        print('serializers.data')
        print(serializers.data)
