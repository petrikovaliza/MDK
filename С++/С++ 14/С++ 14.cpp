// С++ 14.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

struct Cities
{
    string city_name;
    int population;
    int year_founded;
    double city_area;
};

int main()
{
    setlocale(LC_ALL, "Rus");
    cout << "Вариант 1. Задание 1.\n"<<endl;

    const int cityCount = 3; //массив
    Cities cities[cityCount];

    for (int i = 0; i < cityCount; i++)
    {
        cout << "Введите информацию о городе - " << (i + 1) << ":\n";
        cout << "Название города: ";
        cin >> ws; // убираем пробелы перед вводом
        getline(cin, cities[i].city_name);
        cout << "Численность населения: ";
        cin >> cities[i].population;
        cout << "Год основания: ";
        cin >> cities[i].year_founded;
        cout << "Занимаемая площадь (в км2): ";
        cin >> cities[i].city_area;
        cout << endl; //пустая строка для разделения вводов
    }

    ofstream citiesFile("cities.txt");
    if (!citiesFile)
    {
        cout << "Ошибка, не удалось открыть файл для записи!" << endl;
        return 1; 
    }
    
    for (const auto& city : cities) // объявляем city ссылкой на элемент контейнера, а именно на каждую структуру типа City в массиве
    {
        citiesFile << "Город: " << city.city_name << " Население: " << city.population << " Год основания: " << city.year_founded << " Занимаемая площадь: " << city.city_area<<" км\n"<< "----------------------"<<endl;
    }
    citiesFile.close();
    cout << "Информация о городах была успешно записана в файл cities.txt." << endl;



    cout << "\n\nЗадание 2.\n" << endl;

    ifstream citiesFile_read("cities.txt");
    string line;

    if (!citiesFile_read)
    {
        cerr << "Ошибка, не удалось открыть файл для чтения!" << endl;
        return 1;
    }

    while (getline(citiesFile_read, line))
    {
        cout << line << endl;
    }
    citiesFile_read.close();

    cout << "\n\nЗадание 3.\n" << endl;
    ifstream citiesFile_read3("cities.txt");

    cout << "\nГородa, основанные позднее 1900 года: "<<endl;

    while (getline(citiesFile_read3, line))
    {
        for (int i = 0; i < line.length(); i++)
        {
            if (cities[i].year_founded > 1900) cout << cities[i].city_name << endl;
        }
    }
        
    citiesFile_read3.close();

    cout << "\n\nЗадание 4.\n" << endl;

    ifstream citiesFile_read4("cities.txt");

    int max_population = 0;
    string max_city;

    string line;
    while (getline(citiesFile_read4, line))
    {
        size_t pos = line.find("Население: ");
        if (pos != string::npos)
        {
            int population = stoi(line.substr(pos + 11));
            if (population > max_population)
            {
                max_population = population;
                max_city = line.substr(7, pos - 8);
            }
        }
    }

    cout << "Город с самым большим населением: " << max_city << " (" << max_population << ")" << endl;

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
