#include <iostream>
#include "E:\Я\МДК Работы\С++  class\MyCLass.h"

using namespace std;

void Students::set_name(string student_name)
{
    Students::name = student_name;
}

string Students::get_name()
{
    return Students::name;
}

void Students::set_age(int student_age)
{
    Students::age = student_age;
}

int Students::get_age()
{
    return Students::age;
}

void Students::set_scores(int scores[])
{
    for (int i = 0; i < 5; ++i) {
        Students::scores[i] = scores[i];
    }
}

void Students::set_average_ball(float ball)
{
    Students::average_ball = ball;
}

float Students::get_average_ball()
{
    return Students::average_ball;
}

//

void Book::set_book_name(string book_name)
{
    Book::book_name = book_name;
}

string Book::get_book_name()
{
    return Book:: book_name;
}

void Book::set_avtor(string avtor)
{
    Book::avtor = avtor;
}

string Book::get_avtor()
{
    return Book:: avtor;
}

void Book::set_year_vupusk(int year_vupusk)
{
    Book::year_vupusk = year_vupusk;
}

int Book::get_year_vupusk()
{
    return Book::year_vupusk;
}

void Students::printInfo()
{
    Students student;

    string name;
    int age;

    cout << "Имя: ";
    getline(cin, name);

    cout << "Возраст: ";
    cin >> age;

    student.set_name(name);
    student.set_age(age);

    int scores[5];
    int sum = 0;

    for (int i = 0; i < 5; ++i) {
        cout << "Оценки " << i + 1 << ": ";
        cin >> scores[i];
        sum += scores[i];
    }

    student.set_scores(scores);
    float average_ball = sum / 5.0;
    student.set_average_ball(average_ball);
    cout << "Средний балл " << student.get_name() << ": " << student.get_average_ball() << " Возраст: "
        << student.get_age() << endl;
}
