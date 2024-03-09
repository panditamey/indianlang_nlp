from indianl_nlp.indianl_nlp import generate_text

seed_text = "Today"
language = 'english'
generated_text = generate_text(seed_text,500, language)
print(generated_text)
