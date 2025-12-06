

# import libraries
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# variable to keep chat history
chat_history = []
model_cache = {}

# define the model name
model_name = "facebook/blenderbot-400M-distill"
#-----------------------------------------------------------------------------------------------------------------------------------------
# Note: We use that model as its lightweight and fast to run on CPU.
# You can change it to any other model from Hugging Face, but make sure you have enough resources (CPU/GPU) to run it.
# Please consider changing the AutoModelForSeq2SeqLM to AutoModelForCausalLM if you use a model that is not Seq2Seq (e.g. T5, OPT, etc.)
# For more information on the models, please refer to https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads
#-----------------------------------------------------------------------------------------------------------------------------------------

# loading the model and tokenizer based on the model name
def load_model(model_name):

    # choose float16 on CUDA when available
    preferred_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_name,
        torch_dtype=preferred_dtype,
    )

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    model_cache[model_name] = (model, tokenizer)

    return model, tokenizer

# selecting 
def get_response(prompt):

    model, tokenizer = load_model(model_name)

    response = generate_response(prompt, model, tokenizer)

    return response

# function to generate response from the model
def generate_response(prompt, model, tokenizer):
    
    # get only last 2 exchanges for Blenderbot to save context length
    if "blenderbot" in model.name_or_path.lower():
        short_history = chat_history[-2:]
        max_len = 128
    else:
        short_history = chat_history
        max_len = 256
        
    conversation = ""
    for u, a in short_history:
        conversation += f"User: {u}\nAssistant: {a}\n"
    conversation += f"User: {prompt}\nAssistant: "

    # tokenize the model_input_text (encode_plus used as we give new prompt and chat history together)
    inputs = tokenizer(conversation, 
                       return_tensors="pt", 
                       truncation=True, 
                       max_length=max_len)

    # generate model response
    outputs = model.generate(
        **inputs,
        max_new_tokens=80,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
        )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("response:", response)

    # extract only the assistant reply
    if "Assistant:" in response:
        response = response.split("Assistant:")[-1].strip()

    chat_history.append((prompt, response))

    return conversation, response
