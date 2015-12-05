from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def navactive(request, url):
    if url in request.path:
        return "active"
    return ""


@register.simple_tag
def navbar_button(request, *inp_buttons):

	css = 'btn btn-default btn-md navbar-btn'
	buts = [i.split() for i in inp_buttons]

	for b in buts:
		b[0] = reverse(b[0])
		if b[0] in request.path:
			b.append(css+' active')
		else:
			b.append(css)
	
	button = "<li>\n"\
			"<a href='{0}' " \
			"class = '{3}' role = 'button'> \n" \
			"<span class = 'glyphicon glyphicon-{2}'> " \
			"</span> {1} \n</a>\n</li>"


	buttons = [button.format(*b) for b in buts]
	return '\n'.join(buttons)