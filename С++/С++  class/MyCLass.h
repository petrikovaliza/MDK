#pragma once

#include <string>

using namespace std;

class Students {
public:

    void set_name(string);
    string get_name();
    void set_age(int);
    int get_age();
    void set_scores(int[]);
    void set_average_ball(float);
    float get_average_ball();
    void printInfo();

private:

    int scores[5];
    float average_ball;
    string name;
    int age;
};

class Book {
public:

    void set_book_name(string);
    string get_book_name();
    void set_avtor(string);
    string get_avtor();
    void set_year_vupusk(int);
    int get_year_vupusk();
    void printInfo();

private:

    int year_vupusk;
    string book_name;
    string avtor;

};