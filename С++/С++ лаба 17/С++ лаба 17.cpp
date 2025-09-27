// С++ лаба 17.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <vector>
#include <random>
#include <ctime>

using namespace std;

int main()
{
    setlocale(LC_ALL, "Rus");
    cout << "Вариант 13. Задание 1.\n" << endl;

    vector<int> numbers(7);

    for (size_t i = 0; i < numbers.size(); ++i) {
        cout << "Введите число " << i + 1 << ": ";
        cin >> numbers[i];
    }

    int sum = 0;

    for (int num : numbers)
    {
        if (num >= 0 && num % 2 == 0) sum += num;
    }

    cout << "\nСумма четных неотрицательных элементов: " << sum << endl;


    cout << "Задание 2.\n" << endl;

    vector<int> random_numbers(6);

    mt19937 generator(time(0));
    uniform_int_distribution<int> distribution(1, 8);

    for (int i = 0; i < 6; i++)
    {
        random_numbers[i] = distribution(generator);
    }
    cout << "Случайные числа: ";
    for (int numbers : random_numbers) cout << numbers << " ";

    cout << "\nЗаменить все числа кратные 3 – на 1: ";

    for (int numbers : random_numbers)
    {
        if (numbers % 3 == 0) numbers = 1;
        cout << numbers << " ";
    }*/

    cout << "Задание 3.\n" << endl;

    vector<int> random_nums(5);

    mt19937 generator(time(0));
    uniform_int_distribution<int> distribution(-2, 4);

    for (int i = 0; i < 5; i++)
    {
        random_nums[i] = distribution(generator);
    }
    cout << "Случайные числа: ";
    for (int numbers : random_nums) cout << numbers << " ";

    cout << "\nИндексы всех нечётных элементов: ";

    for (int i = 0; i < random_nums.size(); i++)
    {
        if (random_nums[i] % 2 != 0) cout << i << " ";
    }

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
