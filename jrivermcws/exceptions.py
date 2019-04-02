"""
jrivermcws.exceptions
~~~~~~~~~~~~~~~~~~~~~~

For when things are used wrong

~~~~~~~~~~~~~~~

Copyright Michael Adkins 2017
Distributed under the MIT License.
See accompanying file LICENSE.md file or copy at http://opensource.org/licenses/MIT

"""


class BadCommandException(ValueError):
    """Command was bad in some way"""
    pass


class NullCommandException(BadCommandException):
    """A None value command was passed"""
    pass


class MissingParametersException(BadCommandException):
    """Not enough parameters for given command"""
    pass


class FailedAuthenticationException(ValueError):
    """Username or password incorrect or no auth?"""
    pass
