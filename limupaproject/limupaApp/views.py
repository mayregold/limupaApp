from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from user.decorators import seller_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy



# Create your views here.

def custom_404(request, exception):
    return render(request, 'limupaApp/404.html', status=404)

def base(request):
    profile = request.user.profile  # Ensure this line correctly retrieves the profile
    context = {
        'user_profile': profile,
    }
    return render(request, 'limupaApp/base.html')


@method_decorator(seller_required, name='dispatch')
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'limupaApp/update_product.html'

  
    def get_success_url(self):
        return reverse_lazy('product_details', kwargs={'pk': self.object.pk})


def index(request):
    return render(request, 'limupaApp/index.html')

def about(request):
    return render(request, 'limupaApp/about-us.html')

@method_decorator(seller_required, name='dispatch')
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'limupaApp/add_product.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the product's user to the current user
        return super().form_valid(form)


def blog2column(request):
    return render(request, 'limupaApp/blog-2-column.html')

def blog3column(request):
    return render(request, 'limupaApp/blog-3-column.html')

def blogaudioformat(request):
    return render(request, 'limupaApp/blog-audio-format.html')

def blogdetailsleftsidebar(request):
    return render(request, 'limupaApp/blog-details-left-sidebar.html')

def blogdetailsrightsidebar(request):
    return render(request, 'limupaApp/blog-details-right-sidebar.html')

def blogdetails(request):
    return render(request, 'limupaApp/blog-details.html')

def bloggalleryformat(request):
    return render(request, 'limupaApp/blog-gallery-format.html')

def blogleftsidebar(request):
    return render(request, 'limupaApp/blog-left-sidebar.html')

def bloglistleftsidebar(request):
    return render(request, 'limupaApp/blog-list-left-sidebar.html')

def bloglistrightsidebar(request):
    return render(request, 'limupaApp/blog-list-right-sidebar.html')

def bloglist(request):
    return render(request, 'limupaApp/blog-list.html')

def blogrightsidebar(request):
    return render(request, 'limupaApp/blog-right-sidebar.html')

def blogvideoformat(request):
    return render(request, 'limupaApp/blog-video-format.html')

def cart(request):
    return render(request, 'limupaApp/cart.html')

def checkout(request):
    return render(request, 'limupaApp/checkout.html')

def compare(request):
    return render(request, 'limupaApp/compare.html')

def contact(request):
    return render(request, 'limupaApp/contact.html')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'limupaApp/delete.html'
    success_url = reverse_lazy('product_list')

def faq(request):
    return render(request, 'limupaApp/faq.html')

def index2(request):
    return render(request, 'limupaApp/index-2.html')

def index3(request):
    return render(request, 'limupaApp/index-3.html')

def index4(request):
    return render(request, 'limupaApp/index-4.html')

def loginregister(request):
    return render(request, 'limupaApp/login-register.html')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'limupaApp/product_details.html'
    context_object_name = 'product'

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'limupaApp/product_list.html' 
    context_object_name = 'products'  


def shop3column(request):
    return render(request, 'limupaApp/shop-3-column.html')

def shop4column(request):
    return render(request, 'limupaApp/shop-4-column.html')

def shopleftsidebar(request):
    return render(request, 'limupaApp/shop-left-sidebar.html')

def shoplistleftsidebar(request):
    return render(request, 'limupaApp/shop-list-left-sidebar.html')

def shoplistrightsidebar(request):
    return render(request, 'limupaApp/shop-list-right-sidebar.html')

def shoplist(request):
    return render(request, 'limupaApp/shop-list.html')

def shoprightsidebar(request):
    return render(request, 'limupaApp/shop-right-sidebar.html')

def shoppingcart(request):
    return render(request, 'limupaApp/shopping-cart.html')

def singleproductaffiliate(request):
    return render(request, 'limupaApp/single-product-affiliate.html')

def singleproductcarousel(request):
    return render(request, 'limupaApp/single-product-carousel.html')

def singleproductgalleryleft(request):
    return render(request, 'limupaApp/single-product-gallery-left.html')

def singleproductgalleryright(request):
    return render(request, 'limupaApp/single-product-gallery-right.html')

def singleproductgroup(request):
    return render(request, 'limupaApp/single-product-group.html')

def singleproductnormal(request):
    return render(request, 'limupaApp/single-product-normal.html')

def singleproductsale(request):
    return render(request, 'limupaApp/single-product-sale.html')

def singleproducttabstyletop(request):
    return render(request, 'limupaApp/single-product-tab-style-top.html')

def singleproducttabstyleleft(request):
    return render(request, 'limupaApp/single-product-tab-style-left.html')

def singleproducttabstyleright(request):
    return render(request, 'limupaApp/single-product-tab-style-right.html')

def singleproduct(request):
    return render(request, 'limupaApp/single-product.html')

@method_decorator(seller_required, name='dispatch')
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'limupaApp/update_product.html'


    def get_success_url(self):
        return reverse_lazy('product_details', kwargs={'pk': self.object.pk})


def wishlist(request):
    return render(request, 'limupaApp/wishlist.html')




