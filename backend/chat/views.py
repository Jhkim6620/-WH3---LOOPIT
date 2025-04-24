from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from chat.models import ChatRoom
from products.models import Product

class ChatRoomCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        product_id = request.data.get('product_id')

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': '상품이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)

        seller = product.owner
        buyer = user

        if buyer == seller:
            return Response({'error': '본인과는 채팅할 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        room, created = ChatRoom.objects.get_or_create(
            buyer=buyer,
            seller=seller,
            product=product
        )

        return Response({
            'room_id': room.id,
            'product_title': product.title,
            'seller_id': seller.id,
            'buyer_id': buyer.id
        }, status=status.HTTP_200_OK)
