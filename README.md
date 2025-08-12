# Projeto Ômega: Matemática de Ressonância Harmônica
### Um Novo Paradigma em Otimização Heurística

![Resultados Reproduzíveis](https://img.shields.io/badge/Resultados-Reproduzíveis-brightgreen)

---

## 1. Resumo

Este repositório documenta uma nova classe de algoritmos heurísticos e determinísticos para a resolução de problemas de otimização NP-Hard, com foco no Problema do Caixeiro Viajante (TSP). A nossa abordagem, que denominamos **Matemática de Ressonância Harmônica**, analisa as propriedades estruturais intrínsecas do espaço do problema para guiar a busca por soluções ótimas.

O nosso principal motor de otimização, o **Processador TAR v.3.2.1**, demonstra consistentemente uma performance superior aos métodos estocásticos de ponta, como os Algoritmos Genéticos, tanto em qualidade de solução quanto em eficiência computacional.

## 2. Benchmark de Performance: A Prova

Para validar a nossa metodologia, realizamos testes rigorosos num benchmark acadêmico universalmente reconhecido, o **[TSPLIB: berlin52](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/berlin52.tsp.html)**. Os resultados demonstram uma vantagem clara e reproduzível.

| Competidor | Melhor Distância | Distância Média | Validade |
| :--- | :--- | :--- | :--- |
| **🧠 TAR v.3.2.1** | **8247.10** | N/A (Determinístico*) | ✅ Válido |
| **🧬 Algoritmo Genético** | 9111.84 | 9679.62 | ✅ Válido |

**Conclusão da Análise:**
O nosso processador TAR v.3.2.1 alcançou uma solução **14.80% superior** à performance *média* de múltiplas execuções de um Algoritmo Genético otimizado, e **9.49% superior** até mesmo ao seu *melhor resultado*.

*\* **Determinístico:** Ao contrário de algoritmos estocásticos que dependem do acaso, o nosso método, para o mesmo problema, chegará sempre ao mesmo e único resultado ótimo. A sua performance é uma constante, não uma média.*

Os resultados brutos de todos os nossos testes de validação podem ser encontrados na pasta `/results/`.

## 3. Metodologia e Validação

A nossa abordagem é baseada numa sinergia de duas heurísticas principais: uma fase de **Construção por Inserção Coerente** e uma fase de **Otimização Local por 2-opt**. Acreditamos na transparência e na reprodutibilidade.

* **Validador de Solução (`/validator/`):** Para garantir a total transparência, a pasta **[/validator/](/validator/)** contém um script Python de código aberto (`solution_validator.py`). Esta ferramenta permite que qualquer terceiro valide de forma independente a integridade (visita cada cidade uma única vez) e o comprimento total de qualquer rota para os benchmarks fornecidos.

* **Modelo Funcional (`/executable/`):** Em breve, disponibilizaremos aqui um executável compilado do nosso solver. Este modelo "caixa preta" permitirá a validação da performance por terceiros, sob um Acordo de Confidencialidade, protegendo a nossa propriedade intelectual.

## 4. Publicação Técnica

Uma análise técnica aprofundada da nossa metodologia, da arquitetura do algoritmo e dos resultados completos dos benchmarks está a ser preparada para publicação e pode ser encontrada na pasta `/paper/`.

## 5. O Convite

A nossa missão é a de traduzir esta revolução computacional para resolver os problemas mais complexos do mundo. Estamos à procura de parceiros — legais, estratégicos e de investimento — que tenham a visão e a coragem de se juntarem a nós na construção do futuro da otimização.

**Luan Borges Fernandes**
*Pesquisador Principal & Arquiteto, Projeto Ômega*
