from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # 모델로부터 정보를 가져와서 필요한 필드를 만들어준다.

'''
class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField() # html form에서는 char/textfield 구분하지 않음
    photo = forms.FileField()
'''

# model은 db / forms는 html.
# forms는 html태그를 만들고 입력 받은 데이터 유효성 검사도 해준다.


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'message']

# =

# class CommentForm2(forms.Form):
#     author = forms.CharField()
#     message = form.CharField(widget=forms.Textarea)

#     def save(self, commit=True):
#         comment = Comment(**self.cleaned_data)
#         if commit:
#             comment.save()
#         return comment