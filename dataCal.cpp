#include "include/nlohmann/json.hpp"
#include <iostream>
#include <fstream>
#include <string>

using json = nlohmann::json;
using string = std::string;

class dataCal{
    public:
    dataCal(){};
    ~dataCal(){};

    void populateTeams(){
        std::ifstream dataFile("exampleTeamsRequest.json");
        json data = json::parse(dataFile);

        json output;
        std::cout << data.size() << "\n";
        int index = 0;
        for(json x:data){
            json temp;
            std::cout << x["team_number"] << " ";
            temp["teamName"] = x["nickname"];
            temp["teamNumber"] = x["team_number"];
            int t=x["team_number"];
            string number = "num"+index;
            
            output[index] = temp;
            index+=1;
        }
        std::cout << "\n";
        std::cout << output << "\n";
    };

    private:

};
