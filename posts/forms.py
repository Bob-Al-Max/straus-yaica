from django import forms
from posts.models import Posts

class PostCreateForm(forms.ModelForm):

    title = forms.CharField()
    
    
    class Meta:
        model = Posts
        fields = ['title', 'content', 'image']



class ImageCreateForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ('title', 'content', 'image')


    def clean_image(self):
        image = self.cleaned_data['image']
        
        return image    
        

       


