// C++ лаба 15.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <string>
#include <fstream>
#include <cmath>

using namespace std;

class Chisla
{
public:
    
    int max(double a, double b)
    {
        if (a > b) return a; else return b;
    }
    int fun(double a, double b)
    {
        return b + max(a, b) + max(10, b) / 2;
    }
};
class Cylinder 
{
public:
    double radius;
    double height;
    double osnovArea; 
    double objem; 

public:
    Cylinder(double r, double h) {
        radius = r;
        height = h;
        calculateosnovArea();
        calculateVolume();
    }
    void calculateosnovArea() {
        osnovArea = 3.14 * pow(radius, 2);
    }

    void calculateVolume() {
        objem = osnovArea * height;
    }

    void printInfo() {
        cout << "Радиус основания: " << radius << endl;
        cout << "Высота: " << height << endl;
        cout << "Площадь основания: " << osnovArea << endl;
        cout << "Объем: " << objem << endl;
    }
};
class ZamenaBukv
{ 
public:
    string st(string slovo, char simvol)
    {
        for (size_t i = 0; i < slovo.length(); ++i) {
            if (slovo[i] == simvol) {
                slovo[i] = '*';
            }
        }
        return slovo;
    }
};

int main()
{
    setlocale(LC_ALL, "Rus");
    cout << "Вариант 3. Задание 1\n" << endl;

    double a, b;

    cout << "Введите a: ";
    cin >> a;
    cout << "Введите b: ";
    cin >> b;

    Chisla chisla;
    cout <<"Максимальное число: " << chisla.max(a, b) << endl;
    cout <<"Возвращаемое значение: " << chisla.fun(a, b) << endl;

    cout << "\nЗадание 2\n"<<endl;


    Cylinder cylinder(5, 10);
    cylinder.printInfo();

    cout << "Задание 2\n" << endl;

    string slovo;
    char simvol;

    cout << "Введите слово: ";
    cin >> slovo;
    cout << "Введите символ для замены на *: ";
    cin >> simvol;

    ZamenaBukv oldslovo;
    cout << "Результат:  " << oldslovo.st(slovo, simvol) << endl;

    return 0;



}

// Запуск программы: CTRL+F5 или меню "Отладка" > "Запуск без отладки"
// Отладка программы: F5 или меню "Отладка" > "Запустить отладку"

// Советы по началу работы 
//   1. В окне обозревателя решений можно добавлять файлы и управлять ими.
//   2. В окне Team Explorer можно подключиться к системе управления версиями.
//   3. В окне "Выходные данные" можно просматривать выходные данные сборки и другие сообщения.
//   4. В окне "Список ошибок" можно просматривать ошибки.
//   5. Последовательно выберите пункты меню "Проект" > "Добавить новый элемент", чтобы создать файлы кода, или "Проект" > "Добавить существующий элемент", чтобы добавить в проект существующие файлы кода.
//   6. Чтобы снова открыть этот проект позже, выберите пункты меню "Файл" > "Открыть" > "Проект" и выберите SLN-файл.
