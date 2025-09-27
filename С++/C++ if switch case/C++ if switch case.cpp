// C++ if switch case.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>

using namespace std;

int main()
{
    setlocale(LC_ALL, "Rus");
    cout << "Задание 1.\n";

    /*int numb;

    cout << "Введите число от 1 до 7: ";
    cin >> numb;

    switch (numb)
    {
    case 1:
        cout << "Понедельник";
        break;
    case 2:
        cout << "Вторник";
        break;
    case 3:
        cout << "Среда";
        break;
    case 4:
        cout << "Четверг";
        break;
    case 5:
        cout << "Пятница";
        break;
    case 6:
        cout << "Суббота";
        break;
    case 7:
        cout << "Воскресенье";
        break;
    default:
        cout << "Нет!!! Введите от 1 до 7!";
        break;
    }*/

    //
    //cout << "Задание 2.\n";

    //int month;

    //cout << "Введите номер месяца: ";
    //cin >> month;

    //switch (month)
    //{
    //case 12:
    //case 1:
    //case 2:
    //    cout << "Зима" << endl;
    //    break;
    //case 3:
    //case 4:
    //case 5:
    //    cout << "Весна" << endl;
    //    break;
    //case 6:
    //case 7:
    //case 8:
    //    cout << "Лето" << endl;
    //    break;
    //case 9:
    //case 10:
    //case 11:
    //    cout << "Осень" << endl;
    //    break;  
    //default:
    //    cout << "Нет!!! Введите от 1 до 12!" << endl;
    //    break;
    //}

    ////
    //cout << "Задание 3.\n";

    //int mark;

    //cout << "Введите оценку от 1 до 5: ";
    //cin >> mark;

    //switch (mark)
    //{
    //case 1:
    //    cout << "Просто кошмар" << endl;
    //    break;
    //case 2:
    //    cout << "Мерзость" << endl;
    //    break;
    //case 3:
    //    cout << "Удовлетворительно" << endl;
    //    break;
    //case 4:
    //    cout << "Хорошо" << endl;
    //    break;
    //case 5:
    //    cout << "Отлично!!!" << endl;
    //    break;
    //default:
    //    cout << "Нет!!! Нет такой оценки!" << endl;
    //    break;
    //}

    ////
    //cout << "Задание 4.\n";

    //int number;

    //cout << "Введите число: ";
    //cin >> number;

    //if (number % 2 == 0) cout << "Четное" << endl; else cout << "Нечетное" << endl;

    //
    cout << "Задание 5.\n";

    int ed_izmer;
    double value;
    string ed_value;

    do 
    {
        cout << "Введите единицу измерения(цифру):\n1. Миллиметр\n2. Сантиметр\n3. Метр\n\n4. Километр\n5. Миллиграмм\n6. Грамм\n\n7. Килограмм\n8. Тонн\n9.Куб.миллиметр\n\n10. Куб.сантиметр\n11. Куб.метр\n12. Куб.километр" << endl;
        cout << "Для выхода нажмите 0." << endl;
        cin >> ed_izmer;

        cout << "Введите значение: ";
        cin >> value;

        cout << "--------------" << endl;

        switch (ed_izmer)
        {
        case 1:
            cout << value << " мм: " << endl;
            cout << "Cантиметр: " << value / 10 << endl;
            cout << "Метр: " << value / 1000 << endl;
            cout << "Километр: " << value / 1000000 << endl;
            continue;

        case 2:
            cout << value << " см: " << endl;
            cout << "Миллиметр: " << value * 10 << endl;
            cout << "Метр: " << value / 100 << endl;
            cout << "Километр: " << value / 100000 << endl;
            continue;

        case 3:
            cout << value << " м: " << endl;
            cout << "Миллиметр: " << value * 1000 << endl;
            cout << "Сантиметр: " << value / 100 << endl;
            cout << "Километр: " << value / 1000 << endl;
            continue;

        case 4:
            cout << value << " км: " << endl;
            cout << "Миллиметр: " << value * 1000000 << endl;
            cout << "Сантиметр: " << value * 100000 << endl;
            cout << "Метр: " << value * 1000 << endl;
            continue;

        case 5:
            cout << value << " мг: " << endl;
            cout << "Грамм: " << value / 1000 << endl;
            cout << "Килограмм: " << value / 1000000 << endl;
            cout << "Тонна: " << value / 1000000000 << endl;
            continue;

        case 6:
            cout << value << " г: " << endl;
            cout << "Миллиграмм: " << value * 1000 << endl;
            cout << "Килограмм: " << value / 1000 << endl;
            cout << "Тонна: " << value / 1000000 << endl;
            continue;

        case 7:
            cout << value << " кг: " << endl;
            cout << "Миллиграмм: " << value * 1000000 << endl;
            cout << "Грамм: " << value * 1000 << endl;
            cout << "Тонна: " << value / 1000 << endl;
            continue;

        case 8:
            cout << value << " т: " << endl;
            cout << "Миллиграмм: " << value * 1000000000 << endl;
            cout << "Грамм: " << value * 1000000 << endl;
            cout << "Килограмм: " << value * 1000 << endl;
            continue;

        case 9:
            cout << value << " куб.мм: " << endl;
            cout << "Кубический сантиметр: " << value / 1000 << endl;
            cout << "Кубический метр: " << value / 1000000 << endl;
            cout << "Кубический километр: " << value / 1000000000000 << endl;
            continue;

        case 10:
            cout << value << " куб.см: " << endl;
            cout << "Кубический миллиметр: " << value * 1000 << endl;
            cout << "Кубический метр: " << value / 1000000 << endl;
            cout << "Кубический километр: " << value / 1000000000000 << endl;
            continue;

        case 11:
            cout << value << " куб.м: " << endl;
            cout << "Кубический миллиметр: " << value * 1000000 << endl;
            cout << "Кубический сантиметр: " << value * 1000000 << endl;
            cout << "Кубический километр: " << value / 1000000000 << endl;
            continue;

        case 12:
            cout << value << " куб.км: " << endl;
            cout << "Кубический миллиметр: " << value * 1000000000000 << endl;
            cout << "Кубический сантиметр: " << value * 1000000000000 << endl;
            cout << "Кубический метр: " << value * 1000000000 << endl;
            continue;

        default:
            cout << "Такой операции нет!" << endl;
            continue;

        }
        cout << "--------------" << endl;

    }while (ed_izmer != 0);
    
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
