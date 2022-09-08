from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
  bag = request.session.get('bag', {})
  if not bag:
    messages.error(request, "There's nothing in your bag at the moment")
    return redirect(reverse('products'))
  
  order_form = OrderForm()
  template = 'checkout/checkout.html'
  context = {
    'order_form': order_form,
    'stripe_public_key': 'pk_test_51LfqaZEL1As7JUm6Nu8M0qk9aNBVxiumYBHnP10NBfDjhyhc52TbTTs4eF7tLqOIM1VDJrDgPvLYQKfcNMEWdNvG00NjwNbhdt',
    'client_secret': 'test client secret',
  }
  
  return render(request, template, context)