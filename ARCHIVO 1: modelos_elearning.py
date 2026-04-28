"""
📊 MODELOS DE DATOS PARA E-LEARNING
Define la estructura de todas las entidades
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict
from enum import Enum


class Nivel(Enum):
    """Niveles de estudiante"""
    PRINCIPIANTE = "PRINCIPIANTE"
    INTERMEDIO = "INTERMEDIO"
    AVANZADO = "AVANZADO"


class EstiloAprendizaje(Enum):
    """Estilos de aprendizaje"""
    VISUAL = "VISUAL"
    LECTURA = "LECTURA"
    PRÁCTICA = "PRÁCTICA"


class TipoContenido(Enum):
    """Tipos de contenido"""
    VIDEO = "VIDEO"
    LECTURA = "LECTURA"
    PRÁCTICA = "PRÁCTICA"
    EJERCICIO = "EJERCICIO"


class Dificultad(Enum):
    """Niveles de dificultad"""
    FÁCIL = "FÁCIL"
    MEDIO = "MEDIO"
    DIFÍCIL = "DIFÍCIL"


@dataclass
class Estudiante:
    """Representa un estudiante"""
    id_estudiante: Optional[int] = None
    nombre: str = "Diego Mercedes Llauger"
    matricula: str = "2026-0048"
    carrera: str = "Ingeniería en Ciberseguridad"
    nivel_inicial: Nivel = Nivel.PRINCIPIANTE
    estilo_aprendizaje: EstiloAprendizaje = EstiloAprendizaje.PRÁCTICA
    horas_disponibles_semana: int = 10
    fortalezas: List[str] = field(default_factory=list)
    debilidades: List[str] = field(default_factory=list)
    metas: List[str] = field(default_factory=list)
    fecha_registro: datetime = field(default_factory=datetime.now)
    
    def to_dict(self):
        return {
            "id": self.id_estudiante,
            "nombre": self.nombre,
            "matricula": self.matricula,
            "nivel": self.nivel_inicial.value,
            "estilo": self.estilo_aprendizaje.value,
            "horas_semana": self.horas_disponibles_semana,
            "fortalezas": self.fortalezas,
            "debilidades": self.debilidades,
            "metas": self.metas
        }


@dataclass
class Curso:
    """Representa un curso/tema"""
    id_curso: Optional[int] = None
    nombre: str = ""
    descripcion: str = ""
    nivel_minimo: Nivel = Nivel.PRINCIPIANTE
    duracion_estimada: int = 40  # horas
    
    def to_dict(self):
        return {
            "id": self.id_curso,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "nivel_minimo": self.nivel_minimo.value,
            "duracion": self.duracion_estimada
        }


@dataclass
class Modulo:
    """Representa un módulo dentro de un curso"""
    id_modulo: Optional[int] = None
    id_curso: int = 0
    nombre: str = ""
    descripcion: str = ""
    orden_secuencia: int = 1
    duracion_estimada: int = 5  # horas
    prerequisitos: List[int] = field(default_factory=list)
    
    def to_dict(self):
        return {
            "id": self.id_modulo,
            "nombre": self.nombre,
            "orden": self.orden_secuencia,
            "duracion": self.duracion_estimada,
            "prerequisitos": self.prerequisitos
        }


@dataclass
class Contenido:
    """Representa un recurso educativo"""
    id_contenido: Optional[int] = None
    id_modulo: int = 0
    titulo: str = ""
    tipo: TipoContenido = TipoContenido.VIDEO
    url: str = ""
    duracion_minutos: int = 15
    nivel_dificultad: Dificultad = Dificultad.FÁCIL
    estilo_aprendizaje_enfoque: EstiloAprendizaje = EstiloAprendizaje.VISUAL
    
    def to_dict(self):
        return {
            "id": self.id_contenido,
            "titulo": self.titulo,
            "tipo": self.tipo.value,
            "duracion": self.duracion_minutos,
            "dificultad": self.nivel_dificultad.value
        }


@dataclass
class RutaPersonalizada:
    """Ruta de aprendizaje personalizada para estudiante"""
    id_ruta: Optional[int] = None
    id_estudiante: int = 0
    id_curso: int = 0
    modulos_ordenados: List[int] = field(default_factory=list)
    razon_orden: Dict[int, str] = field(default_factory=dict)  # Por qué cada módulo en ese orden
    fecha_creacion: datetime = field(default_factory=datetime.now)
    fecha_estimada_fin: Optional[datetime] = None
    
    def to_dict(self):
        return {
            "id": self.id_ruta,
            "modulos": self.modulos_ordenados,
            "fecha_fin_estimada": self.fecha_estimada_fin.isoformat() if self.fecha_estimada_fin else None
        }


@dataclass
class Quiz:
    """Pregunta generada automáticamente"""
    id_quiz: Optional[int] = None
    id_modulo: int = 0
    id_contenido: int = 0
    pregunta: str = ""
    tipo: str = "OPCION_MULTIPLE"  # OPCION_MULTIPLE, VERDADERO_FALSO, RELLENAR
    opciones: List[str] = field(default_factory=list)
    respuesta_correcta: str = ""
    explicacion: str = ""
    dificultad: Dificultad = Dificultad.FÁCIL
    tiempo_limite: int = 30  # segundos
    
    def to_dict(self):
        return {
            "id": self.id_quiz,
            "pregunta": self.pregunta,
            "tipo": self.tipo,
            "opciones": self.opciones,
            "dificultad": self.dificultad.value
        }


@dataclass
class Respuesta:
    """Respuesta de un estudiante a un quiz"""
    id_respuesta: Optional[int] = None
    id_estudiante: int = 0
    id_quiz: int = 0
    respuesta_dada: str = ""
    es_correcta: bool = False
    tiempo_respuesta: int = 0  # segundos
    fecha_respuesta: datetime = field(default_factory=datetime.now)
    
    def to_dict(self):
        return {
            "id": self.id_respuesta,
            "respuesta": self.respuesta_dada,
            "es_correcta": self.es_correcta,
            "tiempo": self.tiempo_respuesta
        }


@dataclass
class AnalisisDesempeño:
    """Análisis del desempeño de un estudiante"""
    id_analisis: Optional[int] = None
    id_estudiante: int = 0
    id_modulo: int = 0
    puntuacion_promedio: float = 0.0
    conceptos_entendidos: List[str] = field(default_factory=list)
    conceptos_no_entendidos: List[str] = field(default_factory=list)
    retroalimentacion: Dict[int, str] = field(default_factory=dict)  # id_quiz -> feedback
    recomendaciones: List[str] = field(default_factory=list)
    fecha_analisis: datetime = field(default_factory=datetime.now)
    
    def to_dict(self):
        return {
            "id": self.id_analisis,
            "puntuacion": self.puntuacion_promedio,
            "entendidos": self.conceptos_entendidos,
            "no_entendidos": self.conceptos_no_entendidos,
            "recomendaciones": self.recomendaciones
        }


@dataclass
class Prediccion:
    """Predicción de nota final"""
    id_prediccion: Optional[int] = None
    id_estudiante: int = 0
    id_curso: int = 0
    nota_predicha: float = 0.0
    confianza: float = 0.0  # 0-1
    temas_criticos: List[str] = field(default_factory=list)
    plan_final: List[str] = field(default_factory=list)
    veredicto: str = ""  # PROBABLEMENTE APRUEBES, EN RIESGO, DEBES ESTUDIAR MÁS
    fecha_prediccion: datetime = field(default_factory=datetime.now)
    
    def to_dict(self):
        return {
            "id": self.id_prediccion,
            "nota_predicha": self.nota_predicha,
            "confianza": self.confianza,
            "veredicto": self.veredicto,
            "temas_criticos": self.temas_criticos,
            "plan": self.plan_final
        }
