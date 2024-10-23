# Medicina Personalizada - Redefinindo o Tratamento de Câncer.  
**Curso - Machine Learning**  
Projeto da Formação Cientista de Dados da [Data Science Academy](https://www.datascienceacademy.com.br/)

## Descrição Projeto

Muito tem sido dito durante os últimos anos sobre como a medicina de precisão e, mais concretamente, como o teste genético, vai provocar disrupção no tratamento de doenças como o câncer.  

Mas isso ainda está acontecendo apenas parcialmente devido à enorme quantidade de trabalho manual ainda necessário. Neste projeto, tentaremos levar a medicina personalizada ao seu potencial máximo.  

Uma vez sequenciado, um tumor cancerígeno pode ter milhares de mutações genéticas. O desafio é distinguir as mutações que contribuem para o crescimento do tumor das mutações.  

Atualmente, esta interpretação de mutações genéticas está sendo feita manualmente. Esta é uma tarefa muito demorada, onde um patologista clínico tem que revisar manualmente e classificar cada mutação genética com base em evidências da literatura clínica baseada em texto.

Para este projeto, o [MSKCC](https://en.wikipedia.org/wiki/Memorial_Sloan_Kettering_Cancer_Center) (Memorial Sloan Kettering Cancer Center) está disponibilizando uma base de conhecimento anotada por especialistas, onde pesquisadores e oncologistas de nível mundial anotaram manualmente milhares de mutações.

   > O objetivo do projeto é desenvolver um **algoritmo de Aprendizado de Máquina com Keras e TensorFlow**.

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
- [TensorFlow](https://www.tensorflow.org/)
- [GitHub](https://github.com/)
- [Colab](https://colab.research.google.com/)
- [Plotly](https://plotly.com/)

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

>| gene  | variation | clinical_evidence | class |
>|-------|-----------|-------------------|-------|
>| IDH1  | G123R     | Mutations in the genes for isocitrate dehydrogenase 1 (IDH1) and isocitrate dehydrogenase 2 (IDH2) have been recently identified in glioblastoma. In the present study, we investigated IDH1 and IDH... | 1 |
>| MYC   | MYC-nick  | Evasion of apoptosis is critical in Myc-induced tumor progression. Here we report that cancer cells evade death under stress by activating calpain-mediated proteolysis of Myc. This generates Myc-n... | 4 |
>| ERCC2 | R487W     | The increasing application of gene panels for familial cancer susceptibility disorders will probably lead to an increased proposal of susceptibility gene candidates. Using ERCC2 DNA repair gene as... | 1 |


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













