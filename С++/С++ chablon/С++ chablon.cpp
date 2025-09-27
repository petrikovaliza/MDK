// С++ chablon.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>

using namespace std;

template<typename T>

void swapValues(T& a, T& b)
{
    T temp = a;
    a = b;
    b = temp;
}

template<class T>

class Pair {
private:
    T 1_elem;
    T 2_elem;
public:
    Pair(T 1_elem, 2_elem) : 1_elem{ 1_elem }, 2_elem{ 2_elem } {}

    void getFirst() 
    {
        cout << 1_elem << endl;
    }
    void getSecond()
    {
        cout << 2_elem << endl;
    }
    double printSum()
    {
        cout <<"Сумма: "<< 1_elem + 2_elem << endl;
    }
    double printProduct()
    {
        cout <<"Произведение: " 1_elem * 2_elem << endl;
    }
};

int main()
{
    setlocale(LC_ALL, "Rus");
    cout << "Задание 1.\n";

    int num1 = 3, num2 = 6;
    string name = "Liza", last_name = "Petrikova";

    swapValues<int>(num1,num2);
    cout << num1 << " " << num2 << endl;

    swapValues<string>(name, last_name);
    cout << name << " " << last_name << endl;

    cout << "\nЗадание 2.\n";

    Pair<int> f{ 3, 7 };
    f.printProduct();


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
