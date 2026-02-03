"""
Custom template tags for markdown rendering.
"""

from django import template
from django.utils.safestring import mark_safe
import markdown as md

register = template.Library()


@register.filter(name='markdown')
def markdown_format(text):
    """
    Convert markdown text to HTML.
    Supports: bold, italic, code, links, lists, headings.
    """
    if not text:
        return ''
    
    # Configure markdown with extensions
    html = md.markdown(
        text,
        extensions=[
            'extra',          # Tables, fenced code blocks, etc.
            'codehilite',     # Syntax highlighting
            'nl2br',          # Newline to <br>
            'sane_lists',     # Better list handling
        ]
    )
    
    return mark_safe(html)
