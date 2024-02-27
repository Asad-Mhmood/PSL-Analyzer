
# PSL Analyzer

This project focuses on enhancing the PSL (Pakistan Super League) experience through two primary features.

The first feature involves predicting the score of the team batting in the first inning. This prediction adds an element of anticipation and insight into the game, allowing fans to gauge team performance and potential outcomes.

The second feature is centered around predicting the probability of a team winning during the second inning. By leveraging data and analytical models, this feature provides valuable insights into the dynamics of the match, empowering viewers to make informed predictions and engage more deeply with the game.

# Demo

https://youtu.be/kxnwQAgLmHE?si=PUSD-vdTkWfV3W_R

# Working

This project leverages data from the first seven seasons of PSL matches. The initial steps involve extracting crucial features from the dataset and preprocessing it to ensure optimal performance. Subsequently, two models are trained: one for predicting scores and the other for estimating winning probabilities.

Following model training, the project exports the resulting models as pickle files, preparing them for integration into a website. Flask serves as the framework for website development, facilitating seamless integration of the predictive models. Additionally, MySQL is utilized for implementing user authentication, including login and registration functionalities.

In summary, the project encompasses data preprocessing, model training, exportation of models as pickle files, and website development using Flask with MySQL integration for user authentication.



# Tools

- Flask
- SQL
- HTML/CSS
- Pandas
- Numpy
- Scikit Learn


## Screenshots

![login](https://drive.google.com/file/d/1q4ELLxeyD9ru-mjriU_2zgsy2dLvOKAJ/view?usp=sharing)
![Registration](https://drive.google.com/file/d/1HySVUXgdl947U9tmfSuLm7rbZoBLBV0_/view?usp=sharing)
![menue](https://drive.google.com/file/d/1Gj5jiVPGeNLDTHE-pOiEqwiKuNe6ww4X/view?usp=sharing)
![Score Prediction](https://drive.google.com/file/d/1P9EzquaiRwJH-GjINNaBa-az9cgTXuwB/view?usp=sharing)
![Winning Probability Prediction](https://drive.google.com/file/d/1arp2-qF3BPLq1O63jG6B4d0WL37Qv-Jp/view?usp=sharing)

