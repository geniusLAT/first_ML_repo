from transformers import pipeline

classifier = pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")

print(classifier("Под эти репозитории надо много памяти!"))
