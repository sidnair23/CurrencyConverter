#include <iostream>

int main() {
  
  //declaring the currency variables for Pesos, Reais and Soles
  
  double Pesos;
  double Reais;
  double Soles;
  
  //declaring the dollar
  
  double USDollars;
  
  //Total Colombian Pesos
  std::cout << "How much Colombian Pesos do you have: ";
  std::cin >> Pesos;
  
  //Total Brazilian Reais
  std::cout << "How much Brazilian Reais do you have: ";
  std::cin >> Reais;
  
  //Total Peruvian Soles
  std::cout << "How much Peruvian Soles do you have: ";
  std::cin >> Soles;
  
  /*Colombian Pesos to USD: 0.00029
  Brazilian Reais to USD: 0.24
  Peruvian Soles to USD: 0.30*/ 
  
  //Total Dollars
  
  USDollars = (0.00029*Pesos) + (0.24*Reais) + (0.30*Soles);
  
  //Seeing this out
  std::cout << "US Dollars = $" << USDollars << "\n";
}