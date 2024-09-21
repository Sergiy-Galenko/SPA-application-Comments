import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Comment
from .serializers import CommentSerializer

class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("comments_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("comments_group", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        username = data['username']
        text = data['text']
        email = data['email']

        # Збереження нового коментаря
        comment = Comment.objects.create(username=username, text=text, email=email)

        # Серіалізація коментаря
        comment_data = CommentSerializer(comment).data

        # Відправка коментаря всім підключеним клієнтам
        await self.channel_layer.group_send(
            "comments_group",
            {
                'type': 'comment_message',
                'comment': comment_data
            }
        )

    async def comment_message(self, event):
        comment = event['comment']

        # Відправка коментаря назад через WebSocket
        await self.send(text_data=json.dumps({
            'comment': comment
        }))
