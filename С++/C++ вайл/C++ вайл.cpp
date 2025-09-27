// C++ вайл.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <ctime>

using namespace std;

int main()
{
    setlocale(LC_ALL, "Rus");
    cout << "Задание 1." << endl;

    int start = 0, N;

    cout << "Введите число N: ";
    cin >> N;

    cout << "Вывод чисел от 1 до N: ";
    while (start < N)
    {
        start += 1;
        cout << start << " ";
    }
    cout << "\n";
    system("pause");

    cout << "\n\nЗадание 2.\n";

    srand(time(0));
    int unknown_number = 1 + rand() % 10;
    int enter_number;
    cout << "Отгадайте число от 1 до 10: ";
    cin >> enter_number;

    while (enter_number != unknown_number)
    {
        cout << "Нет, продолжай отгадывать: ";
        cin >> enter_number;
    }
    
    cout << "Ты угадала!!!\n";
    system("pause");

    cout << "\n\nЗадание 3.\n";

    string password = "tru00", enter_password;
    cout << "Введите пароль: ";
    cin >> enter_password;

    while (enter_password != password)
    {
        cout << "Неверный пароль, попробуй снова: ";
        cin >> enter_password;
    }

    cout << "Пароль верный!\n";

    system("pause");

    cout << "\n\nЗадание 4.\n";

    int sum = 0, enter_numb = 1;

    while (enter_numb != 0)
    {
        cout << "Вводите числа. Для выхода нажмите 0: ";
        cin >> enter_numb;
        sum += enter_numb;
    }

    cout << "Сумма введенных чисел: " << sum<< endl;
    system("pause");

    cout << "\n\nЗадание 5.\n";

     int N_end;

    cout << "Введите N: ";
    cin >> N_end;

    int factorial = 1;
    int i = 1;

    while (i <= N_end)
    {
        factorial *= i;
        i++;
    }
    cout << "Факториал числа: " << factorial << endl;

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
