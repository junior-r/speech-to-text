# Script de python para convertir archivos de audio a texto

## Requisitos
- Tener instalado Python 3.10
- Tener instalado virtualenv
```bash
pip install virtualenv
```

## Instalación
1. Clonar el repositorio
```bash
git clone https://github.com/junior-r/speech-to-text.git
```
2. Crear un entorno virtual
```bash
virtualenv venv --python=python3.10
```
3. Activar el entorno virtual
```bash
# Windows
.\venv\Scripts\activate
# Linux y Mac
source venv/bin/activate
```
4. Instalar las dependencias
```bash
pip install -r requirements.txt
```
3. Instalar FFmpeg en el sistema.
### En Windows.
1. Descargar el ejecutable de FFmpeg desde [aquí](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z).
2. Descomprimir el archivo descargado.
3. Renombrar la carpeta descomprimida a `ffmpeg`.
4. Agregar la ruta de la carpeta `ffmpeg` al PATH del sistema.
5. Reiniciar el sistema.

Para los pasos 1 y 2 se puede utilizar el [ejemplo](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/) de la página de GeeksforGeeks.
Para los pasos 3 y 4 se puede utilizar el [ejemplo](https://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/) de la página de Greg Zaal.

6. Comprobar que la instalación fue exitosa.
```bash
ffmpeg -codecs
```

### En Linux.
```bash
sudo apt-get install ffmpeg
```

### API de Google Cloud
#### Para este proceso se necesita una cuenta de Google Cloud y un proyecto con la API de Speech-to-Text habilitada.
#### Siguiendo los pasos de la [documentación](https://cloud.google.com/speech-to-text/docs/before-you-begin?hl=es-419) de Google Cloud (Hasta el paso 5) se puede obtener el archivo JSON con las credenciales necesarias para la autenticación.
#### Luego de descargar el archivo JSON con las credenciales, se debe guardar en la raíz del proyecto.

## Configuración
1. Crear un archivo `.env` en la raíz del proyecto.
2. Agregar las siguientes variables de entorno al archivo `.env`.
```env
GOOGLE_APPLICATION_CREDENTIALS=nombre_del_archivo.json
AUDIO_NAME=nombre_del_archivo
AUDIO_EXTENSION=extensión_del_archivo
AUDIO_LANGUAGE=lenguaje_del_audio (es-ES, en-US, etc.)
```
3. Guardar el archivo `.env`.

## Estructura de archivos inicial
```plaintext
.
├── venv
├── .env
├── .gitignore
├── audio.mp3
├── main.py
├── README.md
├── requirements.txt
├── nombre_del_archivo_credenciales.json
```

## Estructura de archivos final
Luego de correr el script, se generará un archivo de texto con el contenido del audio.
```plaintext
.
├── venv
├── .env
├── .gitignore
├── audio.mp3
├── audio.wav
├── main.py
├── output.txt
├── README.md
├── requirements.txt
├── nombre_del_archivo_credenciales.json
```


## Uso
```bash
python main.py
```
