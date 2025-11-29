
<p align="center">
    <img src="https://i.ibb.co/cXV5p25L/1000008279-removebg-preview.png" alt="1000008279-removebg-preview" border="0" />
</p>

<h1 align="center">HON (HTML Object Notation) ✨ </h1>

**HON** – a clean, human-readable, JSON-like language for writing HTML that feels natural and joyful.

## Why HON? 🚀

- HTML without the tag soup  
- Structure as clear as JSON, but made for humans  
- No more missing closing tags – ever  
- Variables, loops, and real power in minimal syntax  

Write HTML the way it should have always been.

## Features 🔥

- Variables → `%%title="Hello World"` ♻️  
- Clean loops → repeat anything effortlessly 🔁  
- Auto-balanced tags → perfectly valid HTML guaranteed 🛡️  
- Helpful, precise error messages ⚡  

Ideal for learning, prototyping, static sites, or just loving clean code.

Ready to write beautiful HTML again? Dive in! 👇

## Example
```
%%title="Hello, World!"
"<!doctype html>"
:html[lang="en"] {
  :head {
    :meta (
      [charset="utf-8"]
      [name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"]
    )
    :link:[rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css"]
    :title { %title }
  }
  :body {
    :h1 { %title }
    :script[src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js"]
  }
}
```
### Output
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8"></meta>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"></meta>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" />
    <title>Hello, World!</title>
  </head>
  <body>
    <h1>Hello, World!</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js"></script>
  </body>
</html>
```

## Grammer
* This grammar is described in the `BNF` Backus Normal Form or Backus Naur Form. 

```
<expression> ::= 
            | <string> <expression>
            | <variable_definition> <expression>
            | <variable_access> <expression>
            | <tag> <expression>
            | <content> <expression>
```

```
<content> ::= <tag>  <left_brace> <expression> <right_brace>

```

```
<tag> ::= <tag_name>
            | <tag_name> <bracket_definition>
            | <tag_name> <left_parentheses> <bracket_definition> <bracket_definition> <multiple_bracket_definition> <right_parentheses>
```

```
<multiple_bracket_definition> ::=
            | <bracket_definition> <multiple_bracket_definition>
```

```
<bracket_definition> ::= <left_bracket> <attribute_definition> <comma> <multiple_attribute_definition> <right_bracket>

```

```
<multiple_attribute_definition> ::=
            | <attribute_definition> <comma> <multiple_attribute_definition>
```

```
<attribute_definition> ::= <attribute_name> <assignment_operator> <string>
            | <attribute_name> <assignment_operator> <multiple_variable_access>
```

```
<multiple_variable_access> ::=
            | <variable_access> <multiple_variable_access>
```

```
<variable_definition> ::=  <variable> <assignment_operator> <string>
```

```
<tag_name> ::= ":[a-zA-Z0-9\_]+"
            | ":([a-zA-Z0-9\_]+):"

<variable> ::= \%\%[a-zA-Z]\w+

<variable_access> ::= "\%[a-zA-Z\_]+[a-zA-Z0-9\_]+"

<attribute_name> ::= "[a-zA-Z]+(-[a-zA-Z]+)*"

<string> ::= "(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'

<assignment_operator> ::= "="

<comma> ::=
            | ","

<left_brace> ::= "{"

<right_brace> ::= "}"

<left_parentheses> ::= "("

<right_parentheses> ::= ")"

<left_bracket> ::= "["

<right_bracket> ::= "]"
```

<h1 align="center">𝕋𝕙𝕒𝕟𝕜 𝕐𝕠𝕦 ♡</h1>
