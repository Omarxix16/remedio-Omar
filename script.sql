script.sql
CREATE TABLE tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL
);

INSERT INTO tareas (descripcion) VALUES ("Comprar comida");
INSERT INTO tareas (descripcion) VALUES ("Hacer tarea");
INSERT INTO tareas (descripcion) VALUES ("Ir al gimnasio");
