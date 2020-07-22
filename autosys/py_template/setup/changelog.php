#!/usr/bin/env php
<?php
/*
 * changelog.php - template for a GitHub repository 'CHANGELOG' file
 *   that formats MD to HTML on the fly as needed (MD=True)
 * @version 0.4.0
 * @php > 7.2 (mainly for HEREDOC updates)
 *
 */

// !------------------------------------------------------> Utilities
function br($n=1) { return str_repeat(PHP_EOL, $n); } // insert a number of CLI linebreaks
function h($string="") { return htmlspecialchars($string); } // encode html
function headers($html) { // replace html head tags
    $changelog = preg_replace("/^(# )(.*)/", "<h1>$2</h1>", $changelog);
    $changelog = preg_replace("/^(## )(.*)/", "<h2>$2</h2>", $changelog);
    $changelog = preg_replace("/^(### )(.*)/", "<h3>$2</h3>", $changelog);
    $changelog = preg_replace("/^(#### )(.*)/", "<h4>$2</h4>", $changelog);
    $changelog = preg_replace("/^(##### )(.*)/", "<h5>$2</h5>", $changelog);
    $changelog = preg_replace("/^(###### )(.*)/", "<h6>$2</h6>", $changelog);
    }

function md2html($html) {
    // MD to HTML patterns
    // beginning of line:
    // $RE_line_start = "/^#.*/";
    headers($html);
    // replacing # to ###### with <H1> - <H6>

    }

function head($title, $tags='', $scripts='', $css='', $lang='en', $charset='UTF-8') { // Returns an html <HEAD></HEAD> section
    return h(<<<HEADER
    <!DOCTYPE html>
    <html lang="$lang">
    <head>
        <meta charset="$charset">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>$title</title>
        $tags
        $scripts
        $css
    </head>
    HEADER);
    }

function foot($info = '') { // Returns an html <HEAD></HEAD> section
    return h(<<<FOOTER
    $info
    </footer>
    FOOTER);
    }

function create_html($body,
              $header = $default_header,
              $footer = $default_footer
              ) {
              // Returns an html page using parameters
              //   for header, body, footer.
    return h(<<<EOL
    $header
    $body
    $footer

    EOL)
    ;
    }

// !------------------------------------------------------> Defaults
$title = 'CHANGELOG';
$meta_tags = '';
$header_scripts = '';
$default_header = head('CHANGELOG');


$default_footer = <<<FOOTER
    </html>
    FOOTER;

// !------------------------------------------------------> The CHANGELOG path
// TODO: find the git repo root and use 'CHANGELOG.md' from there
// only run from a git repo root
$changelog_path = "../CHANGELOG.md"; // up one directory ...

//! ------------------------------------------------------> DEBUG
$changelog_path = '/Users/skeptycal/Documents/coding/python/autosys/CHANGELOG.md';
// $changelog = file_get_contents( $changelog_path );
$sample_changelog = <<<SAMPLE
    # This is the title. # asdf##
    ## line #2.
    #### title 4
    ### title 3
    ### not ...


SAMPLE
;

// !------------------------------------------------------> Content





include (changelog_header.php);
content();
include (changelog_footer.php);

// References:

// $changelog = preg_replace( "/###[ ]?([0-9\.]+): ([A-Z0-9 ,]+)/i", "<h3>$1</h3>" . PHP_EOL . "<i>$2</i>" . PHP_EOL . "<ul>", $changelog );
// $changelog = preg_replace( "/\* ([A-Z0-9 \._,'\(\)\/\-&\"\']+)/i", "<li>$1</li>", $changelog );
// $changelog = preg_replace( "/" . PHP_EOL . "<h3>/i", "</ul>" . PHP_EOL . PHP_EOL . "<h3>", $changelog );
// $changelog .= PHP_EOL . "</ul>";

// // Ouput. Copy and paste this to your website.
// echo '<textarea name="changelog" cols="100" rows="30">' . $changelog . '</textarea><br />';
