"""
Paquete 'outputstyles' en un solo Módulo.
"""

# NOTE: Variables a usar.
all_styles = {

    # Formatos.
    'reset': '\033[0m',
    'bold': '01',
    'disabled': '02',
    'italic': '03',
    'underline': '04',
    'blink': '05',
    'blink2': '06',
    'reverse': '07',
    'invisible': '08',
    'strike_through': '09',

    # Colores del Texto.
    'fg_black': '30',
    'fg_red': '31',
    'fg_green': '32',
    'fg_yellow': '33',
    'fg_blue': '34',
    'fg_magenta': '35',
    'fg_cyan': '36',
    'fg_white': '37',
    'fg_black2': '90',
    'fg_red2': '91',
    'fg_green2': '92',
    'fg_yellow2': '93',
    'fg_blue2': '94',
    'fg_magenta2': '95',
    'fg_cyan2': '96',
    'fg_white2': '97',

    # Colores del Fondo.
    'bg_black': '40',
    'bg_red': '41',
    'bg_green': '42',
    'bg_yellow': '43',
    'bg_blue': '44',
    'bg_magenta': '45',
    'bg_cyan': '46',
    'bg_white': '47',
    'bg_black2': '100',
    'bg_red2': '101',
    'bg_green2': '102',
    'bg_yellow2': '103',
    'bg_blue2': '104',
    'bg_magenta2': '105',
    'bg_cyan2': '106',
    'bg_white2': '107',
}
"""
Contiene todos los estilos que se le pueden aplicar a los textos:
- Formato (Bold, Underline, etc).
- Color del Texto (Red, Black, Green, etc).
- Color del Fondo (Red, Black, Green, etc).
"""

error_data = {"ico_code": "\u2718", "color": "red"}
"""
Datos del Mensaje de tipo 'Error'
- Icono: \u2718
- Color: Red
"""


warning_data = {"ico_code": "\u26A0", "color": "yellow"}
"""
Datos del Mensaje de tipo 'Warning'
- Icono: \u26A0
- Color: Yellow
"""


success_data = {"ico_code": "\u2714", "color": "green"}
"""
Datos del Mensaje de tipo 'Success'
- Icono: \u2714
- Color: Green
"""


info_data = {"ico_code": "\u24D8", "color": "blue"}
"""
Datos del Mensaje de tipo 'Info'
- Icono: \u24D8
- Color: Blue
"""


# NOTE: Funciones principales.
def add_text_styles(text: str, styles: list = [], all_styles: dict = all_styles) -> str:
    """
    Aplicarles los estilos al texto.

    Parameters:
    text (str): Texto al que se le van a aplicar los estilos.
    styles (list) [Opcional]: Lista de estilos que se le van a aplicar al texto.
    all_styles (dict): Diccionario con todos los estilos posibles.

    Returns:
    srt: Devuelve el texto con los estilos aplicados.
    """

    # Comprobar que existan estilos en los argumentos y que sea una lista.
    if not styles or type(styles) != list:
        return text

    # Lista resultante de los estilos que se van a aplicar.
    list_styles = []

    # Recorrer todos los estilos pasados como argumentos e ir aplicandolos.
    for style in styles:

        # Asignar el estilo de turno.
        try:

            # Agregar el valor del estilo a la lista resultante.
            list_styles.append(all_styles[style])

        # En caso de que no exista el estilo (key), imprimimos un error.
        except KeyError:

            msg_bold = f'\033[{all_styles["bold"]}m'
            msg_error = f'\033[{all_styles["bold"]};{all_styles["fg_red"]}m'

            print(
                msg_bold + "No pudo aplicar el estilo:" + all_styles["reset"],
                msg_error + style + all_styles["reset"]
            )

    # Concatenamos los estilos separados por ";" con el texto,
    # además de agregarle "\033[" y "m" para que sea válido el código ANSI.
    # Ej: \033[01;91mTexto
    text_with_styles = f'\033[{";".join(list_styles)}m{text}'

    # Retornamos el texto con los estilos aplicados, al inicio y al final de este reseteamos los estilos.
    return f'{all_styles["reset"]}{text_with_styles}{all_styles["reset"]}'


def create_arg(color: str = "", msg_format: str = "") -> list:
    """
    Crear una Lista de los estilos que se le van a aplicar al texto
    en dependencia del tipo de mensaje.

    Parameters:
    color (str) [Opcional]: Color del texto.
    msg_format (str) [Opcional]: Formato del tipo de mensaje ('ico', 'btn', 'btn_ico')

    Returns:
    list: Devuelve una lista con los estilos a aplicar.
    - Si no tiene formato o es de tipo icono, devuelve Negrita y el color del Texto [bold, fg_color]
    - Si es de tipo Botón o Botón con Icono, devuelve Negrita, color del Texto y del Fondo [bold, fg_color, bg_color]
    - Si no tiene ningún color o formato no válido, devuelve el estilo en Negrita [bold]
    """

    # Si el mensaje tiene el Icono inicialmete o es solo el texto.
    if (not msg_format or msg_format == 'ico') and color:

        # Retornamos el estilo en "Negrita" y el color del texto según el tipo de mensaje.
        return ['bold', f'fg_{color}']

    # Si el mensaje es de tipo Botón o de Botón con icono.
    elif msg_format in ["btn", "btn_ico"] and color:

        # Retornamos el estilo en "Negrita", el color del texto en blanco y color de fondo según el tipo de mensaje.
        return ['bold', 'fg_white2', f'bg_{color}']

    # Si no tiene color o es un formato no válido.
    else:

        # Retornamos solamente el estilo en "Negrita".
        return ["bold"]


def add_icono(text: str, msg_format: str = "", ico_code: str = "") -> str:
    """
    Agregarle un icono delante del texto del mensaje.

    Parameters:
    text (str): Texto al que se le va a agregar el icono.
    msg_format (str) [Opcional]: Formato del tipo de mensaje ('ico', 'btn', 'btn_ico').
    ico_code (str) [Opcional]: Código del icono que se va a agregar.

    Returns:
    srt: Devuelve el texto con los estilos aplicados.
    """

    # Si es de tipo Icono el mensaje.
    if msg_format == "ico" and ico_code:

        # Concatenamos el icono al inicio del texto.
        return f'{ico_code} {text}'

    # Si es de tipo Botón con Icono el mensaje.
    elif msg_format == "btn_ico" and ico_code:

        # Concatenamos el icono al inicio del texto, dejando un espacio al inicio y final.
        return f' {ico_code} {text} '

    # Si no tiene formato o código del icono o no es válido alguno de los dos.
    else:

        # Retornamos solo el Texto.
        return text


def apply_styles(text: str, msg_format: str = "", message_data: dict = {}) -> str:
    """
    Retornar el texto con los estilos aplicados, según el tipo de mensaje.

    Parameters:
    text (str): Texto al que se le van a aplicar los estilos.
    msg_format (str) [Opcional]: Formato del tipo de mensaje ('ico', 'btn', 'btn_ico').
    message_data (dict) [Opcional]: Datos del tipo de mensaje (error_data, warning_data, success_data, info_data).

    Returns:
    srt: Devuelve el texto con los estilos aplicados.
    """

    # Obtener los valores de los datos del mensaje.
    ico_code = message_data.get("ico_code", "")
    color = message_data.get("color", "")

    # Agregar el icono en caso de que lo lleve.
    text = add_icono(text, msg_format, ico_code)

    # Obtener la Lista de los estilos que se le van a aplicar al texto.
    list_styles = create_arg(color, msg_format)

    # Retornamos el código del texto con los estilos aplicados.
    return add_text_styles(text, list_styles)


# NOTE: Funciones de los diferentes tipos de mensajes.
def error(text: str, msg_format: str = "", message_data: dict = error_data) -> str:
    """
    Mensaje de tipo de Error.

    Parameters:
    text (str): Texto al que se le van a aplicar los estilos.
    msg_format (str) [Opcional]: Formato del tipo de mensaje ('ico', 'btn', 'btn_ico').
    message_data (dict): Datos del tipo de mensaje (error_data).

    Returns:
    srt: Devuelve el texto con los estilos aplicados.
    """
    return apply_styles(text, msg_format, message_data)


def warning(text: str, msg_format: str = "", message_data: dict = warning_data) -> str:
    """
    Mensaje de tipo de Warning.

    Parameters:
    text (str): Texto al que se le van a aplicar los estilos.
    msg_format (str) [Opcional]: Formato del tipo de mensaje ('ico', 'btn', 'btn_ico').
    message_data (dict): Datos del tipo de mensaje (warning_data).

    Returns:
    srt: Devuelve el texto con los estilos aplicados.
    """
    return apply_styles(text, msg_format, message_data)


def success(text: str, msg_format: str = "", message_data: dict = success_data) -> str:
    """
    Mensaje de tipo de Success.

    Parameters:
    text (str): Texto al que se le van a aplicar los estilos.
    msg_format (str) [Opcional]: Formato del tipo de mensaje ('ico', 'btn', 'btn_ico').
    message_data (dict): Datos del tipo de mensaje (success_data).

    Returns:
    srt: Devuelve el texto con los estilos aplicados.
    """
    return apply_styles(text, msg_format, message_data)


def info(text: str, msg_format: str = "", message_data: dict = info_data):
    """
    Mensaje de tipo de Info.

    Parameters:
    text (str): Texto al que se le van a aplicar los estilos.
    msg_format (str) [Opcional]: Formato del tipo de mensaje ('ico', 'btn', 'btn_ico').
    message_data (dict): Datos del tipo de mensaje (info_data).

    Returns:
    srt: Devuelve el texto con los estilos aplicados.
    """
    return apply_styles(text, msg_format, message_data)


def bold(text: str) -> str:
    """
    Mensaje de tipo de Bold.

    Parameters:
    text (str): Texto que se va a poner en Negrita.

    Returns:
    srt: Devuelve el texto en Negrita.
    """
    return apply_styles(text)


# NOTE: Mostrar los diferentes tipos de mensajes
if __name__ == "__main__":

    func_style_names = {
        "error": error,
        "warning": warning,
        "success": success,
        "info": info,
        "bold": bold
    }
    """Nombre de las Funciones de los diferentes tipos de mensajes."""

    format_options = ["btn", "ico", "btn_ico"]
    """Opciones de los formatos para los diferentes tipos de mensajes."""

    def print_all_messages(func_style_names: dict, format_options: list) -> None:
        """
        Imprimir los diferentes tipos de mensajes con todas sus variantes de formato.

        Parameters:
        func_style_names (dict): Nombres de las funciones de los tipos de mensajes.
        format_options (list): Formatos del tipo de mensaje ('ico', 'btn', 'btn_ico').

        Returns:
        None: Imprime el texto con los estilos aplicados.
        """

        # Recorrer todas las funciones según su "Key" dentro del diccionario de funciones.
        for func_name in func_style_names:

            # Obtener la función declarada del tipo de mensaje.
            func_type_msg = func_style_names[func_name]

            # El Texto a imprimir es el nombre de la función en Mayúscula, más el simbolo "!".
            msg_text = f'{func_name.capitalize()}!'

            # Imprimir sin opciones de formato la primera vez.
            print(
                func_type_msg(msg_text),
                '-->', f'{func_name}("{msg_text}")'
            )

            # Recorrer las opciones para imprimir sus variantes de formatos.
            for msg_format in format_options:

                # Si es la función de Bold porque esta no tiene diferentes formatos.
                if func_name == "bold":
                    break

                # Imprimir cada tipo de opción (btn, fig, btn_fig).
                else:

                    print(
                        func_type_msg(msg_text, msg_format), '-->',
                        f'{func_name}("{msg_text}", "{msg_format}")'
                    )

            # Dejar un espacio entre cada bloque de tipo de mensajes.
            print("")

    # Imprimir todos los tipos de mensajes con todas sus variantes.
    print(info("Ejemplos del resultado final y como usarlo:\n"))
    print_all_messages(func_style_names, format_options)
