from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import ProductCategory, Product, BillItem, BillSequence, Bill
from .forms import CategoryForm, ProductForm, BillItemForm, BillForm
from django.db.models import Sum
# Create your views here.


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "you have been logged in")
            return redirect('index')
        else:
            messages.success(
                request, 'Your username or password is incorrect...')
            return render(request, 'login.html')
    else:
        if request.user.is_authenticated:
            overall_bill_count = Bill.objects.all().count()
            total_amount_sum = Bill.objects.aggregate(
                total_amount_sum=Sum('total_amount'))['total_amount_sum']
            print(total_amount_sum)
            if total_amount_sum is not None:
                pass
            else:
                total_amount_sum = 0.00
            return render(request, 'dashboard.html', {'overall_bill_count': overall_bill_count, 'total_amount_sum': total_amount_sum})
        else:
            return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "you have been logout")
    return redirect('index')

# Bill


def view_bill(request):
    records = Bill.objects.all()
    return render(request, 'bill/bill_tree_view.html', {'records': records})


def new_bill(request):
    global product_list
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BillForm(request.POST)
            if form.is_valid():
                if 'products_submit' in request.POST:
                    products_queryset = form.cleaned_data['product_ids']
                    # Creating a list of dictionaries for each selected product
                    if products_queryset:
                        product_list = []
                        for count, product in enumerate(products_queryset):
                            product_dict = {
                                'id': product.id,
                                'si_no': count+1,  # Replace with the actual field name in your Product model
                                'name': product,
                                'rate': product.rate,
                                'quantity': 0,  # Assuming quantity is a field in your Book model
                                'total': 0,
                                # Add other fields as needed
                            }
                            product_list.append(product_dict)
                        return render(request, 'bill/bill_create_form.html', {'form': form, 'product_list': product_list})
                    else:
                        messages.success(request, "No product is selected")
                        return redirect("newbill")
                # data = Bill(created_by=request.user)
                # data.save()
                elif 'bill_submit' in request.POST:
                    total_amount = request.POST['totalAmount']
                    bill_seq = BillSequence.objects.get(id=1)
                    prefix = bill_seq.prefix
                    digi = bill_seq.digi
                    after = bill_seq.after

                    # Format the other_integer with leading zeros
                    formatted_integer = f"{after + 1:03d}"

                    # Concatenate the base_value and the formatted_integer
                    sequence = f"{prefix}{formatted_integer}"
                    bill_seq.after = after+1
                    bill_seq.save()

                    bill = Bill(
                        name=sequence, total_amount=total_amount, created_by=request.user)
                    bill.save()
                    for product_item in product_list:
                        product_id = Product.objects.get(id=product_item['id'])
                        get_product_name = "product_name_" + \
                            str(product_item['id'])
                        get_rate = "rate_"+str(product_item['id'])
                        get_qty = "qty_"+str(product_item['id'])
                        get_total = "total_"+str(product_item['id'])

                        product_name = request.POST[get_product_name]
                        rate = request.POST[get_rate]
                        qty = request.POST[get_qty]
                        total = request.POST[get_total]

                        bill_item = BillItem(bill_id=bill, product_id=product_id,
                                             product_name=product_name, rate=rate, qty=qty, total=total)
                        bill_item.save()

                    messages.success(request, "Product created Successfully")
                    return redirect("viewbill")
            else:
                messages.success(request, "Form is Invalid")
                return redirect("viewbill")
        else:
            form = BillForm()
            return render(request, 'bill/bill_create_form.html', {'form': form})
    else:
        return redirect('index')


def view_billform(request, pk):
    if request.user.is_authenticated:
        bill_record = Bill.objects.get(id=pk)
        form = BillForm(request.POST or None, instance=bill_record)
        billitem_records = BillItem.objects.filter(bill_id=pk)
        sno = []
        for i in range(0, len(billitem_records)):
            sno.append(i+1)
        billitem_records = zip(billitem_records, sno)
        return render(request, "bill/view_billform.html", {'bill_record': bill_record, 'billitem_records': billitem_records})
    else:
        messages.success('you not logged in')
        return redirect('index')


# Product
def view_product(request):
    records = Product.objects.all()
    return render(request, 'product/product_tree_view.html', {'records': records})


def new_product(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ProductForm(request.POST)
            if form.is_valid():
                product_name = form.cleaned_data['product_name']
                category_id = form.cleaned_data['category_id']
                rate = form.cleaned_data['rate']
                data = Product(product_name=product_name,
                               category_id=category_id, rate=rate, created_by=request.user)
                data.save()
                messages.success(request, "Product created Successfully")
                return redirect("viewproduct")
            else:
                messages.success(request, "Form is Invalid")
                return redirect("viewproduct")
        else:
            form = ProductForm()
            return render(request, 'product/product_create_form.html', {'form': form})
    else:
        return redirect('index')


def edit_product(request, pk):
    if request.user.is_authenticated:
        current_record = Product.objects.get(id=pk)
        form = ProductForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated Successfully")
            return redirect('viewproduct')
        return render(request, "product/product_update.html", {'record': current_record, 'form': form})
    else:
        messages.success('you not logged in')
        return redirect('index')


def delete_product(request, pk):
    if request.user.is_authenticated:
        view_record = Product.objects.get(id=pk)
        view_record.delete()
        return redirect('viewproduct')
    else:
        messages.success('you not logged in')
        return redirect('index')

# Product Category


def view_productcat(request):
    records = ProductCategory.objects.all()
    return render(request, 'category/productcat_tree_view.html', {'records': records})


def new_productcat(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CategoryForm(request.POST)
            if form.is_valid():
                name = request.POST['name']
                data = ProductCategory(name=name, created_by=request.user)
                data.save()
                messages.success(request, "Category created Successfully")
                return redirect("viewproductcat")
            else:
                messages.success(request, "Form is Invalid")
                return redirect("viewproductcat")
        else:
            form = CategoryForm()
            records = ProductCategory.objects.all()
            return render(request, 'category/productcat_create.html', {'form': form, 'records': records})


def edit_productcat(request, pk):
    if request.user.is_authenticated:
        current_record = ProductCategory.objects.get(id=pk)
        form = CategoryForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated Successfully")
            return redirect('viewproductcat')
        return render(request, "category/productcat_edit.html", {'record': current_record, 'form': form})
    else:
        messages.success('you not logged in')
        return redirect('index')


def delete_cat(request, pk):
    if request.user.is_authenticated:
        view_record = ProductCategory.objects.get(id=pk)
        view_record.delete()
        return redirect('viewproductcat')
    else:
        messages.success('you not logged in')
        return redirect('index')
