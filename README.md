Grupo 15 Trabajo Práctico de ISI I
Integrantes: 
Castillo, Marcos
Caviedes, Francisco
Monsalvo, Lucas


Plataforma de Preguntas y Respuestas (Q&A)
Decisiones de diseño

Strategy (generación de respuestas con IA): AgenteIA no sabe cómo se genera el texto, solo le pide a su Strategy que lo haga. Gemini, OpenAI y StrategyLocal implementan esa interfaz con el mismo método, generarTexto(prompt), y el agente puede cambiar de proveedor en cualquier momento con setEstrategia. Si mañana se suma otro LLM, se crea una clase nueva y el resto del modelo queda igual.

Autoría polimórfica: Autor es una clase abstracta de la que heredan Usuario y AgenteIA. Respuesta está vinculada a Autor, por lo que no le importa si quien respondió es una persona o la IA. Cada subclase define a su manera cómo genera una respuesta.

Cuándo responde la IA: AgenteIA guarda una etiqueta de disparo (por ejemplo #ia-help) y el método debeResponder(p) indica si una pregunta la tiene o si lleva demasiado tiempo sin respuestas.
