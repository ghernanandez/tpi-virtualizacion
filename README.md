# Trabajo Integrador de Arquitectura y Sistemas Operativos
## Virtualización con VirtualBox y KVM

---

## 📖 Descripción del Proyecto

Este trabajo integrador tiene como objetivo investigar y aplicar conceptos relacionados con la virtualización mediante el uso de las tecnologías **VirtualBox** y **KVM (Kernel-based Virtual Machine)**.

Como parte de la implementación práctica, se desarrolló y ejecutó una aplicación en Python capaz de convertir números decimales a binarios dentro de un entorno virtualizado basado en Linux.

El proyecto contempla la instalación y configuración de máquinas virtuales, la administración de redes virtuales, la utilización de herramientas de gestión y la validación del funcionamiento de aplicaciones dentro de un entorno aislado.

---

## 🎯 Objetivos

- Comprender los fundamentos de la virtualización.
- Implementar máquinas virtuales utilizando VirtualBox y KVM.
- Configurar y administrar redes virtuales.
- Aplicar conceptos de administración de sistemas Linux.
- Ejecutar aplicaciones desarrolladas en Python dentro de entornos virtualizados.
- Documentar el proceso de implementación y los resultados obtenidos.

---

## 📂 Estructura del Repositorio

```text
.
├── conversor.py
├── Informe_tecnico.pdf
├── capturas/
│   ├── OVB-ubuntu/
│   └── KVM-ubuntu-server-26.04-LTS/
└── README.md
```

### Contenido

| Archivo / Carpeta | Descripción |
|------------------|-------------|
| `conversor.py` | Programa para convertir números decimales a binarios. |
| `Informe_tecnico.pdf` | Informe técnico completo del proyecto. |
| `capturas/` | Evidencias visuales del desarrollo y resultados. |
| `capturas/OVB-ubuntu/` | Capturas del proceso de instalación y configuración de la máquina virtual (Virtual Box). |
| `capturas/KVM-ubuntu-server-26.04-LTS/` | Capturas del proceso de instalación y configuración de la máquina virtual (KVM). |
| `README.md` | Documentación principal del repositorio. |

---

## ⚙️ Requisitos

- Python 3.x
- Git
- Ubuntu Server o Ubuntu Desktop
- VirtualBox o KVM/QEMU
- Virt-Manager (opcional para administración gráfica)

---

## 🚀 Instalación y Ejecución

### 1. Verificar las dependencias

```bash
python3 --version
git --version
```

### 2. Instalar dependencias

```bash
sudo apt update
sudo apt install python3 git -y
```

### 3. Clonar el repositorio

```bash
git clone git@github.com:ghernanandez/tpi-virtualizacion.git
```

### 4. Acceder al directorio

```bash
cd tpi-virtualizacion
```

### 5. Ejecutar la aplicación

```bash
python3 conversor.py
```

---

## 💻 Ejemplo de Uso

```text
---- CONVERSOR DE DECIMAL A BINARIO ----

Ingrese un número decimal: 13

El número 13 en binario es: 1101
```

---

## 🛠️ Tecnologías Utilizadas

### Virtualización

- VirtualBox
- KVM (Kernel-based Virtual Machine)
- QEMU
- Virt-Manager

### Desarrollo

- Python 3
- Git
- Ubuntu Server 26.04 LTS
- Ubuntu 26.04 LTS

---

## 🌐 Configuración de Red

- **NAT (Network Address Translation):** permite que la máquina virtual acceda a Internet utilizando la conexión del host.
- **Bridge (Adaptador Puente):** permite que la máquina virtual forme parte de la red local como un equipo independiente, obteniendo su propia dirección IP.

---

## 📊 Resultados Obtenidos

Se logró implementar correctamente un entorno virtualizado utilizando VirtualBox y KVM, configurar la conectividad de red necesaria para las pruebas y ejecutar satisfactoriamente una aplicación desarrollada en Python dentro de una máquina virtual Linux.

---

## 📚 Referencias

- Oracle. *Oracle VirtualBox User Manual*.
- ArchWiki. *KVM*.
- Red Hat. *What is a Hypervisor?*
- VMware. *What is a Hypervisor?*
- Chacon, S., & Straub, B. *Pro Git*.

---

## 👨‍💻 Autor

**Héctor Atilio Signoriello - Comisión 10**

**Gregorio Agustin Hernandez - Comisión 12**

Trabajo Integrador – Arquitectura y Sistemas Operativos


##  🔗 Link

[Video: ](https://youtube.com)
<https://youtube.com>
