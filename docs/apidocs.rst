wttr.py API documentation
=========================

.. py:function:: getWttr([where=None, [loc="en"]])

    A function that returns a string with wttr.in's response.

    ``where`` is ``None`` or a string that contains city name, (ex. ``paris``) any location, (``+`` for spaces, ex.  ``~Eiffel+tower``)
    Unicode name of any location in any language, (ex. ``Москва``) airport code, (3 letters, ex. ``muc``) domain name, (ex. ``@stackoverflow.com``)
    area codes (ex. ``94107``) or GPS coordinates (ex. ``-78.46,106.79``)

    If ``where`` is not given or ``None``, then location will be auto-detected by wttr.in depending on your IP.

    ``loc`` is the language code (ex. ``en``, ``fr``. Look for the full list of supported languages here_) that you want wttr.in respond in.

    .. _here: https://wttr.in/:help