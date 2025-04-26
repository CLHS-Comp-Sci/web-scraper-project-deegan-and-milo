
#include "include/nlohmann/json.hpp"
#include <iostream>
#include <fstream>
#include <string>

#include "dataCal.cpp"

using json = nlohmann::json;
using string = std::string;


int main(){
    
    // std::ifstream f("teams.json");
    // std::ofstream thisFile("exam.json");

    // string newVar = "hithere";
    // std::ofstream thisFile("example.json");

    // json j2;
    // j2["hi"]="there";
    // j2["pi"]=3.14;
    // j2["happy"]=true;


    // std::cout << f.get() << "\n";
    // std::cout << f.get() << "\n";

    // if(f.get()==-1){
    //     std::cout << "file is empty" << std::endl;
    // }
    // thisFile << j2;
    // json data = json::parse(thisFile);
    // std::cout << data["hi"];
    // thisFile << data;

    dataCal dataCalc = dataCal();

    dataCalc.populateTeams();


    system("pause");
}
