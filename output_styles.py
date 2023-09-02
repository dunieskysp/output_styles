"""Versión resumida del paquete 'outputstyles' en un solo Script"""

# NOTE: Variables
all_styles = {
    'reset': '\033[0m',
    'bold': '01',
    'fg_red': '31',
    'fg_green': '32',
    'fg_yellow': '33',
    'fg_blue': '34',
    'fg_white2': '97',
    'bg_red': '41',
    'bg_green': '42',
    'bg_yellow': '43',
    'bg_blue': '44',
}
"""
Contiene solo los estilos de error(), warning(), success(), info(), bold():
- Formato (Reset, Bold)
- Color del Texto (Red, Green, Yellow, Blue, White2)
- Color del Fondo (Red, Green, Yellow, Blue)
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


# NOTE: Funciones principales
def add_text_styles(text, styles=[], all_styles=all_styles):
    """
    Aplicarles los estilos al texto.

    Parameters:
    text (str): Texto al que se le van a aplicar los estilos
    styles (list): Lista de estilos que se le van a aplicar al texto
    all_styles (dict): Diccionario con todos los estilos posibles

    Returns:
    srt: Devuelve el texto con los estilos aplicados
    """
    list_styles = []

    for style in styles:
        try:
            list_styles.append(all_styles[style])
        except KeyError:
            print(
                f'No exite el estilo: \033[1;31m{style}{all_styles["reset"]}')

    text_with_styles = f'\033[{";".join(list_styles)}m{text}'

    return f'{all_styles["reset"]}{text_with_styles}{all_styles["reset"]}'


def create_arg(color=None, msg_format=None):
    """
    Crear una Lista de los estilos que se le van a aplicar al texto
    en dependencia del tipo de mensaje.

    Parameters:
    color (str): Color del texto (Valor por defecto es 'None')
    msg_format (str): Formato del tipo de mensaje ('ico', 'btn', 'btn_ico')

    Returns:
    list (str): Devuelve una lista con los estilos a aplicar,
    - Si no tiene ningún color, devuelve el estilo en Negrita (bold)
    - Si no tiene formato o es de tipo icono, devuelve Negrita y el color del Texto (bold, fg_color)
    - Si es de tipo Botón o Botón con Icono, devuelve Negrita, color del Texto y del Fondo (bold, fg_color, bg_color)
    """
    if not color:
        return ["bold"]

    if msg_format == "ico" or not msg_format:
        return ["bold", f'fg_{color}']
    elif msg_format == "btn" or msg_format == "btn_ico":
        return ["bold", f'fg_white2', f'bg_{color}']


def print_message(text, msg_format=None, message_data=None):
    """
    Retornar el código del texto con los estilos aplicados, según el tipo de mensaje.

    Parameters:
    text (str): Texto al que se le van a aplicar los estilos
    msg_format (str): Formato del tipo de mensaje ('ico', 'btn', 'btn_ico')
    message_data (dict): Datos del tipo de mensaje (error_data, warning_data, success_data, info_data)

    Returns:
    srt: Devuelve el código del texto con los estilos aplicados
    """
    if msg_format == "ico":
        text = f'{message_data["ico_code"]} {text}'
    elif msg_format == "btn_ico":
        text = f' {message_data["ico_code"]} {text} '

    if message_data:
        list_styles = create_arg(message_data['color'], msg_format)
    else:
        list_styles = create_arg()

    return add_text_styles(text, list_styles)


# NOTE: Funciones de los diferentes tipos de mensajes
def error(text, msg_format=None, message_data=error_data):
    """
    Mensaje de tipo de Error

    Parameters:
    text (str): Texto al que se le van a aplicar los estilos
    msg_format (str): Formato del tipo de mensaje ('ico', 'btn', 'btn_ico')
    message_data (dict): Datos del tipo de mensaje (error_data)

    Returns:
    srt: Devuelve el texto con los estilos aplicados
    """
    return print_message(text, msg_format, message_data)


def warning(text, msg_format=None, message_data=warning_data):
    """
    Mensaje de tipo de Warning

    Parameters:
    text (str): Texto al que se le van a aplicar los estilos
    msg_format (str): Formato del tipo de mensaje ('ico', 'btn', 'btn_ico')
    message_data (dict): Datos del tipo de mensaje (warning_data)

    Returns:
    srt: Devuelve el texto con los estilos aplicados
    """
    return print_message(text, msg_format, message_data)


def success(text, msg_format=None, message_data=success_data):
    """
    Mensaje de tipo de Success

    Parameters:
    text (str): Texto al que se le van a aplicar los estilos
    msg_format (str): Formato del tipo de mensaje ('ico', 'btn', 'btn_ico')
    message_data (dict): Datos del tipo de mensaje (success_data)

    Returns:
    srt: Devuelve el texto con los estilos aplicados
    """
    return print_message(text, msg_format, message_data)


def info(text, msg_format=None, message_data=info_data):
    """
    Mensaje de tipo de Info

    Parameters:
    text (str): Texto al que se le van a aplicar los estilos
    msg_format (str): Formato del tipo de mensaje ('ico', 'btn', 'btn_ico')
    message_data (dict): Datos del tipo de mensaje (info_data)

    Returns:
    srt: Devuelve el texto con los estilos aplicados
    """
    return print_message(text, msg_format, message_data)


def bold(text):
    """
    Mensaje de tipo de Bold

    Parameters:
    text (str): Texto que se va a poner en Negrita

    Returns:
    srt: Devuelve el texto en Negrita
    """
    return print_message(text)


# NOTE: Mostrar los diferentes tipos de mensajes
if __name__ == "__main__":
    functions_styles = {
        "error": error,
        "warning": warning,
        "success": success,
        "info": info,
        "bold": bold
    }
    """Nombre de las Funciones de los diferentes tipos de mensajes"""

    function_options = [None, "btn", "ico", "btn_ico"]
    """Opciones para los diferentes tipos de mensajes"""

    def print_all_messages(dict_functions, list_options):
        """
        Imprimir los diferentes tipos de mensajes con todas sus variantes de formato

        Parameters:
        dict_functions (dict): Nombres de las funciones de los tipos de mensajes
        list_options (list): Formato del tipo de mensaje (None, 'ico', 'btn', 'btn_ico')

        Returns:
        print: Imprime el texto con los estilos aplicados
        """

        for func_name in dict_functions:
            func_style = dict_functions[func_name]

            text_print = f'{func_name.capitalize()}!'

            if func_name == "bold":
                print(func_style(text_print), '-->',
                      f'{func_name}("{text_print}")')
            else:
                for option in list_options:
                    if not option:
                        print(func_style(text_print),
                              '-->', f'{func_name}("{text_print}")')
                    else:
                        print(func_style(text_print, option), '-->',
                              f'{func_name}("{text_print}", "{option}")')
            print("")

    print(info("Ejemplos del resultado final y como usarlo:\n"))
    print_all_messages(functions_styles, function_options)
