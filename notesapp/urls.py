from django.urls import path
from . import views


urlpatterns = [
    path('notes/', views.notes, name='notes'),
    path('notes/<slug:slug>', views.note_detail, name='note-detail'),
    path('notes-search/', views.search_notes, name='notes-search'),
    path('categories/', views.categories, name='categories'),
    path('categories/add-category/', views.add_category, name='add-category'),
    path('categories/delete/<int:id>/', views.delete_category, name='delete-category'),
]



# endpoints:
# GET_ALL_NOTES_and_CREATE_NEW_NOTE = "127.0.0.1:8008/notes/"
# GET_SPECIFIC_NOTE = "127.0.0.1:8008/notes/note-slug"
# SEARCH_NOTES = "127.0.0.1:8008/notes-search/?search=meeting"
# GET_CATEGORIES = "cateories/category-id"
# ADD_CATEGORY = "categories/add-category"