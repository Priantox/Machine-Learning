# Machine Learning Metrics Explanation

## 1. Accuracy

**Definition:** The percentage of correct predictions out of total predictions.

**Formula:** 
$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

Where:
- TP = True Positives
- TN = True Negatives
- FP = False Positives
- FN = False Negatives

**Higher is Better:** ✅ YES (Ranges from 0 to 1 or 0% to 100%)

**Use Case:** Good for balanced datasets where all classes are equally important. Not ideal for imbalanced datasets.

---

## 2. Precision

**Definition:** Of all positive predictions made, what percentage were actually correct?

**Formula:**
$$\text{Precision} = \frac{TP}{TP + FP}$$

**Higher is Better:** ✅ YES (Ranges from 0 to 1)

**Use Case:** Important when false positives are costly (e.g., spam detection, medical diagnosis). Focus on avoiding incorrect positive predictions.

---

## 3. Recall (Sensitivity/True Positive Rate)

**Definition:** Of all actual positives, what percentage did the model correctly identify?

**Formula:**
$$\text{Recall} = \frac{TP}{TP + FN}$$

**Higher is Better:** ✅ YES (Ranges from 0 to 1)

**Use Case:** Important when false negatives are costly (e.g., disease detection, fraud detection). Focus on catching all positive cases.

---

## 4. F1 Score

**Definition:** The harmonic mean of Precision and Recall. Balances both metrics.

**Formula:**
$$\text{F1 Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

**Higher is Better:** ✅ YES (Ranges from 0 to 1)

**Use Case:** Use when you need to balance precision and recall, especially with imbalanced datasets. Better than accuracy for classification problems.

---

## 5. R² Score (Coefficient of Determination)

**Definition:** The proportion of variance in the dependent variable explained by the independent variables. Used for regression models.

**Formula:**
$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}} = 1 - \frac{\sum(y_i - \hat{y}_i)^2}{\sum(y_i - \bar{y})^2}$$

Where:
- $SS_{res}$ = Sum of Squared Residuals
- $SS_{tot}$ = Total Sum of Squares
- $y_i$ = Actual values
- $\hat{y}_i$ = Predicted values
- $\bar{y}$ = Mean of actual values

**Higher is Better:** ✅ YES (Ranges from 0 to 1, can be negative for poor models)

**Interpretation:**
- R² = 1: Perfect fit
- R² = 0.7-0.9: Strong relationship
- R² = 0.4-0.7: Moderate relationship
- R² < 0.4: Weak relationship
- R² < 0: Model performs worse than a horizontal line (baseline)

**Use Case:** Evaluate regression models to understand how well the model explains variance in the data.

---

## 6. EM (Expectation Maximization)

**Definition:** EM is an iterative algorithm used for finding maximum likelihood estimates in the presence of latent (hidden) variables. Often used in clustering, mixture models, and incomplete data scenarios.

**Key Points:**
- **E-step:** Calculate the expectation of the log-likelihood function
- **M-step:** Maximize the likelihood by updating parameters

**Not a Metric:** EM is an algorithm, not typically a performance metric. However, you can evaluate EM-based models (like Gaussian Mixture Models) using:
- Log-likelihood
- BIC (Bayesian Information Criterion)
- AIC (Akaike Information Criterion)

**Use Case:** Unsupervised learning tasks like clustering and handling missing data.

---

## 7. RL (Possible Interpretations)

This could refer to several concepts depending on context:

### a) **Root Mean Squared Error (RMSE)** - If RL means "Regression Loss"

**Formula:**
$$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$$

**Lower is Better:** ✅ YES (0 is perfect)

**Use Case:** Regression evaluation. Penalizes larger errors more heavily.

### b) **Mean Absolute Error (MAE)** - If RL means "Regression Loss"

**Formula:**
$$MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$$

**Lower is Better:** ✅ YES (0 is perfect)

**Use Case:** Regression evaluation. More interpretable than RMSE as it's in the same units as the target variable.

### c) **Reinforcement Learning Metrics** - If RL means "Reinforcement Learning"

Common metrics include:
- **Cumulative Reward:** Higher is better ✅
- **Average Reward per Episode:** Higher is better ✅

---

## Summary Comparison Table

| Metric | Type | Better If | Range | Key Use |
|--------|------|-----------|-------|---------|
| **Accuracy** | Classification | Higher ✅ | [0, 1] | Balanced datasets |
| **Precision** | Classification | Higher ✅ | [0, 1] | Minimize false positives |
| **Recall** | Classification | Higher ✅ | [0, 1] | Minimize false negatives |
| **F1 Score** | Classification | Higher ✅ | [0, 1] | Imbalanced datasets |
| **R² Score** | Regression | Higher ✅ | (-∞, 1] | Variance explained |
| **RMSE** | Regression | Lower ✅ | [0, ∞) | Penalizes large errors |
| **MAE** | Regression | Lower ✅ | [0, ∞) | Interpretable errors |

---

## Quick Decision Guide

**For Classification Problems:**
- Balanced data → Use **Accuracy**
- Imbalanced data → Use **F1 Score** or **Precision/Recall**
- Need both precision & recall → Use **F1 Score**
- Care about missing positives → Prioritize **Recall**
- Care about false alarms → Prioritize **Precision**

**For Regression Problems:**
- Model explanation → Use **R² Score**
- Error magnitude → Use **RMSE** or **MAE**
- Interpretability → Use **MAE**
- Penalize outliers → Use **RMSE**

---