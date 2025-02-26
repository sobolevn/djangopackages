from django.views.generic.dates import ArchiveIndexView

from package.models import Package
from package.views import (
                            add_example,
                            add_package,
                            ajax_package_list,
                            edit_package,
                            edit_example,
                            delete_example,
                            confirm_delete_example,
                            update_package,
                            usage,
                            package_list,
                            package_detail,
                            post_data,
                            edit_documentation,
                            github_webhook
                            )
from django.urls import path, re_path

urlpatterns = [

    path('', view=package_list,
        name="packages",
    ),

    path('latest/', view=ArchiveIndexView.as_view(
                        queryset=Package.objects.filter().select_related(),
                        paginate_by=50,
                        date_field="created"
        ),
        name="latest_packages",
    ),
    path('add/', view=add_package,
        name="add_package",
    ),

    path('<slug:slug>/edit/', view=edit_package,
        name="edit_package",
    ),

    path('<slug:slug>/fetch-data/', view=update_package,
        name="fetch_package_data",
    ),

    path('<slug:slug>/post-data/', view=post_data,
        name="post_package_data",
    ),

    path('<slug:slug>/example/add/', view=add_example,
        name="add_example",
    ),

    path('<slug:slug>/example/<int:id>/edit/', view=edit_example,
        name="edit_example",
    ),

    path('<slug:slug>/example/<int:id>/delete/', view=delete_example,
        name="delete_example",
    ),

    path('<slug:slug>/example/<int:id>/confirm_delete/', view=confirm_delete_example,
        name="confirm_delete_example",
    ),

    path('p/<slug:slug>/', view=package_detail,
        name="package",
    ),

    path('ajax_package_list/', view=ajax_package_list,
        name="ajax_package_list",
    ),

    re_path(
        r"^usage/(?P<slug>[-\w]+)/(?P<action>add|remove)/$", view=usage,
        name="usage",
    ),

    path('<slug:slug>/document/', view=edit_documentation,
        name="edit_documentation",
    ),
    path('github-webhook/', view=github_webhook,
        name="github_webhook"
    ),
]
