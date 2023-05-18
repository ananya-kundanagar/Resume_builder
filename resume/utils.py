from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)

    font_config = FontConfiguration()
    css = CSS('./resume/templates/pdf/test.css')
    
    pdf = HTML(string=html).write_pdf(stylesheets=[css], font_config=font_config)
    if pdf:
        return pdf
    return None