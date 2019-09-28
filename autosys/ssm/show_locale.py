#!/usr/bin/env python3
""" locale_env.py """
import locale
import os
import pprint
import sys

pp = pprint.PrettyPrinter(indent=4)
locale.setlocale(locale.LC_ALL, '')
DEFAULT_LOCALE: str = locale.getlocale()
print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())


def print_env_settings():
    """
    Print Brief Locale Information (language, encoding)
    """
    print('Environment settings:')
    for env_name in ['LC_ALL', 'LC_CTYPE', 'LANG', 'LANGUAGE']:
        print('  {} = {}'.format(
            env_name, os.environ.get(env_name, ''))
        )


def print_locale_settings():
    """
    Print detailed locale information for internationalization.
    """
    print('\nLocale from environment:', DEFAULT_LOCALE)

    template = """
  Numeric formatting:

    Decimal point      : "{decimal_point}"
    Grouping positions : {grouping}
    Thousands separator: "{thousands_sep}"

  Monetary formatting:

    International currency symbol   : "{int_curr_symbol!r}"
    Local currency symbol           : {currency_symbol!r}
    Symbol precedes positive value  : {p_cs_precedes}
    Symbol precedes negative value  : {n_cs_precedes}
    Decimal point                   : "{mon_decimal_point}"
    Digits in fractional values     : {frac_digits}
    Digits in fractional values,
                    international  : {int_frac_digits}
    Grouping positions              : {mon_grouping}
    Thousands separator             : "{mon_thousands_sep}"
    Positive sign                   : "{positive_sign}"
    Positive sign position          : {p_sign_posn}
    Negative sign                   : "{negative_sign}"
    Negative sign position          : {n_sign_posn}

  """

    sign_positions = {
        0: 'Surrounded by parentheses',
        1: 'Before value and symbol',
        2: 'After value and symbol',
        3: 'Before value',
        4: 'After value',
        locale.CHAR_MAX: 'Unspecified',
    }

    info = {}
    info.update(locale.localeconv())
    info['p_sign_posn'] = sign_positions[info['p_sign_posn']]
    info['n_sign_posn'] = sign_positions[info['n_sign_posn']]

    print(template.format(**info))


# pprint.
