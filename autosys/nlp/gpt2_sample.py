#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" gpt2_sample - a little something to play with ...
    reference: https://towardsdatascience.com/roadmap-to-natural-language-processing-nlp-38a81dcff3a6
    ---
    Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

# Loading and setting up GPT2 Open AI Transformer Model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = TFGPT2LMHeadModel.from_pretrained("gpt2",
                                          pad_token_id=tokenizer.eos_token_id)
# Encoding the starting point of the sentence we want to predict
input_data = tokenizer.encode("A book is a mirror that offers us only " +
                              "what we already carry inside us.",
                              return_tensors='tf')
# Generating Output String
output = model.generate(
    input_data,
    do_sample=True,
    max_length=50,
    top_k=30
)

print(tokenizer.decode(output[0], skip_special_tokens=True))
