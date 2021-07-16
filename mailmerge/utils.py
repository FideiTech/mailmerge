"""
Utility functions used by multiple mailmerge modules.

Andrew DeOrio <awdeorio@umich.edu>
"""
import io
import email


def flatten_message(message):
    """Return message as string.

    We can't use Python 3's message.__str__() because it doesn't work on Python
    2.  We can't use message.as_string() because it errors on UTF-8 headers.

    Based on Python 2 documentation
    https://docs.python.org/2/library/email.message.html

    """
    stream = io.StringIO()
    generator = email.generator.Generator(
        stream,
        mangle_from_=False,
        maxheaderlen=78,
        policy=message.policy.clone(cte_type=u"7bit"),
    )
    generator.flatten(message)
    text = stream.getvalue()
    return text
