# The Music Minion
### Domain
Analysis of music clips available from open data bases with supervised learning techniques we hope to be able to:  
1. Build a classifier for music genre. Only very general genres (e.g. rock, electronic, pop...) will be considered at first. Further refinement of the genres will be carried out depending on the results.  

2. A language classifier for the audio clips. As a first step only English and no lyrics categories will be considered. Other languages for which enough data will be included depending on the results.  

### Data
For the project the [FMA data set](https://arxiv.org/pdf/1612.01840.pdf) will be used. More than 100,000 audio clips are available in the data set. A very convenient characteristic of FMA is that pre-computed features are already available for all tracks. A total of 512 features were extracted using [LibROSA Python library](https://librosa.github.io/librosa/). All features can be grouped in 11 music analysis magnitudes such as Mel-frequency cepstral coefficients (MFCC), Tonnetz and spectral contrast. Different features will be selected for the two parts of the project and only a part of the observations will be considered at first.  

### Known unknowns  
* The relevant features will be selected on the basis of music analysis literature and some knowledge in that field has to be collected.  
* It is not known if these features will be enough to obtain reasonable accuracies for the classifiers. Further analysis using LiBROSA could be needed in the FMA database or other music audio if the data base needs to be expanded. 
