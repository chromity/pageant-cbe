from django.urls import path

from . import views

app_name = 'candidates'
urlpatterns = [
    path('', views.index, name='index'),
    path('pageant_proper_overview/', views.pageant_proper_overview, name='pageant_proper_overview'),
    path('pageant_night_overview/', views.pageant_night_overview, name='pageant_night_overview'),
    path('top_candidates/', views.top_candidates, name='top_candidates'),
    path('pageant_result_overview/', views.pageant_result_overview, name='pageant_result_overview'),
    path('pre_pageant/list', views.pre_pageant_list, name='pre_pageant_list'),
    path('pre_pageant/<int:pk>/', views.pre_pageant_detail, name='pre_pageant_detail'),
    path('pre_pageant/<int:pk>/edit/', views.pre_pageant_edit, name='pre_pageant_edit'),
    path('pre_pageant/add', views.pre_pageant_add, name='pre_pageant_add'),
    path('pre_pageant/', views.pre_pageant_overview, name='pre_pageant_overview'),

    path('old_street_fashion_attire/list', views.old_street_fashion_attire_list, name='old_street_fashion_attire_list'),
    path('old_street_fashion_attire/<int:pk>/', views.old_street_fashion_attire_detail,
         name='old_street_fashion_attire_detail'),
    path('old_street_fashion_attire/<int:pk>/edit/', views.old_street_fashion_attire_edit,
         name='old_street_fashion_attire_edit'),
    path('old_street_fashion_attire/add', views.old_street_fashion_attire_add, name='old_street_fashion_attire_add'),
    path('old_street_fashion_attire/', views.old_street_fashion_attire_overview,
         name='old_street_fashion_attire_overview'),
    path('old_street_fashion_attire/add_all', views.old_street_fashion_attire_add_all, name='old_street_fashion_add_all'),
    path('old_street_fashion_attire_add_all_logic', views.old_street_fashion_attire_add_all_logic,
         name='old_street_fashion_add_all_logic'),

    path('formal_attire/list', views.formal_attire_list, name='formal_attire_list'),
    path('formal_attire/<int:pk>/', views.formal_attire_detail, name='formal_attire_detail'),
    path('formal_attire/<int:pk>/edit/', views.formal_attire_edit, name='formal_attire_edit'),
    path('formal_attire/add', views.formal_attire_add, name='formal_attire_add'),
    path('formal_attire/', views.formal_attire_overview, name='formal_attire_overview'),
    path('formal_attire/add_all', views.formal_attire_add_all, name='formal_attire_add_all'),
    path('formal_attire/add_all_logic', views.formal_attire_add_all_logic, name='formal_attire_add_all_logic'),

    path('uniform_attire/list', views.uniform_attire_list, name='uniform_attire_list'),
    path('uniform_attire/<int:pk>/', views.uniform_attire_detail, name='uniform_attire_detail'),
    path('uniform_attire/<int:pk>/edit/', views.uniform_attire_edit, name='uniform_attire_edit'),
    path('uniform_attire/add', views.uniform_attire_add, name='uniform_attire_add'),
    path('uniform_attire/', views.uniform_attire_overview, name='uniform_attire_overview'),
    path('uniform_attire/add_all', views.uniform_attire_add_all, name='uniform_attire_add_all'),
    path('uniform_attire/add_all_logic', views.uniform_attire_add_all_logic, name='uniform_attire_add_all_logic'),

    path('question_and_answer/list', views.question_and_answer_list, name='question_and_answer_list'),
    path('question_and_answer/<int:pk>/', views.question_and_answer_detail, name='question_and_answer_detail'),
    path('question_and_answer/<int:pk>/edit/', views.question_and_answer_edit, name='question_and_answer_edit'),
    path('question_and_answer/add', views.question_and_answer_add, name='question_and_answer_add'),
    path('question_and_answer/', views.question_and_answer_overview, name='question_and_answer_overview'),
    path('question_and_answer/add_all', views.question_and_answer_add_all, name='question_and_answer_add_all'),
    path('question_and_answer/add_all_logic', views.question_and_answer_add_all_logic,
         name='question_and_answer_add_all_logic')
]
