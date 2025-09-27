// С++ except.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <exception>
#include <fstream>
#include <string>
#include <map>


using namespace std;

int divide(double a, double b)
{
    if (b == 0) throw string("Zero division error");
    return a / b;
}

class Bank_chet
{
private:
    double balance;
public:
    Bank_chet()
    {
        balance = 0;
    }
    void menu()
    {
        int choice;

        cout << "Выберите операцию: \n1.Посмотреть баланс.\n2.Пополнение.\n3.Снятие\n";
        cin >> choice;

        if (choice == 1) get_balance();
        else if (choice == 2) popolnenie();
        else if (choice == 3) snyatie();
        else  throw string("Такой операции нет!");
    }

    void get_balance()
    {
        cout << "Текущий баланс: " << balance << endl;
        cout << "\n";
        menu();
    }

    void popolnenie()
    {
        float summ_popolnenia;
        cout << "Введите сумму для пополнения: ";
        cin >> summ_popolnenia;
        balance += summ_popolnenia;
        cout << "Счет пополнен." << endl;
        cout << "\n";
        menu();
    }

    void snyatie()
    {
        float summ_snyatia;
        cout << "Введите сумма для снятия: ";
        cin >> summ_snyatia;
        if (balance >= summ_snyatia) 
        {
            balance -= summ_snyatia;
            cout << "Успешно." << endl;
        }
        else if (balance < 0) throw string("Баланс отрицательный, снять невозможно!");
        else throw string("Сумма снятия больше баланса!");
        
        cout << "\n";
        menu();

    }
};


void user_data()
{
    string username, password, email;
    map<string, pair<string, string>> database = { 
        { "Alice",{ "111rrr", "dasjsahdkjs@mail.ru" } }, 
        { "Vadim",{"dfsd534", "buba@gmail.com" } }, 
        { "Kolya",{ "55yy", "koko@mail.ru" } } };

    while (true)
    {
        cout << "Введите имя пользователя: ";
        getline(cin, username);
        if (username == "") throw string("Имя пользователя не может быть пустым.");

        cout << "Введите пароль: ";
        getline(cin, password);
        if (password == "") throw string("Пароль не может быть пустым.");

        cout << "Введите электронную почту: ";
        getline(cin, email);
        if (email == "") throw string("Почта не может быть пустой.");

        auto it = database.find(username);

        if (it != database.end()) 
        {
            const auto& vnalichii_pair = it->second;

            if (vnalichii_pair.first == password && vnalichii_pair.second == email)
            {
                cout << "Добро пожаловать, " << username << "!" << endl;
                return;
            }
            else 
            {
                throw string("Неверный пароль или электронная почта.");
            }
        }
        else 
        {
            throw string("Пользователь '" + username + "' не найден.");
        }
    }
}


int main()
{
    setlocale(LC_ALL, "Rus");
    cout << "Задание 1."<<endl;

    double a, b;

    cout << "Введите a: ";
    cin >> a;
    cout << "Введите b: ";
    cin >> b;

    try
    {
        cout <<"a / b: " << divide(a, b);
    }
    catch (string error_message)
    {
        cout << error_message;
    }

    cout << "\nЗадание 2.\n" << endl;

    Bank_chet go;

    try
    {
        go.menu();
        go.snyatie();
        go.popolnenie();
        go.get_balance();     
    }
    catch (string error_message)
    {
        cout << error_message << endl;

        ofstream log_write("log2.txt", ios_base::app);

        log_write << "Error throw: " << error_message << endl;
        log_write << "Date and time of exception: " << __DATE__ << " " << __TIME__ << endl;
        log_write << "In a path: " << __FILE__ << endl;
        log_write << "In a function: " << __func__ << endl;
        log_write << "At line: " << __LINE__ << endl;
        log_write << "\n";
        log_write.close();
    }

    cout << "\nЗадание 3.\n" << endl;

    try 
    {
        user_data();
    }
    catch (string error_message2)
    {
        cout << error_message2 << endl;

        ofstream log_write2("log2.txt", ios_base::app);

        log_write2 << "Error throw: " << error_message2 << endl;
        log_write2 << "Date and time of exception: " << __DATE__ << " " << __TIME__ << endl;
        log_write2 << "In a path: " << __FILE__ << endl;
        log_write2 << "In a function: " << __func__ << endl;
        log_write2 << "At line: " << __LINE__ << endl;
        log_write2 << "\n";
        log_write2.close();
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
