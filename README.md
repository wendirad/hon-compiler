# HON Compiler
HON is a simple, human-readable, JSON-like syntax language for describing HTML documents.

## Features
- **Variable Declaration**: Yes, in HTML 😊
- **Loops**: Simple, easy, and lovable. 🪄 
- **Easy error handling**: No more unstructured results due to the missing closing tag. Hon is doing it by itself.

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
