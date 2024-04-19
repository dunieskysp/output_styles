# Output Styles

Aplicarle estilos al texto de salida por CLI.

## Instalación

```bash
  pip install outputstyles
```

## Uso/Ejemplos

### 1 - Usar los diferentes tipos de mensajes y estilos implementados

**Tipos de mensajes implementados:**

| Message   | Description                                   |
| --------- | --------------------------------------------- |
| `error`   | Admite las variantes: **_btn, ico, btn_ico_** |
| `warning` | Admite las variantes: **_btn, ico, btn_ico_** |
| `success` | Admite las variantes: **_btn, ico, btn_ico_** |
| `info`    | Admite las variantes: **_btn, ico, btn_ico_** |
| `bold`    | No tiene variantes.                           |

**Usar los tipos de mensajes implementados:**

```py
from outputstyles import error, warning, info, success, bold

# Print error messages.
print(error("Error!"))
print(error("Error!", "btn"))
print(error("Error!", "ico"))
print(error("Error!", "btn_ico"))

# Print warning messages.
print(warning("Warning!"))
print(warning("Warning!", "ico"))
print(warning("Warning!", "btn"))
print(warning("Warning!", "btn_ico"))

# Print warning messages.
print(success("Success!"))
print(success("Success!", "btn"))
print(success("Success!", "ico"))
print(success("Success!", "btn_ico"))

# Print info messages.
print(info("Info!"))
print(info("Info!", "btn"))
print(info("Info!", "ico"))
print(info("Info!", "btn_ico"))

# Print text in bold style.
print(bold("Bold!"))
```

Resultado:

![output_styles](docs/img/outputstyles_all.png)

### 2 - Agregar otros estilos al texto

**Modificadores y estilos que se le pueden aplicar al texto de salida:**

| Modifiers      | Foreground | Foreground light | Background | Background light |
| -------------- | ---------- | ---------------- | ---------- | ---------------- |
| reset          | fg_black   | fg_light_black   | bg_black   | bg_light_black   |
| bold           | fg_red     | fg_light_red     | bg_red     | bg_light_red     |
| disabled       | fg_green   | fg_light_green   | bg_green   | bg_light_green   |
| italic         | fg_yellow  | fg_light_yellow  | bg_yellow  | bg_light_yellow  |
| underline      | fg_blue    | fg_light_blue    | bg_blue    | bg_light_blue    |
| blink          | fg_magenta | fg_light_magenta | bg_magenta | bg_light_magenta |
| blink2         | fg_cyan    | fg_light_cyan    | bg_cyan    | bg_light_cyan    |
| reverse        | fg_white   | fg_light_white   | bg_white   | bg_light_white   |
| hidden         |            |                  |            |                  |
| strike_through |            |                  |            |                  |

**Aplicar estilos personalizados:**

```py
from outputstyles import add_text_styles

# Styles of the text.
styles = ["fg_red", "underline"]

print(add_text_styles("Hola", styles))
```

Resultado:

![output_styles](docs/img/custom_styles.png)

### 3 - Crear nuevas funciones

**Definir los datos y la función del nuevo tipo de mensaje:**

```py
from outputstyles import apply_styles

# Data of the new message.
msg_data = {
    "ico_code": "\u2726",
    "color": "cyan"
}


# Apply the style of the new message type.
def new_msg(text: str, msg_format: str = "", message_data: dict = msg_data) -> str:
    return apply_styles(text, msg_format, message_data)


print(new_msg("Nuevo estilo"))
print(new_msg("Nuevo estilo", "btn"))
print(new_msg("Nuevo estilo", "ico"))
print(new_msg("Nuevo estilo", "btn_ico"))
```

Resultado:

![output_styles](docs/img/new_message_type.png)

## Screenshots

![output_styles](docs/img/output_styles_light.png)

## License

[MIT](LICENSE)

## Authors

- [@dunieskysp](https://github.com/dunieskysp)
