from django.utils.translation import ugettext_lazy as _

import horizon


class Midonet(horizon.Dashboard):
    name = _("Midonet")
    slug = "midonet"
    panels = ('monitor',)  # Add your panels here.
    default_panel = 'monitor'  # Specify the slug of the dashboard's default panel.


horizon.register(Midonet)
