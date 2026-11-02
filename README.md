Grupo 15 Trabajo Práctico de ISI 
Integrantes: 
Castillo, Marcos
Caviedes, Francisco
Monsalvo, Lucas


Plataforma de Preguntas y Respuestas (Q&A)

Este proyecto es el diseño en UML de una plataforma donde los estudiantes hacen preguntas y reciben respuestas, ya sea de otros usuarios o de una inteligencia artificial. Acá explicamos cómo lo armamos y por qué.

Cómo está armado el sistema

Preguntas y respuestas: un usuario hace una pregunta con título, texto y fecha. Cada pregunta tiene una sola categoría (por ejemplo Python o Flask) y puede tener varias etiquetas. Una pregunta puede recibir muchas respuestas, y cada respuesta guarda su texto, su fecha y si fue marcada como aceptada.

Usuarios: hay dos tipos, UsuarioPromedio y Administrador. Los dos heredan de Usuario, que guarda el email y la contraseña.

Votos: los usuarios pueden votar de forma positiva o negativa tanto las preguntas como las respuestas.

Decisiones de diseño

Strategy (la IA y sus modelos): la IA puede usar distintos modelos, como Gemini, OpenAI o uno local. Para no tener que armar una clase distinta de agente por cada uno, creamos una interfaz llamada Strategy con un solo método: generarTexto(prompt). Cada modelo (Gemini, OpenAI y StrategyLocal) la implementa a su manera. AgenteIA guarda el modelo que está usando y lo puede cambiar cuando haga falta con setEstrategia. La ventaja es que si mañana queremos sumar otro modelo, solo creamos una clase nueva y no tocamos lo que ya funciona.

Autor (humanos e IA por igual): la consigna pedía que una respuesta pudiera venir de una persona o de la IA. Por eso creamos la clase abstracta Autor, de la que heredan Usuario y AgenteIA. La clase Respuesta se conecta con Autor y no con Usuario, así que no le importa quién la escribió. Las dos clases hijas tienen su propia versión de generarRespuesta.

Cuándo responde la IA: AgenteIA tiene una etiqueta que lo activa (por ejemplo #ia-help) y un método debeResponder(p). Con eso decide si una pregunta tiene esa etiqueta o si lleva mucho tiempo sin que nadie la conteste.
