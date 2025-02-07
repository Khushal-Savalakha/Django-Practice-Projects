from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogPost

# Create a list of numbers (for demonstration purposes)
numbers_list = list(range(1, 31))  # List of numbers from 1 to 30


def paginate_numbers(request):
    # Default number of items per page
    items_per_page = 3

    # Check if the user has specified a custom number of items per page
    if 'items_per_page' in request.GET:
        items_per_page = int(request.GET.get('items_per_page'))
    
    # Create a Paginator object
    paginator = Paginator(numbers_list, items_per_page)

    # Get the current page number from the request
    page = request.GET.get('page')

    try:
        # Get the Page object for the current page
        numbers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        numbers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        numbers = paginator.page(paginator.num_pages)

    # Pass the paginated numbers and other context to the template
    context = {
        'numbers': numbers,
        'items_per_page': items_per_page,
        'page_count': paginator.num_pages,
    }

    return render(request, 'paginate_numbers.html', context)


# Function-Based View (FBV) for Advanced Pagination
def advanced_pagination(request):
    # Default number of items per page
    items_per_page = 10

    # Allow the user to change the number of items per page via query parameter
    if 'items_per_page' in request.GET:
        try:
            items_per_page = int(request.GET.get('items_per_page'))
            if items_per_page < 1:
                items_per_page = 10  # Fallback to default if invalid
        except ValueError:
            items_per_page = 10  # Fallback to default if invalid

    # Fetch all blog posts from the database
    blog_posts = BlogPost.objects.all()

    # Create a Paginator object
    paginator = Paginator(blog_posts, items_per_page)

    # Get the current page number from the request
    page = request.GET.get('page')

    try:
        # Get the Page object for the current page
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        posts = paginator.page(paginator.num_pages)

    # Calculate a range of page numbers to display (e.g., "1 2 3 ... 10")
    page_range = paginator.get_elided_page_range(number=posts.number, on_each_side=2, on_ends=1)

    # Pass the paginated posts and other context to the template
    context = {
        'posts': posts,
        'items_per_page': items_per_page,
        'page_range': page_range,
    }

    return render(request, 'advanced_pagination.html', context)


# Class-Based View (CBV) for Built-in Pagination
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blogpost_list.html'
    context_object_name = 'posts'
    paginate_by = 10  # Default number of items per page

    def get_paginate_by(self, queryset):
        # Allow the user to change the number of items per page via query parameter
        return self.request.GET.get('items_per_page', self.paginate_by)