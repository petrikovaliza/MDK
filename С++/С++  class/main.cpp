// С++  class.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <windows.h>
#include "MyCLass.h""

using namespace std;

int main()
{
    setlocale(LC_ALL, "Russian");

    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);

    //////Задание 1

    Students student;

    student.set_name();
    student.get_name();
    student.set_age();
    student.get_age();
    student.set_scores();
    student.set_average_ball();
    get_average_ball
    student.set_age();
    
        
    //////Задание 2

    Book book;

    string book_name, avtor;
    int year_vupusk;

    cout << "Введите название книги: ";
    getline(cin, book_name);

    cout << "Введите автора: ";
    getline(cin, avtor);

    cout << "Введите год выпуска: ";
    cin >> year_vupusk;

    book.set_book_name(book_name);
    book.set_avtor(avtor);
    book.set_year_vupusk(year_vupusk);


    cout << "Книга: " << book.get_book_name() << endl;
    cout << "Автор: " << book.get_avtor() << endl;
    cout << "Год издания: " << book.get_year_vupusk() << endl;

    //////Задание 3



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
