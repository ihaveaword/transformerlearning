import torch
from transformers import pipeline

# 创建一个情感分析管道，并且指定使用 GPU
# classifier = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english", device=0)
#
# results = classifier("We are very happy to show you the 🤗 Transformers library.")
#
# # results = classifier(["We are very happy to show you the 🤗 Transformers library.", "We hope you don't hate it."])
# for result in results:
#     print(f"label: {result['label']}, with score: {round(result['score'], 4)}")