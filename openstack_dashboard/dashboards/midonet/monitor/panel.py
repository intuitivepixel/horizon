from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.midonet import dashboard


class Monitor(horizon.Panel):
    name = _("Monitor")
    slug = "monitor"


dashboard.Midonet.register(Monitor)
