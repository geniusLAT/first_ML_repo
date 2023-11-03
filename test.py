from transformers import pipeline

clf = pipeline(
    task = 'sentiment-analysis', 
    model = 'SkolkovoInstitute/russian_toxicity_classifier')

text = ['У нас в есть убунты и текникал превью.',
    	'Как минимум два малолетних дегенерата в треде, мда.',
        'иди на хер']

print(clf(text))

#вывод
#[{'label': 'neutral', 'score': 0.9872767329216003},
# {'label': 'toxic', 'score': 0.985331654548645}]