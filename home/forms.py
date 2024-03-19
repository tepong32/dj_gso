from django import forms
from .models import Item


# See "Add blog categories - Django blog #12" by Codemy for explanation (around 7min mark)
# Note that only admins can add Category-s. For users, it'll only be a dropdown selector
# categories = Category.objects.all().values_list('name', 'name')
# categories_list = []

# for item in categories:
# 	categories_list.append(item)

class ItemForm(forms.ModelForm):
    title = forms.CharField(max_length=100)		# i think this can be removed since the same field is in the model?
    
    class Meta:
    	model = Item
    	fields = ['date', 'obrNum', 'category', 'sub_category', 'brand', 'supplier', 'price_per_unit', 'qty', 'status', 'returned_date', 'notes']
    	widgets = {
    		# 'tag'
    		# 'category' : forms.Select(choices=categories, attrs={'class': 'form-control'})
    	}

    ### or you can use "exclude" if it fits your usage: ###
    # class Meta:
    #     model = YourModel
    #     exclude = ['field_to_exclude1', 'field_to_exclude2']

