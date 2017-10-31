"""
Default settings for the ``mezzanine_pagedown`` app.

Each of these can be overridden in your project's settings module, 
just like regular Django settings. 
The ``editable`` argument for each controls whether 
the setting is editable via Django's admin.
Thought should be given to how a setting is actually used before
making it editable, as it may be inappropriate - for example settings
that are only read during startup shouldn't be editable, since changing
them would require an application reload.
"""
from mezzanine.conf import register_setting

register_setting(
    name="PAGEDOWN_SERVER_SIDE_PREVIEW",
    description="Render previews on the server using the same "
                "converter that generates the actual pages.",
    editable=False,
    default=False,
)

register_setting(
    name="PAGEDOWN_MARKDOWN_EXTENSIONS",
    description="A tuple specifying enabled python-markdown extensions.",
    editable=False,
    default=(),
)

register_setting(
    name="PAGEDOWN_USE_MEZZANINE_HTML_ESCAPE",
    description="Use MEZZANINE's HTML escape processing. "
	            "When set to True, HTML escape of MEZZANINE according to RICH TEXT FILTER is done. ",
    editable=False,
    default=False,
)
