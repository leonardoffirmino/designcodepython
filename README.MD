# Calculadoras com Design Patterns em Python RocketSeat

## 📌 Sobre o projeto  
Este projeto foi desenvolvido com o objetivo de **entender e aplicar conceitos de design de código em Python**, utilizando os padrões de projeto **Factory** e **Interfaces**.  

Foram criadas **três calculadoras diferentes**, cada uma implementando operações matemáticas básicas e suas regras respectivas. A ideia principal é demonstrar como os padrões de design podem tornar o código:  
- Mais **flexível**;  
- Mais **fácil de manter**;  
- **Aberto para extensões** sem necessidade de grandes alterações. 

Também foram aplicado conceitos de testes para todos os fluxos desenvolvidos com pytest.

---

## 🛠️ Padrões de Design aplicados  

### 🔹 Factory  
O **Factory Pattern** foi utilizado para criar instâncias das calculadoras de forma centralizada, permitindo que o código cliente solicite uma calculadora sem precisar conhecer sua implementação interna.  

### 🔹 Interfaces  
Foram definidas **interfaces (abstrações)** para padronizar os métodos que todas as calculadoras devem possuir. Isso garante consistência e facilita a substituição ou adição de novas calculadoras no futuro.  

