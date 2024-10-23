# Medicina personalizzata - Ridefinire il trattamento del cancro. 
**Corso - Machine Learning**  
Progetto del Programma di Formazione per Data Scientist della Data Science Academy

## Descrizione del Progetto
Negli ultimi anni si è parlato molto di come la medicina di precisione e, più specificamente, i test genetici, cambieranno il trattamento di malattie come il cancro. Tuttavia, questo sta accadendo solo parzialmente a causa della grande quantità di lavoro manuale ancora necessario. In questo progetto, cercheremo di portare la medicina personalizzata al suo massimo potenziale. Una volta sequenziato, un tumore canceroso può avere migliaia di mutazioni genetiche. La sfida è distinguere le mutazioni che contribuiscono alla crescita del tumore dalle altre mutazioni.

Attualmente, questa interpretazione delle mutazioni genetiche viene eseguita manualmente. Questo è un compito molto lungo, in cui un patologo clinico deve rivedere manualmente e classificare ciascuna mutazione genetica in base a prove dalla letteratura clinica basata su testo. Per questo progetto, il [MSKCC](https://en.wikipedia.org/wiki/Memorial_Sloan_Kettering_Cancer_Center) sta fornendo una base di conoscenza annotata da esperti, dove ricercatori e oncologi di fama mondiale hanno annotato manualmente migliaia di mutazioni.

> L'obiettivo del progetto è sviluppare un algoritmo di **Apprendimento Automatico utilizzando Keras e TensorFlow**.

Per costruire questo progetto, il dataset è disponibile per il download al seguente link: [kaggle.data](https://www.kaggle.com/c/msk-redefining-cancer-treatment/data)

## Fonte dei Dati

- [Kaggle](https://www.kaggle.com)
- [Data Science Academy](https://www.datascienceacademy.com.br)

## Tecnologie Utilizzate

- [PDM Python](https://pdm-project.org/)
- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [Keras](https://keras.io/)
- [TensorFlow](https://www.tensorflow.org/)
- [GitHub](https://github.com/)
- [Colab](https://colab.research.google.com/)
- [Plotly](https://plotly.com/)

## Installazione
Scaricare il progetto da [github](https://github.com/rbalbinotti/treat_cancer_keras)

Installare le dipendenze utilizzando PDM Python digitando il comando qui sotto nella cartella del progetto:
```
    pdm sync
```
    Se necessario, i pacchetti e le versioni sono elencati nel file pyproject.toml.

## Dizionario dei Dati
- ID: Identificazione univoca di ogni elemento
- Gene: Gene in cui si trova la mutazione genetica
- Variation: Amminoacidi modificati dalla mutazione
- Class: Classe 1-9 in cui verrà classificata la mutazione genetica
- Clinical Evidence: Prove cliniche scritte da specialisti

>| gene  | variation | clinical_evidence | class |
>|-------|-----------|-------------------|-------|
>| IDH1  | G123R     | Mutations in the genes for isocitrate dehydrogenase 1 (IDH1) and isocitrate dehydrogenase 2 (IDH2) have been recently identified in glioblastoma. In the present study, we investigated IDH1 and IDH... | 1 |
>| MYC   | MYC-nick  | Evasion of apoptosis is critical in Myc-induced tumor progression. Here we report that cancer cells evade death under stress by activating calpain-mediated proteolysis of Myc. This generates Myc-n... | 4 |
>| ERCC2 | R487W     | The increasing application of gene panels for familial cancer susceptibility disorders will probably lead to an increased proposal of susceptibility gene candidates. Using ERCC2 DNA repair gene as... | 1 |

# Bibliografia e Crediti
### Materiale di Supporto
- [Guida Markdown](https://www.markdownguide.org/)
- [Documentazioni Pandas](https://pandas.pydata.org/docs/)
- [Plotly](https://plotly.com/python/)
- [Python](https://docs.python.org/3/)
- [Keras](https://keras.io/api/)

### Crediti
Materiale creato da **Roberto R Balbinotti**.  
Progetto di Conclusione del Corso - Machine Learning della [Data Science Academy](https://www.datascienceacademy.com.br/)