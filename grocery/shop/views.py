from django.shortcuts import render, redirect
from .models import Product, Sale

def shopkeeper(request):
    if request.method == "POST":
        Product.objects.create(
            name=request.POST["name"],
            price=float(request.POST["price"]),
            stock=int(request.POST["stock"])
        )
        return redirect("shopkeeper")

    return render(request, "shopkeeper.html", {
        "products": Product.objects.all(),
        "sales": Sale.objects.all()
    })


def customer(request):
    products = Product.objects.all()
    total = 0

    if request.method == "POST":
        for p in products:
            qty = int(request.POST.get(str(p.id), 0))
            if qty > 0 and p.stock >= qty:
                Sale.objects.create(product=p, qty=qty)
                p.stock -= qty
                p.save()
                total += p.price * qty

        return render(request, "customer.html", {
            "products": products,
            "total": total,
            "msg": "Order Completed!"
        })

    return render(request, "customer.html", {"products": products})
