Clone da Netflix com Django, incluindo funcionalidades como “Últimos Assistidos”, “Recomendações” e “Novidades”. Utilizei o Superusuário do Django para gerenciar filmes e categorias, e implementei autenticação encriptada.
# House Prices Kaggle
Técnicas Avançadas de Regressão

<img src="https://github.com/HugoLeandro/django/blob/main/imagens/homepage.png" width=800/>


## Etapa 1: Modelo Básico com Variáveis Numéricas
Nesta etapa inicial, foi criado um modelo básico utilizando apenas variáveis numéricas e substituindo valores ausentes por -1. As seguintes etapas foram realizadas:

- Eliminação de Colunas com Valores Vazios: Colunas com mais de 10% de valores ausentes foram removidas para evitar problemas de viés e instabilidade nos modelos.
- Divisão do Conjunto de Dados: O conjunto de dados foi dividido em conjuntos de treinamento e teste para avaliar o desempenho dos modelos.
- Implementação de Algoritmos de Regressão Simples: Foram utilizados os seguintes algoritmos de regressão:
### Regressão Linear
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
### Árvore de Regressão
https://scikit-learn.org/stable/modules/tree.html#regression
### KNeighborsRegressor
https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor

## Avaliação dos Modelos: A performance dos modelos foi avaliada utilizando as seguintes métricas:
Erro Médio Absoluto (MAE):
https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html

Erro Quadrático Médio (MSE):
https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html

- Resultado obitido:
<img src="https://github.com/HugoLeandro/House-Prices/blob/main/Imagens/resultado-kaggle1.png"/>
