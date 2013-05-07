from pyramid.scaffolds import PyramidTemplate


class Jinja2AlchemyProjectTemplate(PyramidTemplate):
    """
    Project template for jinja2 and sqlalchemy. This is only compatible with 1.3
    """
    _template_dir = 'jinja2_alchemy'
    summary = 'Jinja2 sqlalchemy project template'
