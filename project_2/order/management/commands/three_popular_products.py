from django.core.management.base import BaseCommand
from django.db.models import Count
from order.models import CartItem
from store.models import Product

class Command(BaseCommand):
    help = 'ეძებს 3 ყველაზე პოპულარულ პროდუქტს'

    def handle(self, *args, **options):
        popular_products = (
            Product.objects.annotate(user_count=Count('cartitem__cart__user', distinct=True))
            .order_by('-user_count')[:3]
        )
        if popular_products:
            self.stdout.write('ტოპ 3 პროდუქტი:')
            for product in popular_products:
                self.stdout.write(f'{product.name}-{product.user_count} მომხმარებელი')
        else:
            self.stdout.write('ჯერჯერობით არ გვაქვს პოპულარული პროდუქტები')



