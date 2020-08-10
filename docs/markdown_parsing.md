## blocks of text

Text that is separated by blank lines ...

is assumed to the the start of a new paragraph.
No need for <br /> tags

## headers (main and sub; H1 and H2)

The official method for inserting headers

# This is an H1

## This is an H2

is to place equals signs under the words. It doesn't matter now many = or - are used, but at least 3 is standard.

## headers 1-6

using # symbols is the more common way to indicate headers

# H1

## H2

### H3

#### H4

##### H5

###### H6

## picture links -

![Twitter Follow](https://img.shields.io/twitter/follow/skeptycal.svg?style=social) ![GitHub followers](https://img.shields.io/github/followers/skeptycal.svg?label=GitHub&style=social)

## links

[Follow on Twitter](https://img.shields.io/twitter/follow/skeptycal.svg?style=social)

> files on local machine
> [About](./README.md)

## Reference Links

[License][1]

    # this is placed where the link goes:

    [License][1]

    # then place the reference anywhere in the document
    # gathering them all at the end like footnotes is common
    # the following are equivalent.

    [foo]: http://example.com/  "Optional Title Here"
    [foo]: http://example.com/  'Optional Title Here'
    [foo]: http://example.com/  (Optional Title Here)

**There is currently a bug with using single quotes**

> The implicit link name shortcut allows you to omit the name of the link

    Use the link [Google][] inline...
    [Google]: https://www.google.com

Use the link [Google][] inline...

## table

| this   |  is   |         a | table |   header |
| :----- | :---: | --------: | :---: | -------: |
| data   |   x   |         y |   z   | sin(tax) |
| more   | data  |        is | good  |    forus |
| aligns |  are  | important |  not  |  spacing |

## bold / italic

_italic_
**bold**
**_both_**
`code`

## code blocks

> indenting indicates a block of source code

    # so you can type quick examples like this
    from os import linesep as NL

    def double_space(*a, **k):
        """
        Print arguments double spaced.
        """
        print(*a, NL, **k)

> using specific ```python

```py
    # this python code will be color formatted in many editors
    # and on many platforms that serve markdown

    from os import linesep as NL

    def double_space(*a, **k):
        """
        Print arguments double spaced.
        """
        print(*a, NL, **k)
```

> Here is an example of AppleScript:

    tell application "Foo"
        beep
    end tell

> Easy html examples without messing with escaped characters

    <div class="footer">
        &copy; 2004 Foo Corporation
    </div>

> This markdown code

    <p>This is a normal paragraph:</p>

    <pre><code>This is a code block.
    </code></pre>

> Turns into this:

<p>This is a normal paragraph:</p>

<pre><code>This is a code block.
</code></pre>

## escaped characters?

## lists

> Unordered lists use asterisks, pluses, and hyphens — interchangably — as list markers:

-   Red
-   Green
-   Blue

> is equivalent to:

-   Red
-   Green
-   Blue

> and:

-   Red
-   Green
-   Blue

> Ordered lists use numbers followed by periods:

1.  Bird
2.  McHale
3.  Parish

> To make lists look nice, you can wrap items with hanging indents:

-   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
    viverra nec, fringilla in, laoreet vitae, risus.
-   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
    Suspendisse id sem consectetuer libero luctus adipiscing.

## block quotes

> this is a quote

## Nested quotes

> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.

> ## This is a header.
>
> 1.  This is the first list item.
> 2.  This is the second list item.
>
> Here's some example code:
>
>     return shell_exec("echo $input | $markdown_script");

## inline HTML

> Block tags must be separated from markdown by a blank line...

<table>
    <tr>
        <th>Foo</th><th>Bar</th>
    </tr>
    <tr>
        <td>Foo</td><td>Bar</td>
    </tr>
</table>

> Markdown tags are not parsed inside of html block level tags. (div, table, pre, p, etc)

**emphasis**

<div>
**emphasis**
</div>

> Unlike block-level HTML tags, Markdown syntax is processed within span-level tags. (span, cite, a, img, etc)

<span>This is some **emphasis** within an html tag.</span>

> Special html characters are escaped automatically

& shows up as &
< shows up as <

```
<p> shows up as a paragraph!
```

<p> shows up as a paragraph!

using &lt; works fine, like &lt;p>

## other bits

&amp;copy; is the copyright symbol &copy;

AT&T gets translated into AT&amp;T

4 < 5 gets translated into 4 &lt; 5

## HR's

Any of these will work. VSCode translates them all into `---` anyway.

    * * *

    ***

    *****

    - - -

    ---------------------------------------

[1]: ./LICENSE 'license file hover title'
[google]: https://www.google.com
