// С++ лаба 16.2.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
using namespace std;

class Car
{
protected:
    double rashod_na_100;

public:
    Car(double rashod_na_100) : rashod_na_100(rashod_na_100) {}

    virtual double Price() = 0;
    virtual void printInfo() = 0;
};

class Gruzovik : public Car
{
private:
    double gruzopojem;

public:
    Gruzovik(double rashod_na_100, double gruzopojem) : Car(rashod_na_100), gruzopojem(gruzopojem) {}

    double Price() override
    {
        
        double price_toplivo = 50 * rashod_na_100 / 100;
        return price_toplivo / gruzopojem;
    }

    void printInfo() override
    {
        cout << "Грузовик:\n" << endl;
        cout << "Грузоподьемность: " << gruzopojem << " тонн" << endl;
        cout << "Расход на 100 км: " << rashod_na_100 << " литров" << endl;
        cout << "Затраты на 1 тонну груза на 1 км: " << Price() << " рублей" << endl;
    }
};

class Bus : public Car
{
private:
    int passanger_mesta;

public:
    Bus(double rashod_na_100, int passanger_mesta) : Car(rashod_na_100), passanger_mesta(passanger_mesta) {}

    double Price() override
    {
        
        double price_toplivo = 50 * rashod_na_100 / 100;
        return price_toplivo / passanger_mesta;
    }

    void printInfo() override
    {
        cout << "\nАвтобус:\n" << endl;
        cout << "Количество пассажирских мест: " << passanger_mesta << endl;
        cout << "Расход на 100 км: " << rashod_na_100 << " литров" << endl;
        cout << "Затраты на 1 пассажира на 1 км: " << Price() << " рублей" << endl;
    }
};

int main() 
{
    setlocale(LC_ALL, "Rus");
    Gruzovik грузовик(20, 10);
    Bus автобус(15, 30);

    грузовик.printInfo();
    автобус.printInfo();

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
