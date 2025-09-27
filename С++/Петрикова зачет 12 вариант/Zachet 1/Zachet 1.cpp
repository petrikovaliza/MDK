// Zachet 1.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <list>
#include <string>
#include <cmath>
#include <set>
#include <vector>

using namespace std;

list<int> krat17(list<int>numbers)
{
    list<int> result_list = {};
    for (int number : numbers)
        if (number % 17 == 0) result_list.push_back(number);

    return result_list;
}

int armstrong_number(int number)
{
    string digits = to_string(number);
    double sum_of_cubes = 0;

    for (char digit : digits)
        int number = digit - '0';
        sum_of_cubes += pow(number, digits.size());

    if (sum_of_cubes == number)
    {
        cout << number << " является числом Армстронга.";
    }
    else
    {
        cout << number << " не является числом Армстронга.";
    }

    return sum_of_cubes;
}

int power_set(set<int> set)
{
    return set.size();
}

void sort_shell(vector<int>& posled)
{
    int count_element = posled.size();
    int step = count_element / 2;
    while (step > 0)
    {
        for (int i = step; i < count_element; i++)
        {
            int j = i;
            while (j >= step && posled[j] < posled[j - step])
                swap(posled[j], posled[j - step]);
                j -= step;
        }
        step = step /= 2;
    }
}

int main()
{
    setlocale(LC_ALL, "Rus");
    cout << "Задание 1"<< endl;

    list<int> myspisochek{ 359, 2839, 17, 147, 294,357 };
    list<int>result = krat17(myspisochek);
    for (int num : result)
        cout << num << " ";

    cout << "\n\nЗадание 2" << endl;

    armstrong_number(2017);

    cout << "\n\nЗадание 3" << endl;

    set<int> mySet = { 1, 3, 4, 35, 3, 8, 9 };
    cout << "Мощность множества: " << power_set(mySet) << endl;
    
    cout << "\n\nЗадание 5" << endl;

    vector<int> spisochek = { 5, 0, -2, 7, 3 };
    cout << "Список до сортировки: ";
    for (int element : spisochek)
        cout << element << " ";
    cout << "\nСписок после сотрировки: ";
    sort_shell(spisochek);
    for (int element : spisochek)
        cout << element << " ";

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
