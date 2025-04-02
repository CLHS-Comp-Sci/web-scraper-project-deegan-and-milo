

#include "include/nlohmann/json.hpp"
#include <iostream>
#include <fstream>
#include <string>
using json = nlohmann::json;

// ...
int main(){
    
    // std::ifstream f("example.json");
    std::fstream thisFile("exam.json");

    std::string newVar = "hithere";
    // std::ofstream thisFile("example.json");

    json j2;
    j2["hi"]="there";
    j2["pi"]=3.14;
    j2["happy"]=true;


    thisFile << j2;
    // std::cout << f;
    // json data = json::parse(thisFile);
    // std::cout << data["hi"];
    // thisFile << data;
}
