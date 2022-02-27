In this project, I'll be employing several supervised learning algorithms on data collected from the '`1994 U.S. Census`' and comparing their predictive performance against one another.

The goal is to construct a model that accurately predicts whether an individual makes more than $50,000. This sort of information is useful in non-profit settings, where organizations can better understand how large of a donation to request, or whether or not they should reach out to begin with.

The [dataset](https://archive.ics.uci.edu/ml/datasets/Census+Income) was donated by **Ron Kohavi** and **Barry Becker** to the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php) after being published in the article [Scaling Up the Accuracy of Naive-Bayes Classifiers: A Decision-Tree Hybrid](https://www.academia.edu/download/40088603/Scaling_Up_the_Accuracy_of_Naive-Bayes_C20151116-5477-1fw84ob.pdf).

However, [our version](https://drive.google.com/file/d/1pSqjbiTiTX4H4vLahjMUMXmNj6ChXn9q/view?usp=sharing) here consists of small changes to the original dataset, such as removing the `'fnlwgt'` feature and records with missing or ill-formatted entries.