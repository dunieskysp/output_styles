"""
Funciones para aplicar los estilos al texto
"""

# Importar variable con todos los estilos
from variables import all_styles


def add_text_styles(text, styles=[]):
    """
    Aplicarles los estilos al texto

    Parameters:
    text (str): Texto al que se le va a aplicar los estilos
    styles (list): Lista de estilos que se le van a aplicar al texto

    Returns:
    srt: Devuelve el texto con los estilos aplicados
    """

    # Inicializar los estilos (se le agrega al inicio el código ANSI)
    result_styles = '\033['

    # Variable para verificar si ya tiene algún estilo aplicado
    add_style = False

    # Recorrer todos los estilos pasados como argumentos e ir aplicandolos
    for style in styles:
        # Tratar de asignar el estilo de turno
        try:
            # Comprobar si es el primer estilo o no
            if not add_style:
                # Agregar el valor del estilo según su "Key" en el diccionario "all_styles"
                result_styles += all_styles[style]
                # Confirmar que ya se agregó el primer estilo
                add_style = True

            # Si hay más de un estilo, los separamos por ";"
            else:
                result_styles += ';' + all_styles[style]

        # En caso de que no exista el estilo, lo imprimimos como un error
        except KeyError:
            print(
                f'No exite el estilo: \033[1;31m{style}{all_styles["reset"]}')

    # Concatenamos todos los estilos con el texto y antes del texto agregamos "m" para que sea válido el código ANSI
    result_styles += "m" + text

    # Retornamos el texto con los estilos aplicados, al inicio y al final de este reseteamos los estilos
    return f'{all_styles["reset"]}{result_styles}{all_styles["reset"]}'


# Función para crer una "Lista" de los argumentos con el formato del mensaje, cada tipo de mensaje se identifica con un color único
def create_arg(color=None, msg_format=None):
    # En caso de que no se especifique ningún color
    if not color:
        # Retornamos solamente el estilo en "Negrita"
        return ["bold"]

    # Si el mensaje tiene el icono inicialmete o es solo el texto
    if msg_format == "ico" or not msg_format:
        # Retornamos el estilo en "Negrita" y el color del texto según el tipo de mensaje
        return ["bold", f'fg_{color}']

    # Si el mensaje es de tipo botón o de botón con icono
    elif msg_format == "btn" or msg_format == "btn_ico":
        # Retornamos el estilo en "Negrita", el color del texto en blanco y color de fondo según el tipo de mensaje
        return ["bold", f'fg_white2', f'bg_{color}']


# Función que retorna el código del Texto con los estilos aplicados según su formato
def print_message(text, msg_format=None, message_data=None):
    # Si el mensaje tiene el icono inicialmente
    if msg_format == "ico":
        # Retornamos el texto con el icono inicialmente y el color del texto según el tipo de mensaje
        return add_text_styles(f'{message_data["ico_code"]} {text}', create_arg(message_data['color'], msg_format))

    # Si el mensaje es de tipo botón
    elif msg_format == "btn":
        # Retornamos el color del texto y del fondo según el tipo de mensaje
        return add_text_styles(text, create_arg(message_data['color'], msg_format))

    # Si el mensaje es de tipo botón y con el icono inicialmente
    elif msg_format == "btn_ico":
        # Retornamos el icono inicialmente y el color del texto y del fondo según el tipo de mensaje
        return add_text_styles(f' {message_data["ico_code"]} {text} ', create_arg(message_data['color'], msg_format))

    # Si el mensaje es solamente de tipo texto, retornamos el color del texto según el tipo de mensaje
    return add_text_styles(text, create_arg(message_data['color'], msg_format))
