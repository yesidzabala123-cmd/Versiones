# Sistema de Votación Integral (Resumen Funcional)

## 📌 ¿Para qué se hizo este sistema?
Diseñado para **administrar votaciones electrónicas seguras desde la terminal**, este programa unifica el control de identidad por documento de identidad, la persistencia en disco de los sufragios, el reporte analítico por porcentajes y la proclamación de resultados finales (ganador único o empates).

---

## ⚙️ ¿Cómo opera el flujo de trabajo?


### Parte realizada por Michael Usme

1. **Restauración de historial (`votos.txt`)**: 
   * Al iniciar, el sistema revisa si existe un archivo de respaldo con registros previos.
   * Si lo encuentra, carga automáticamente los documentos y votos pasados en memoria para evitar que alguien vote dos veces entre diferentes ejecuciones.

### Parte realizada por Jose Mendoza

2. **Captura y validación interactiva**:
   * Solicita el número de documento del votante.
   * Si escribes `"salir"`, el ciclo de votación se detiene y avanza a la muestra de resultados.
   * Valida en tiempo real si el documento ya está registrado; de ser así, rechaza el nuevo voto.
   * Si es válido, pide la opción de voto, la almacena en el diccionario de la sesión actual y la escribe de manera inmediata en el archivo `votos.txt`.

### Parte realizada por Yesid Fonseca

3. **Análisis y reporte de resultados (`ver_resultados`)**:
   * Cuenta cuántos votos acumuló cada opción usando contadores especializados.
   * Calcula de forma proporcional el porcentaje exacto que representa cada opción frente al total de votos emitidos (protegiendo contra divisiones por cero si no hubiera participación).

### Parte realizada por Michael Usme

4. **Proclamación oficial**:
   * Compara los totales para identificar la opción con la mayor cantidad de votos.
   * Anuncia al **ganador absoluto** con su respectivo conteo, o bien, declara un **empate** si dos o más opciones alcanzan la máxima puntuación idéntica.