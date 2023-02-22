from viktor import ViktorController
from viktor.parametrization import ViktorParametrization

from pathlib import Path

from viktor.views import WebResult
from viktor.views import WebView



class Parametrization(ViktorParametrization):
    pass


class Controller(ViktorController):
    viktor_enforce_field_constraints = True  # prevents a warning and can be ignored for the purpose of this guide

    label = "ABM Kampala"              # label to be shown in the interface
    @WebView('ABM Kampala', duration_guess=1)
    def get_web_view(self, params, **kwargs):
        static_html_path = Path(__file__).parent / 'boda-boda-charging-new.html'
        return WebResult.from_path(static_html_path)