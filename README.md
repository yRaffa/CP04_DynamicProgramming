# **📄 Checkpoint 4 | Dynamic Programming 🐍**

## **👥 Integrantes:**

```
Caio Felipe de Lima Bezerra     | RM: 556197
Marcos Vinícius da Silva Costa  | RM: 555490
Rafael Federici de Oliveira     | RM: 554736
```

🔸 Este projeto implementa dois desafios de otimização com três abordagens diferentes: **Brute Force**, **Divide & Conquer** e **Dynamic Programming**.

## **📂 Estrutura**
- `desafio1/`: Implementação dos algoritimos para o Desafio 1
- `desafio2/`: Implementação dos algoritimos para o Desafio 2
- `utils.py`: Funções auxiliares (geração de dados, medições, gráficos)
- `cp04.ipynb`: Notebook principal com testes e análises

## **🚀 Algoritmos Implementados**
### **🎒 DESAFIO 1:** Seleção de Projetos de Mitigação (Knapsack)
- **Brute Force:** O(2^n * n)
- **Divide & Conquer:** O(2^(n/2) * n)
- **Dynamic Programming:** O(n * orcamento)

### **🧠 DESAFIO 2:** Janela de Qualidade do Ar (Máxima Soma Contígua)
- **Brute Force:** O(n²)
- **Divide & Conquer:** O(n log n)
- **Dynamic Programming:** O(n)

## **📊 Resultados**
- **Brute Force:** inviável em instâncias grandes, usado apenas como referência.  
- **Divide & Conquer:** melhora em relação ao brute force, mas ainda limitado.  
- **Dynamic Programming:** solução prática e escalável, adequada para entradas grandes.  

## **▶️ Como executar**
1. Clone o repositório
2. Instale as dependências (`pip install -r requirements.txt`)
3. Abra o notebook:
   ```bash
   jupyter notebook cp04.ipynb
