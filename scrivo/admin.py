from django.contrib import admin
from markitup.widgets import AdminMarkItUpWidget
from scrivo.models import Post

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('categories',)
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == "content":
            kwargs['widget'] = AdminMarkItUpWidget()
        return super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)
    

admin.site.register(Post, PostAdmin)