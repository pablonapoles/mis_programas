% Programa para diagnóstico de reparación de un ventilador

% Las piezas del ventilador
pieza(motor).
pieza(pala).
pieza(aspa).
pieza(eje).

% Preguntas para determinar qué piezas están rotas
rotura(X) :- preguntar(X, 'La pieza ~w esta rota? [s/n]', R), R = s.

% Preguntas
preguntar(X, Texto, Res) :-
    nl, format(Texto, [X]),
    read(Respuesta),
    (Respuesta = 's'; Respuesta = 'n'),
    Res = Respuesta, !.

preguntar(X, Texto, Res) :-
    nl, format('Respuesta inválida para la pieza ~w. Por favor, responda con "s" o "n".', [X]),
    preguntar(X, Texto, Res).

% Diagnóstico
diagnostico(Reparacion) :-
    findall(Pieza, (pieza(Pieza), rotura(Pieza)), PiezasRotas),
    length(PiezasRotas, CantidadRotas),
    CantidadRotas >= 4,
    Reparacion = 'No se puede reparar el ventilador debido a la rotura de 4 piezas simultáneamente.', !.

diagnostico('El ventilador se puede reparar.').