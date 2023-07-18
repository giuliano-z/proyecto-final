# Oceano de libros

## Descripción
Oceano de libros es una librería digital que te permite ver libros en línea. ¡Sumérgete en un vasto océano de conocimiento y disfruta de una amplia selección de títulos disponibles!

## Características
- Búsqueda avanzada para encontrar libros por título, autor o género.
- Catálogo en constante crecimiento con una amplia variedad de géneros literarios.
- Reseñas y valoraciones de libros realizadas por la comunidad.
- Opción de añadir libros a tu lista de deseos para futuras compras.

## Instalación
Puedes instalar Oceano de libros siguiendo estos pasos:

1. Clona el repositorio desde GitHub: git clone https://github.com/tu_usuario/oceano-de-libros.git
2. Accede al directorio del proyecto: cd oceano-de-libros
3. Instala las dependencias: npm start

## Uso
Una vez que hayas instalado Oceano de libros, puedes utilizarlo de la siguiente manera:

1. Abre tu navegador web y accede a la siguiente dirección: `http://127.0.0.1:8000/`.
2. Explora el catálogo de libros utilizando la barra de búsqueda.
3. Haz clic en un libro para ver más detalles, como su descripción y porpietario.
4. ¡Disfruta de tus nuevos libros!

También puedes ver un video de demostración que muestra cómo funciona la página en acción: [Video de demostración de Oceano de libros](https://youtu.be/sJUvWGhBJb0). Este video te guiará a través de los pasos mencionados anteriormente y te mostrará cómo utilizar la plataforma de manera efectiva.

## Estado del proyecto
Actualmente, Oceano de libros se encuentra en desarrollo. Estamos trabajando arduamente para mejorar la plataforma y añadir nuevas funcionalidades. Mantente atento a las actualizaciones futuras.

## Autor
- Giuliano Daniel Zulatto

## Contacto
Si tienes alguna pregunta, sugerencia o comentario sobre Oceano de libros, no dudes en ponerte en contacto conmigo:
- Correo electrónico: giulianodanielzulatto@gmail.com

## Desarrollando
- Reseñas y valoraciones de libros realizadas por la comunidad.
- Opción de añadir libros a tu lista de deseos para futuras compras.
- Opcion de añadir libro a el carrito de compras.

## Estructura del código

A continuación se muestra una parte del código fuente del proyecto:

### Modelo de Libro

```python
class Libro(models.Model):
 titulo = models.CharField(max_length=50)
 autor = models.CharField(max_length=50)
 editorial = models.CharField(max_length=50)
 precio = models.DecimalField(max_digits=10, decimal_places=2, null=True)
 descripcion = models.TextField(null=True)
 imagen = models.ImageField(upload_to='fotos/', null=True, blank=True)

 def __str__(self):
     return f"Libro: {self.titulo} - Autor: {self.autor} - Precio {self.precio} - Editorial: {self.editorial}"
