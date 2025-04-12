
from rest_framework.response import Response
from rest_framework.views import APIView
from .puher import pusher_client

# Create your views here.

class MessageAPIView(APIView):
    
    def post(self, request):
        
        print(request.data)
        
        pusher_client.trigger('chat', 'message', {
            'username': request.data['username'],
            'message': request.data['message']
        })
        
        return Response(
            {
                'status': 'success',
                'message': 'Message sent successfully!'
            }
        )
       
    
