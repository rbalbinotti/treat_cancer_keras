<div style="text-align: center;">
  <p>Scegli la tua lingua / Escolha sua lingua:</p>
  <p>
    <a href="README_it.md" style="display: inline-block; padding: 10px 20px; background-color: #007BFF; color: white; text-decoration: none; border-radius: 5px; margin: 5px;">Italiano</a>
    <a href="README_PT-BR.md" style="display: inline-block; padding: 10px 20px; background-color: #28A745; color: white; text-decoration: none; border-radius: 5px; margin: 5px;">Português</a>
  </p>
</div>


# Personalized Medicine - Redefining Cancer Treatment.
**Course - Machine Learning** 
Project from the Data Scientist Training Program by the Data Science Academy

## Project Description
Much has been said in recent years about how precision medicine and, more specifically, genetic testing will disrupt the treatment of diseases such as cancer. However, this is still happening only partially due to the enormous amount of manual work still required. In this project, we will attempt to bring personalized medicine to its full potential. Once sequenced, a cancerous tumor can have thousands of genetic mutations. The challenge is to distinguish the mutations that contribute to tumor growth from other mutations.

Currently, this interpretation of genetic mutations is being done manually. This is a very time-consuming task, where a clinical pathologist has to manually review and classify each genetic mutation based on evidence from text-based clinical literature. For this project, the [MSKCC](https://en.wikipedia.org/wiki/Memorial_Sloan_Kettering_Cancer_Center) is providing an expert-annotated knowledge base, where world-class researchers and oncologists have manually annotated thousands of mutations.

> The goal of the project is to develop a **Machine Learning algorithm using Keras and TensorFlow**.

For building this project, the dataset is available for download at the following link:
[kaggle.data](https://www.kaggle.com/c/msk-redefining-cancer-treatment/data)

## Data Source

- [Kaggle](https://www.kaggle.com)
- [Data Science Academy](https://www.datascienceacademy.com.br)

## Technologies Used

- [PDM Python](https://pdm-project.org/)
- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [Keras](https://keras.io/)
- [TensorFlow](https://www.tensorflow.org/)
- [GitHub](https://github.com/)
- [Colab](https://colab.research.google.com/)
- [Plotly](https://plotly.com/)

## Installation

- Download the project from [github](https://github.com/rbalbinotti/treat_cancer_keras)
- Install dependencies using PDM Python by typing the command below in the project folder:
```
    pdm sync
```
    If necessary, the packages and versions are listed in the pyproject.toml file.

## Data Dictionary
- ID: Unique identification of each element
- Gene: Gene where the genetic mutation is located
- Variation: Amino acids modified by the mutation
- Class: 1-9 class in which the genetic mutation will be classified
- Clinical Evidence: Clinical evidence written by specialists

>| gene  | variation | clinical_evidence | class |
>|-------|-----------|-------------------|-------|
>| IDH1  | G123R     | Mutations in the genes for isocitrate dehydrogenase 1 (IDH1) and isocitrate dehydrogenase 2 (IDH2) have been recently identified in glioblastoma. In the present study, we investigated IDH1 and IDH... | 1 |
>| MYC   | MYC-nick  | Evasion of apoptosis is critical in Myc-induced tumor progression. Here we report that cancer cells evade death under stress by activating calpain-mediated proteolysis of Myc. This generates Myc-n... | 4 |
>| ERCC2 | R487W     | The increasing application of gene panels for familial cancer susceptibility disorders will probably lead to an increased proposal of susceptibility gene candidates. Using ERCC2 DNA repair gene as... | 1 |

# Bibliography and Credits
### Support Material
- [Markdown Guide](https://www.markdownguide.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Plotly](https://plotly.com/python/)
- [Python](https://docs.python.org/3/)
- [Keras](https://keras.io/api/)

### Credits
Material created by **Roberto R Balbinotti**.
Graduation Project - Machine Learning Course at [Data Science Academy](https://www.datascienceacademy.com.br/)