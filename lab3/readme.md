# How to work with this 

## Setup

1. First make sure you have your local env set up.
2. Make sure you are running ollama and have it installed locally.
3. Copy the model files.

```
./download_ollama.sh
```

4. Find online and copy the shrek script (or for that matter any large text of your liking) to `shrek.txt`

## Task 0 - warmup

Finish the chunking function in the `utils.py`. The `test_utils.py` provides tests for this method.

```
python -m unittest test_utils
```

 
## Task 1

Just fill in the blanks, requires previous warmup funciton from utils.

## Task 2

This requires setup for ollama.
Use the attached Modelfiles to create models `nomic_local` and `llama_local`
You may need to adjust the path of the downloaded .gguf files

you can more or less copy cosine similarity and retrieve chunks from previous task

## Task 3


Fill in the blanks as well, setup from task 2 is required
