from django.utils.translation import ugettext_lazy as _

import horizon

class Midonetgroup(horizon.PanelGroup):
    slug = "midonetgroup"
    name = _("Midonet group")
    panels = ('overview',)


class Midonet(horizon.Dashboard):
    name = _("Midonet")
    slug = "midonet"
    panels = (Midonetgroup,)  # Add your panels here.
    default_panel = 'overview'  # Specify the slug of the dashboard's default panel.

horizon.register(Midonet)
