from transformers import PreTrainedTokenizerFast, GPT2LMHeadModel, GPT2TokenizerFast, GPT2Tokenizer
from argparse import ArgumentParser

def load_model(model_path):
    model = GPT2LMHeadModel.from_pretrained(model_path)
    return model


def load_tokenizer(tokenizer_path):
    tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_path)
    return tokenizer


def generate_text(sequence, max_length):
    model_path = "result_full"
    model = load_model(model_path)
    tokenizer = load_tokenizer(model_path)
    ids = tokenizer.encode(f'{sequence}', return_tensors='pt')
    final_outputs = model.generate(
        ids,
        do_sample=True,
        max_length=max_length,
        pad_token_id=model.config.eos_token_id,
        top_k=50,
        top_p=0.95,
    )
    return tokenizer.decode(final_outputs[0], skip_special_tokens=True)


if __name__ == '__main__':
    sequence = input() # oil price
    if sequence == 'prompts.txt':
        with open(sequence, 'r', encoding='utf-8') as f:
            prompts = f.read().splitlines()
            prompts = [x for x in prompts if x != '']

        for p in prompts:
            p_save = open('_'.join(p.split(' '))+'.txt','w', encoding='utf-8')
            for i in range(10):
                text = generate_text(p, 50)
                p_save.write(text+'\n')
            p_save.close()
    else:        
        max_len = int(input()) # 20
        print(generate_text(sequence, max_len))
