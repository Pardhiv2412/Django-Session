
from django.urls import path,include
from . import views
urlpatterns = [
    path(route='login',view=views.Login,name='login'),
    path(route='logincheck',view=views.Logincheck,name='logincheck'),
    path(route='admin',view=views.Admin,name='admin'),
    path(route ="adddoc",view = views.AddDoctor,name = "adddoc"),
    path(route ="deletedoc/<int:doc_id>/",view = views.DelDoctor,name = "deletedoc"),
    path(route ="alldoc",view = views.AllDoctor,name = "alldoc"),
    path(route ="addpat",view = views.AddPatient,name = "addpat"),
    path(route ="deletepat/<int:pat_id>/",view = views.DelPatient,name = "deletepat"),
    path(route ="allpat",view = views.AllPatient,name = "allpat"),
    path(route ="allpatdoc",view = views.AllPatientdoc,name = "allpatdoc"),
    path(route ="savedoc",view = views.savedoc,name = "savedoc"),
    path(route ="savepat",view = views.savepat,name = "savepat"),
    path(route ="singlepatdoc/<int:pat_id>/",view = views.singlepatdoc,name = "singlepatdoc"),
    path(route ="singlepat/<int:pat_id>/",view = views.singlepat,name = "singlepat"),
    path(route ="singledoc/<int:doc_id>/",view = views.singledoc,name = "singledoc"),
    path(route ='updatepat/<int:pat_id>/',view = views.updatepat,name = "updatepat"),
    path(route ='updatedoc/<int:doc_id>/',view = views.updatedoc,name = "updatedoc"),
]