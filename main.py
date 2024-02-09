"""
Probar el paquete "outputstyles".
"""

from outputstyles import error, warning, info, success, bold

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
            '->',
            f'{func_name}("{msg_text}")'
        )

        # Recorrer las opciones para imprimir sus variantes de formatos.
        for msg_format in format_options:

            # Si es la función de Bold, rompemos el ciclo
            # porque esta no tiene diferentes formatos.
            if func_name == "bold":
                break

            # Imprimir cada tipo de opción (btn, ico, btn_ico).
            print(
                func_type_msg(msg_text, msg_format),
                '->',
                f'{func_name}("{msg_text}", "{msg_format}")'
            )

        # Dejar un espacio entre cada bloque de tipo de mensajes.
        print("")


# Imprimir todos los tipos de mensajes con todas sus variantes.
print(info("Ejemplos del resultado final y como usarlo:\n"))
print_all_messages(func_style_names, format_options)
