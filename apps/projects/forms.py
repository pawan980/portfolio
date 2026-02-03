from django import forms
from .models import Project


class ProjectAdminForm(forms.ModelForm):
    """Custom admin form for Project with multi-select categories."""
    
    categories = forms.MultipleChoiceField(
        choices=[c for c in Project.CATEGORY_CHOICES if c[0] != 'all_projects'],
        widget=forms.CheckboxSelectMultiple,
        required=False,
        help_text="Select one or more categories for this project"
    )
    
    class Meta:
        model = Project
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pre-populate selected categories
        if self.instance and self.instance.pk:
            selected = self.instance.get_categories_list()
            self.fields['categories'].initial = selected
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        # Convert selected categories back to comma-separated string
        selected_categories = self.cleaned_data.get('categories', [])
        instance.categories = ','.join(selected_categories)
        if commit:
            instance.save()
        return instance
