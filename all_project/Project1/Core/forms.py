from django import forms
from Core.models import *


class StudentForm(forms.ModelForm):
   class Meta:
       model=Student
    #    fields=['name','age','mobileNo']
       fields='__all__'
   def __init__(self,*args,**kwargs):
      super().__init__(*args,**kwargs)
      for field in self.fields.values():
          field.widget.attrs['placeholder']='Enter '+field.label + '*'
          field.widget.attrs['class']='form-control' 




