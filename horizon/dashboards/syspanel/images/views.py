# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import logging

from django.utils.translation import ugettext_lazy as _

from horizon import api
from horizon import exceptions
from horizon import tables
from horizon.dashboards.nova.images_and_snapshots.images import views
from .tables import AdminImagesTable
from .forms import AdminUpdateImageForm


LOG = logging.getLogger(__name__)


class IndexView(tables.DataTableView):
    table_class = AdminImagesTable
    template_name = 'syspanel/images/index.html'

    def has_more_data(self, table):
        return self._more

    def get_data(self):
        images = []
        marker = self.request.GET.get(AdminImagesTable._meta.pagination_param,
                                      None)
        try:
            images, self._more = api.image_list_detailed(self.request,
                                                         marker=marker)
        except:
            self._more = False
            msg = _('Unable to retrieve image list.')
            exceptions.handle(self.request, msg)
        return images


class UpdateView(views.UpdateView):
    template_name = 'syspanel/images/update.html'
    form_class = AdminUpdateImageForm


class DetailView(views.DetailView):
    """ Admin placeholder for image detail view. """
    pass
