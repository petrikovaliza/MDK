// С++ лаба 16.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <string>

using namespace std;

class Grajdanin 
{
public:
    string name;
    int yearOfBirth;

public:
    Grajdanin(string new_name, int new_yearOfBirth)
    {
        name = new_name;
        yearOfBirth = new_yearOfBirth;
    }

    int getAge(int currentYear) 
    {
        return currentYear - yearOfBirth;
    }
};

class Woman : public Grajdanin 
{
public:
    Woman(string name, int yearOfBirth) : Grajdanin(name, yearOfBirth) {}

    int ExitPencia(int currentYear) 
    {
        return yearOfBirth + 60;
    }
};

class Man : public Grajdanin 
{
public:
    Man(string name, int yearOfBirth) : Grajdanin(name, yearOfBirth) {}

    int ExitPencia(int currentYear)
    {
        return yearOfBirth + 65;
    }

    void Armia(int currentYear) 
    {
        int startArmia = 18;
        int endArmia = 27;

        for (int i = yearOfBirth + startArmia; i <= yearOfBirth + endArmia && i <= currentYear; ++i)
        {
            cout << i << "\n";
        }
        cout << endl;
    }
};

int main() 
{
    setlocale(LC_ALL, "Rus");
    int currentYear = 2023;

    Woman marina("Марина", 1960);
    Man alexey("Алексей", 1988);

    int marinasAge = marina.getAge(currentYear);
    int alexeysAge = alexey.getAge(currentYear);

    int marinasExitPencia = marina.ExitPencia(currentYear);
    int alexeysExitPencia = alexey.ExitPencia(currentYear);

    cout << "Имя: "<< marina.name <<"\n";
    cout << "Возраст: " << marinasAge << "\n";
    cout << "Год выхода на пенсию: " << marinasExitPencia << "\n\n";

    cout << "Имя: " << alexey.name<< "\n";
    cout << "Возраст: " << alexeysAge << "\n";
    cout << "Год выхода на пенсию: " << alexeysExitPencia << "\n\n";

    cout << "Годы военной обязанности мужчины " << alexey.name << "\n";
    alexey.Armia(currentYear);

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
