import psycopg
class DB_controller():
    def conectar(self):
        try:
            conexion = psycopg.connect(
                host = "localhost",
                dbname = "web_scraping",
                user = "postgres",
                password = "gabo4481"
            )
            print("Conexion Exitosa.")
            return conexion
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None
        
    def obtener_registros(self):
        conexion = self.conectar()
        if conexion:
            try:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        """SELECT * FROM productos"""
                    )
                    registros = cursor.fetchall()
            except psycopg.Error as e:
                print(f"Error al intente leer los productos: {e}")
            finally:
                conexion.close()
                return registros
    
    def guardar_registros(self,registros):
        conexion = self.conectar()
        if conexion:
            try:
                with conexion.cursor() as cursor:
                    for registro in registros:
                        cursor.execute(
                            """INSERT INTO productos (descripcion,precio)
                            VALUES (%s,%s)""",(registro["descripcion"],registro["precio"])
                        )
                    conexion.commit()
            except psycopg.Error as e:
                print(f"Error al intentara guardar el registro: {e} ")
            finally:
                conexion.close()
    
    def elminar_registro(self,id):
        conexion = self.conectar()
        if conexion:
            try:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        """ DELETE FROM productos where id =%s """,(id,)
                    )
                    conexion.commit()
                    if cursor.rowcount > 0:
                        print("Registro borrado exitosamnete.")
                    else:
                        print(f"No se encontro un registro con el id {id}")
            except psycopg.Error as e:
                print(f"Error al intentar borrar el registro: {e}")
            finally:
                conexion.close()
    
    def eliminar_todos_registros(self):
        conexion = self.conectar()
        if conexion:
            try:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        """ DELETE FROM productos """
                    )
                    conexion.commit()
                    if cursor.rowcount > 0:
                        print("Registros borrado exitosamnete.")
                    else:
                        print(f"Sin registros.")
            except psycopg.Error as e:
                print(f"Error al intentar borrar los registros: {e}")
            finally:
                conexion.close()
    
    def obtener_primeros_10(self):
        conexion = self.conectar()
        if conexion:
            try:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        """SELECT * FROM productos order by precio limit 10"""
                    )
                    registros = cursor.fetchall()
            except psycopg.Error as e:
                print(f"Error al intente leer los productos: {e}")
            finally:
                conexion.close()
                return registros
    
    
    def registros_ordenados_descripcion(self):
        conexion = self.conectar()
        if conexion:
            try:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        """SELECT * FROM productos order by descripcion"""
                    )
                    registros = cursor.fetchall()
            except psycopg.Error as e:
                print(f"Error al intente leer los productos: {e}")
            finally:
                conexion.close()
                return registros
    
    def registros_ordenados_precio(self):
        conexion = self.conectar()
        if conexion:
            try:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        """SELECT * FROM productos order by precio"""
                    )
                    registros = cursor.fetchall()
            except psycopg.Error as e:
                print(f"Error al intente leer los productos: {e}")
            finally:
                conexion.close()
                return registros
    
    
    def conteo_registros(self):
        conexion = self.conectar()
        if conexion:
            try:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        """ SELECT COUNT(*) FROM productos """
                    )
                    total_registro = cursor.fetchone()
            except psycopg.Error as e:
                print(f"Error al intentar obetner el conteo de los registros: {e}")
            finally:
                conexion.close()
                return total_registro[0]
            
    def restaurar_secuencias(self):
        conexion = self.conectar()
        if conexion:
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("ALTER SEQUENCE productos_id_seq RESTART WITH 1;")
                    conexion.commit()
            except psycopg.Error as e:
                print(f"Error al intentar obetner el conteo de los registros: {e}")
            finally:
                conexion.close()
        