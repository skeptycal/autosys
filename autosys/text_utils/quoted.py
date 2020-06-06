""" Shell Quoting

/**** The Open Group Base Specifications Issue 7, 2018 edition
    * IEEE Std 1003.1-2017 (Revision of IEEE Std 1003.1-2008)
    * (Issue 6 was the 2004 Edition)
    * Copyright © 2001-2018 IEEE and The Open Group
    * https://pubs.opengroup.org/onlinepubs/9699919799/ (accessed June 2, 2020)
    **************************************************************************/

1.1 Key Introductions
    (IEEE 1.1 Scope)
        POSIX.1-2017 defines a standard operating system interface and environment, including a command interpreter (or "shell"), and common utility programs to support applications portability at the source code level. It is intended to be used by both application developers and system implementors.

        POSIX.1-2017 comprises four major components (each in an associated volume):

            1. General terms, concepts, and interfaces common to all volumes of POSIX.1-2017, including utility conventions and C-language header definitions, are included in the Base Definitions volume of POSIX.1-2017.

            2. Definitions for system service functions and subroutines, language-specific system services for the C programming language, function issues, including portability, error handling, and error recovery, are included in the System Interfaces volume of POSIX.1-2017.

            3. Definitions for a standard source code-level interface to command interpretation services (a "shell") and common utility programs for application programs are included in the Shell and Utilities volume of POSIX.1-2017.

            4. Extended rationale that did not fit well into the rest of the document structure, containing historical information concerning the contents of POSIX.1-2017 and why features were included or discarded by the standard developers, is included in the Rationale (Informative) volume of POSIX.1-2017.

        The following areas are outside of the scope of POSIX.1-2017:

            - Graphics interfaces

            - Database management system interfaces

            - Record I/O considerations

            - Object or binary code portability

            - System configuration and resource availability

    (IEEE 1.3 Normative References)
        The following standards contain provisions which, through references in POSIX.1-2017, constitute provisions of POSIX.1-2017. At the time of publication, the editions indicated were valid. All standards are subject to revision, and parties to agreements based on POSIX.1-2017 are encouraged to investigate the possibility of applying the most recent editions of the standards listed below. Members of IEC and ISO maintain registers of currently valid International Standards.

            ANS X3.9-1978
                (Reaffirmed 1989) American National Standard for Information Systems: Standard X3.9-1978, Programming Language FORTRAN.1
            ISO/IEC 646:1991
                ISO/IEC 646:1991, Information Processing - ISO 7-Bit Coded Character Set for Information Interchange.2
            ISO 4217:2001
                ISO 4217:2001, Codes for the Representation of Currencies and Funds.
            ISO 8601:2004
                ISO 8601:2004, Data Elements and Interchange Formats - Information Interchange - Representation of Dates and Times.
            ISO C (1999)
                ISO/IEC 9899:1999, Programming Languages - C, including ISO/IEC 9899:1999/Cor.1:2001(E), ISO/IEC 9899:1999/Cor.2:2004(E), and ISO/IEC 9899:1999/Cor.3.
            ISO/IEC 10646-1:2000
                ISO/IEC 10646-1:2000, Information Technology - Universal Multiple-Octet Coded Character Set (UCS) - Part 1: Architecture and Basic Multilingual Plane.

1.2 Terminology regarding features:
    - legacy: retained for compatibility, but not appropriate for new applications
    - may: feature is optional - do not rely on this for essential features
    - shall: feature is mandatory
    - should: recommended, but not mandatory
    - undefined: feature resulting from invalid use (a coincidence)
    - unspecified: feature resulting from valid use (a bug)

1.3 Key Features:
1.1 POSIX System Interfaces


The following requirements apply to the system interfaces (functions and headers):


1.2 Portable Filename Character Set
        The set of characters from which portable filenames are constructed.

        A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
        a b c d e f g h i j k l m n o p q r s t u v w x y z
        0 1 2 3 4 5 6 7 8 9 . _ -

    LC_CTYPE
        The LC_CTYPE category shall define character classification, case conversion, and other character attributes.

    Ellipsis
        In addition, a series of characters can be represented by three adjacent <period> characters representing an ellipsis symbol ( "..." ).
            - The ellipsis specification shall be interpreted as meaning that all values between the values preceding and following it represent valid characters.
            - The ellipsis specification shall be valid only within a single encoded character set; that is, within a group of characters of the same size.
            - An ellipsis shall be interpreted as including in the list all characters with an encoded value higher than the encoded value of the character preceding the ellipsis and lower than the encoded value of the character following the ellipsis.

            For example:

            \x30;...;\x39;

The character classes digit, xdigit, lower, upper, and space have a set of automatically included characters. These only need to be specified if the character values (that is, encoding) differ from the implementation default values. It is not possible to define a locale without these automatically included characters unless some implementation extension is used to prevent their inclusion. Such a definition would not be a proper superset of the C or POSIX locale and, thus, it might not be possible for conforming applications to work properly.

I think this should be the other way around "$(pyenv init - zsh --no-rehash)". I tried this way and it didn't seem to solve, reverting the order worked fine.




****************************************************************************************

Shell Quoting
    The application *shall* quote the following characters if they are to represent themselves:

    |  &  ;  <  >  (  )  $  `  \  "  '  <space>  <tab>  <newline>

    Enclosing characters in single-quotes ( '' ) shall preserve the literal value of each character within the single-quotes. A single-quote cannot occur within single-quotes.

    Enclosing characters in double-quotes ( "" ) shall preserve the literal value of all characters within the double-quotes, with the exception of the characters dollar sign, backquote, and backslash, as follows:



# [9, 10, 32, 34, 36, 38, 39, 40, 41, 59, 60, 62, 92, 96, 124]

dollar sign, backquote, and backslash,
"""
from pprint import pprint

quoted_chars = "|&;<>()$`\\\"' \t\n"
print(quoted_chars)

quoted_dict = {f"c{ord(x)}": ord(x) for x in quoted_chars}

# pprint(quoted_dict)

quote_map = map(ord, quoted_chars)
print(sorted(list(quote_map)))
