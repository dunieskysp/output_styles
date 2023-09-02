from outputstyles.msg_print import error, warning, info, success, bold

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

    # Recorrer todas las funciones según su "Key" dentro del diccionario de funciones
    for func_name in dict_functions:
        # Obtener la función declarada del tipo de mensaje
        func_style = dict_functions[func_name]

        # Texto a imprimir es el nombre de la función en Mayúscula, más el simbolo "!"
        text_print = f'{func_name.capitalize()}!'

        # Si es la función de Bold, imprimimos sin opciones
        if func_name == "bold":
            # Ejecutamos la función con el texto y mostramos como se usa
            print(func_style(text_print), '-->',
                  f'{func_name}("{text_print}")')

        # Para los demás tipos de mensajes
        else:
            # Recorrer las opciones para los demás tipos de mensajes
            for option in list_options:
                # Si la opción está vacia (Solo el texto), imprimimos sin opciones
                if not option:
                    print(func_style(text_print),
                          '-->', f'{func_name}("{text_print}")')

                # Imprimir cada tipo de opción (btn, fig, btn_fig)
                else:
                    print(func_style(text_print, option), '-->',
                          f'{func_name}("{text_print}", "{option}")')

        # Dejar un espacio vacio cada vez que se finalice un bloque de tipo de mensajes
        print("")


# Imprimir todos los tipos de mensajes con todas sus variantes de formato
print(info("Ejemplos del resultado final y como usarlo:\n"))
print_all_messages(functions_styles, function_options)
