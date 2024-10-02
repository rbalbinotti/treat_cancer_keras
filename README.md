NOTICE
**Project in development**


> Medicina Personalizada - Redefinindo o Tratamento de Câncer - *Redefining Cancer Treatment*.  
> **Curso - Machine Learning**  
> Projeto da Formação Cientista de Dados da [Data Science Academy](https://www.datascienceacademy.com.br/)

## Descrição Projeto

Muito tem sido dito durante os últimos anos sobre como a medicina de precisão e, mais concretamente, como o teste genético, vai provocar disrupção no tratamento de doenças como o câncer.  

Mas isso ainda está acontecendo apenas parcialmente devido à enorme quantidade de trabalho manual ainda necessário. Neste projeto, tentaremos levar a medicina personalizada ao seu potencial máximo.  

Uma vez sequenciado, um tumor cancerígeno pode ter milhares de mutações genéticas. O desafio é distinguir as mutações que contribuem para o crescimento do tumor das mutações.  

Atualmente, esta interpretação de mutações genéticas está sendo feita manualmente. Esta é uma tarefa muito demorada, onde um patologista clínico tem que revisar manualmente e classificar cada mutação genética com base em evidências da literatura clínica baseada em texto.

Para este projeto, o [MSKCC](https://en.wikipedia.org/wiki/Memorial_Sloan_Kettering_Cancer_Center) (Memorial Sloan Kettering Cancer Center) está disponibilizando uma base de conhecimento anotada por especialistas, onde pesquisadores e oncologistas de nível mundial anotaram manualmente milhares de mutações.

   > O objetivo do projeto é desenvolver um algoritmo de Aprendizado de Máquina que, usando essa base de conhecimento como uma linha de base, classifica automaticamente as variações genéticas.

Para a construção desse projeto, o dataset é disponibilizado para download no link: [kaggle.data](https://www.kaggle.com/c/msk-redefining-cancer-treatment/data)



## Fonte Dados

-   [Kaggle](https://www.kaggle.com)
-   [Data Science Academy](https://www.datascienceacademy.com.br)

## Tecnologias Empregadas

- [PDM Python](https://pdm-project.org/)
- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [Keras](https://keras.io/)
- [GitHub](https://github.com/)

### Instalação

- Baixar o projeto do [github](https://github.com/rbalbinotti/treat_cancer_keras)

- Instalar dependências, utilizando o PDM Python, basta digitar o comando abaixo estando na pasta do projeto.
```
    pdm sync
```
    Caso necessite os pacotes e versões estão no arquivo pyproject.toml

# Dicionário de dados

- ID : Identificação única de cada elemento
- Gene : Gene onde a mutação genética está localizada
- Variation : Aminoácidos modificados pela mutação
- Class : 1-9 classe em que a mutação genética será classificada
- Clinical Evidence: Evidências clinicas escritas por especialistas


# Bibliografia e Créditos

### Material de Apoio
- [Markdown Guide](https://www.markdownguide.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Plotly](https://plotly.com/python/)
- [Python](https://docs.python.org/3/)
- [Keras](https://keras.io/api/)

### Créditos

Material criado por **Roberto R Balbinotti**.  
Projeto de Conclusão do Curso - Machine Learning da [Data Science Academy](https://www.datascienceacademy.com.br/)













