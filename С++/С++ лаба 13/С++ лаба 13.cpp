// С++ лаба 13.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <string>
#include <fstream>


using namespace std;

int main()
{
    setlocale(LC_ALL, "Rus");
    cout << "Вариант 1. Задание 1\n"<<endl;

    ofstream numb15_file_write("file1.txt");

    int n = 15;
    int enterNumb;

    for (int i = 0; i <= n; i++)
    {
        cout << i<<". Введите целое число для записи в файл: ";
        cin >> enterNumb;
        numb15_file_write << enterNumb << endl;
    }
    numb15_file_write.close();

    ifstream numb15_file_read("file1.txt");
    string line;
    int maxNumb = 0;

    while (getline(numb15_file_read, line))
    {
        int currentNumber = stod(line);
        if (currentNumber > maxNumb) maxNumb = currentNumber;
        cout << line << endl;
    }
    cout << "\nНаибольшее число в файле: " << maxNumb << endl;

    numb15_file_read.close();



    cout << "\n\nЗадание 2\n" << endl;

    ofstream num50_file_write("file2.txt");
    ofstream num50_2_file_write("file3.txt");
    string line_1_file, line_2_file;

    for (int i = -50; i <= 50; i++)
    {
        num50_file_write << i << endl;
    }

    num50_file_write.close();

    ifstream numb50_file_read("file2.txt");

    while (getline(numb50_file_read, line_1_file))
    {
        cout << line_1_file << endl;
        int currentNumber = stod(line_1_file);
        if (currentNumber % 3 == 0) num50_2_file_write << currentNumber << endl;
    }
    numb50_file_read.close();
    num50_2_file_write.close();

    ifstream num50_2_file_read("file3.txt");

    while (getline(num50_2_file_read, line_2_file))
    {
        cout << line_2_file << endl;
    }

    num50_2_file_read.close();

    cout << "\n\nЗадание 3\n" << endl;

    remove("file1.txt");
    remove("file2.txt");
    remove("file3.txt");







    

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
