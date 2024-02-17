#include <iostream>
#include <cctype> // Para usar la función toupper
#include <stdlib.h> // Para usar system("color F1")

using namespace std;

class TurbinaControl {
private:
    bool tanquePocaAgua;
    bool cisternaPocaAgua;
    bool turbinaEncendida;
    bool tanqueLleno;

public:
    // Constructor de la clase TurbinaControl
    TurbinaControl();

    // Método para pedir datos al usuario
    void pedirDatos();

    // Método para controlar la turbina según los datos ingresados
    void controlTurbina();
};

// Implementación del constructor de la clase TurbinaControl
TurbinaControl::TurbinaControl() : tanquePocaAgua(false), cisternaPocaAgua(false), turbinaEncendida(false), tanqueLleno(false) {}

// Implementación del método para solicitar datos al usuario
void TurbinaControl::pedirDatos() {
    char input;
    // Solicitar si el tanque tiene poca agua
    do {
        cout << "\nEl tanque tiene poca agua? (S/N): ";
        cin >> input;
        input = toupper(input);
    } while (input != 'S' && input != 'N');
    tanquePocaAgua = (input == 'S');

    // Solicitar si la cisterna tiene poca agua
    do {
        cout << "La cisterna tiene poca agua? (S/N): ";
        cin >> input;
        input = toupper(input);
    } while (input != 'S' && input != 'N');
    cisternaPocaAgua = (input == 'S');

    // Solicitar si la turbina está encendida
    do {
        cout << "Esta la turbina encendida? (S/N): ";
        cin >> input;
        input = toupper(input);
    } while (input != 'S' && input != 'N');
    turbinaEncendida = (input == 'S');

    // Solicitar si el tanque está lleno
    do {
        cout << "Esta el tanque lleno? (S/N): ";
        cin >> input;
        input = toupper(input);
    } while (input != 'S' && input != 'N');
    tanqueLleno = (input == 'S');
}

// Implementación del método para controlar la turbina según los datos ingresados
void TurbinaControl::controlTurbina() {
    // Determinar si la turbina debe apagarse o encenderse según las condiciones
    if (cisternaPocaAgua && turbinaEncendida) {
        cout << "\nLa turbina debe apagarse." << endl;
    } else if (turbinaEncendida && tanqueLleno) {
        cout << "\nLa turbina debe apagarse." << endl;
    } else if (tanquePocaAgua && !cisternaPocaAgua && !turbinaEncendida) {
        cout << "\nLa turbina debe encenderse." << endl;
    } else {
        cout << "\nNo se requiere ninguna accion." << endl;
    }
}

int main() {
    system("color F1"); // Cambiar el color de la consola a blanco sobre fondo azul claro
    cout << "\tPROGRAMA DE CONTROL DE UNA TURBINA" << endl;
    TurbinaControl control;
    control.pedirDatos();
    control.controlTurbina();

    return 0;
}

