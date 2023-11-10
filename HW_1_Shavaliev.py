from transformers import pipeline
reader = pipeline("question-answering")
text = "Vitaly was born in 1986. He studied at the Ural Federal University. His career has been in the field of human resources management"
question = "Which field work Vitaly?"
outputs = reader(question=question, context=text)
print(outputs)