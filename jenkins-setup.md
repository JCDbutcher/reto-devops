
#  Configuración de Jenkins para Desencadenar un Job ante Cambios en Git

Este documento describe los pasos necesarios para configurar correctamente un **Job de Jenkins** y el **repositorio Git** de manera que la ejecución se dispare automáticamente cuando se detecten cambios en el repositorio.

---

##  Requisitos Previos

- Jenkins instalado y accesible vía navegador.
- Jenkins debe tener el plugin **Git**,**Pipeline**,**Docker** y **Docker Pipeline** instalados.
- El repositorio de Git (por ejemplo en GitHub) debe estar accesible desde Jenkins.
- Acceso a un **Personal Access Token (PAT)** de GitHub o credenciales SSH configuradas en Jenkins.

---

## 1.  Configuración en el Repositorio Git

### a. Agrega un `Jenkinsfile`

Este archivo contiene la definición del pipeline. Debe estar ubicado en la raíz del repositorio.

```bash
# Ejemplo en tu proyecto
repo/
├── Jenkinsfile
├── app/
└── requirements.txt
```

Ejemplo de contenido básico:

```groovy
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Construyendo...'
            }
        }
    }
}
```

---

## 2.  Configuración del Job en Jenkins

### a. Crear un nuevo Job de tipo "Pipeline"

1. Entra a Jenkins.
2. Haz clic en **New Item**.
3. Escribe un nombre, selecciona **Pipeline** y clic en **OK**.

### b. Configurar fuente de Git

En la sección **Pipeline**:
- Marca **Pipeline script from SCM**.
- En **SCM**, elige `Git`.
- Introduce la **URL del repositorio**, por ejemplo:
  ```
  https://github.com/usuario/mi-repo.git
  ```
- Si es privado, selecciona las credenciales configuradas.

---

## 3.  Habilitar Construcción Automática por Webhook (no probado solo en teoria)

### a. Activar opción en Jenkins

- En el Job, ve a **Configuración**.
- Marca la opción:  
  **Build Triggers > GitHub hook trigger for GITScm polling**

Esto permite que Jenkins reaccione a notificaciones desde GitHub.

### b. Configurar Webhook en GitHub

1. Ve al repositorio → **Settings** → **Webhooks**.
2. Clic en **Add webhook**.
3. Introduce la URL de Jenkins (ejemplo):

   ```
   http://servidor-jenkins:8080/github-webhook/
   ```

4. Content type: `application/json`.
5. Evento: **Just the push event**.
6. Guardar.

> **Nota:** Jenkins debe ser accesible desde internet si GitHub necesita enviarle notificaciones.

---

##  Resultado Esperado

Cada vez que hagas `git push` al repositorio, GitHub notificará a Jenkins mediante el Webhook. Jenkins ejecutará el pipeline definido en el `Jenkinsfile`.
