from sklearn.metrics import roc_auc_score, f1_score, precision_score, \
    recall_score, confusion_matrix, log_loss

# импортируйте необходимые вам модули

# заведите словарь со всеми метриками
metrics = {}

# посчитайте метрики из модуля sklearn.metrics
# err_1 — ошибка первого рода
# err_2 — ошибка второго рода
_, err1, _, err2 = confusion_matrix(y_test, prediction, normalize='all').ravel()
auc = roc_auc_score(y_test, probas)
precision = precision_score(y_test, prediction)
recall = recall_score(y_test, prediction)  # ваш код здесь #
f1 = f1_score(y_test, prediction)  # ваш код здесь #
logloss = log_loss(y_test, prediction)  # ваш код здесь #

# запишите значения метрик в словарь
metrics["err1"] = err1
metrics["err2"] = err2
metrics["auc"] = auc
metrics["precision"] = precision
metrics["recall"] = recall
metrics["f1"] = f1
metrics["logloss"] = logloss