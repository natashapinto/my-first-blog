from django.shortcuts import render
from .models import Post


# Create your views here.
def post_list(request):
	return render(request, 'blog/post_list.html')

	""" code for submit button

	in post_list.html:
		if sum of "No. of Cells"= 50
		continue 
		elif:
			print "Error- A minimum of 50 cells need to be checked"

