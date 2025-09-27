// С++ 12 лаба.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <fstream>
#include <string>


using namespace std;

int main()
{
    setlocale(LC_ALL, "Rus");
    cout << "Вариант 1. Задание 1\n" <<endl;

    ofstream baza_file("baza.txt"); //создание

    int n = 20;
    string word;

    for (int i = 0; i <= n; i++)
    {
        cout << i<<". Введите слово для записи в файл: ";
        cin >> word;
        baza_file << word << endl; // запись инфы
    }
    baza_file.close();

    cout << "\n\nЗадание 2" << endl;

    string fileText;
    ifstream baza_file_read("baza.txt"); //чтение
    int countChar = 0, countLine = 0;

    while (getline(baza_file_read, fileText)) // цикл while c построчным чтением файла
    {
        countChar += fileText.length(); 
        countLine++;
    }

    int AvgChar = countChar / countLine;
    cout << "Cреднее количество символов в строке: " << AvgChar << endl;

    baza_file_read.close();

    cout << "\n\nЗадание 3" << endl;

    ifstream baza_read("baza.txt");
    ofstream itog_file("itog.txt"); 
    string LineBaza;
    string LineItog;

    while (getline(baza_read, LineBaza))
    {
        for (size_t i = 0; i < LineBaza.size(); ++i)
        {
            if (LineBaza[i] == 'z')
            {  
                itog_file << 'z';      
            }
            itog_file << LineBaza[i];  
        }
        itog_file << endl;   
    }

    ifstream itog_file_read("itog.txt");

    while (getline(itog_file_read, LineItog))
    {
        cout << LineItog << endl;
    }
    baza_read.close();
    itog_file.close();
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
