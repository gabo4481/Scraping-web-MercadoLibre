from controllers.scraping_controller import Scraping_controller
from controllers.DB_controller import DB_controller
from controllers.pdf_controller import PDF_controller
import dearpygui.dearpygui as dpg

controller_DB = DB_controller()
controller_scraping = Scraping_controller()
controller_pdf = PDF_controller()


#Funciones 
def eliminar_todo():
    controller_DB.eliminar_todos_registros()
    controller_DB.restaurar_secuencias()
    actualizar_productos(controller_DB.obtener_registros())
    dpg.set_value("numero_registros",controller_DB.conteo_registros())
    
def realizar_scraping():
    cantidad = dpg.get_value("cantidad_registros")
    registros=controller_scraping.obtener_valores(cantidad)
    controller_DB.guardar_registros(registros)
    dpg.set_value("numero_raspados",f"Registros raspados: {len(registros)} ")
    dpg.set_value("numero_registros",f"Total registros: {controller_DB.conteo_registros()}")
    actualizar_productos(controller_DB.obtener_registros())
    
def actualizar_productos(registros):
    # Verifica y elimina la tabla previa si existe
    if dpg.does_item_exist("tabla_registros"):
        dpg.delete_item("tabla_registros")

    # Crea la tabla con política proporcional
    with dpg.table(header_row=True, parent="contenedor_tabla", tag="tabla_registros", resizable=True, policy=dpg.mvTable_SizingStretchProp):
        # Define las columnas con proporciones específicas
        dpg.add_table_column(label="ID", init_width_or_weight=1)  # Peso proporcional
        dpg.add_table_column(label="Descripcion", init_width_or_weight=3)  # Descripción toma más espacio
        dpg.add_table_column(label="Precio", init_width_or_weight=1)  # Precio toma espacio moderado
        dpg.add_table_column(label="Acciones", init_width_or_weight=1)  # Acciones menor espacio

        # Rellenar filas con registros
        for registro in registros:
            with dpg.table_row():
                dpg.add_text(registro[0])  # ID
                dpg.add_text(registro[1])  # Descripción
                dpg.add_text(registro[2])  # Precio
                with dpg.group(horizontal=True):
                    dpg.add_button(label="Eliminar", callback=create_eliminar_callback(registro[0]),width=80,height=30)
                    dpg.bind_item_theme(dpg.last_item(), "tema_boton_rojo")


                    
def create_eliminar_callback(registro_id):
    def eliminar_producto():
        controller_DB.elminar_registro(registro_id)
        actualizar_productos(controller_DB.obtener_registros())
        print(f"Eliminando registro para ID: {registro_id}")
        dpg.set_value("numero_registros",controller_DB.conteo_registros())
    return eliminar_producto


#Interfaz Grafica

dpg.create_context()
#temas botones
with dpg.theme(tag="tema_boton_rojo"):
            with dpg.theme_component(dpg.mvButton):
                dpg.add_theme_color(dpg.mvThemeCol_Button,(255, 0, 0, 128))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive,(255, 0, 0,50))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (255, 0, 0, 255))
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 24)
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 3, 3)
                dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 8, 8)  # gap
                dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign, 0.5, 0.5 )
                with dpg.theme(tag="tema_boton_azul"):
                    with dpg.theme_component(dpg.mvButton):
                        dpg.add_theme_color(dpg.mvThemeCol_Button, (10, 56, 113) )  # background-color
                        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (138, 43, 226) )  # hover background-color
                        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (138, 43, 226) )  # active background-color
                        dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255) )  # color
                        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 24 )  # border-radius
                        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 3,3)  # padding
                        dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 8, 8)  # gap
                        dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign, 0.5, 0.5 )  # text-align
                    with dpg.theme(tag="tema_boton_blanco"):
                        with dpg.theme_component(dpg.mvButton):
                            dpg.add_theme_color(dpg.mvThemeCol_Button, (216, 223, 232))  # background-color
                            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (138, 43, 226))  # hover background-color
                            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (138, 43, 226))  # active background-color
                            dpg.add_theme_color(dpg.mvThemeCol_Text, (10, 56, 113))  # color
                            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 24)  # border-radius
                            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 3, 3)  # padding
                            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 8, 8)  # gap
                            dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign, 0.5, 0.5)  #
                            
                            
with dpg.window(label="Gestor de productos",tag="principal", width=1350, height=700):
    dpg.add_separator(label="Ingresa la cantidad de registros a buscar")
    with dpg.group(indent=20,horizontal=True,horizontal_spacing=100):
        dpg.add_input_int(tag="cantidad_registros")
        dpg.add_button(label="Buscar",callback=realizar_scraping,width=200,height=30)
        dpg.bind_item_theme(dpg.last_item(), "tema_boton_azul")
    
    dpg.add_separator(label="Estadisticas")
    with dpg.group(indent=20,horizontal=True,horizontal_spacing=100):
        dpg.add_text(tag="numero_raspados",default_value=f"Registros raspados: 0 ")
        dpg.add_text(tag="numero_registros",default_value=f"Total registros: {controller_DB.conteo_registros()}")
        dpg.add_button(label="Mostrar Mejores precios",callback=lambda: actualizar_productos(controller_DB.obtener_primeros_10()),width=200,height=30)
        dpg.bind_item_theme(dpg.last_item(), "tema_boton_azul")
        
    dpg.add_separator(label="Funciones")
    with dpg.group(indent=20,horizontal=True,horizontal_spacing=100):
        dpg.add_button(label="Eliminar Todo", callback=eliminar_todo, width=200, height=30)
        dpg.bind_item_theme(dpg.last_item(), "tema_boton_rojo")

        dpg.add_button(label="Ordenar por Descripcion", width=200, height=30, callback=lambda: actualizar_productos(controller_DB.registros_ordenados_descripcion()))
        dpg.bind_item_theme(dpg.last_item(), "tema_boton_blanco")

        dpg.add_button(label="Ordenar por precio", width=200, height=30, callback=lambda: actualizar_productos(controller_DB.registros_ordenados_precio()))
        dpg.bind_item_theme(dpg.last_item(), "tema_boton_blanco")
        
        dpg.add_button(label="Generar Reporte",width=200, height=30,callback=lambda: controller_pdf.generar_pdf(controller_DB.obtener_registros()))
        dpg.bind_item_theme(dpg.last_item(), "tema_boton_rojo")
    
    dpg.add_separator(label="Registros")
    with dpg.group(indent=20,tag="contenedor_tabla"):
        actualizar_productos(controller_DB.obtener_registros())
            
dpg.create_viewport(title="Scraping Mercado Libre Computacion",resizable=True,x_pos=0,y_pos=0)
dpg.setup_dearpygui()
dpg.maximize_viewport()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


