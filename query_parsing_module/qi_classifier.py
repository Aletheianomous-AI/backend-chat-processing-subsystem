from pathlib import Path
import os
import sys

#Add modules from other folder descendents into memory.
cur_dir = Path(os.getcwd())
par_dir = cur_dir.parent.absolute()
sys.path.append(str(par_dir) + "/data_management_subsystem"
sys.path.append(str(par_dir))

from torchtext import data, datasets

import const
import datasets
import torchtext
import torch
import torch.nn as nn
import spacy

class QIClassifier(nn.Module):
    
    def __init__(self, input_dim, embedding_dim, hidden_dim, output_dim):
        """This function initializes the Queryable Input Classifier model.
        
        PARAMETERS
        input_dim - The input dimension of the model.
        embedding_dim - The dimension/neurons of the embedding layer.
        hidden_dim - The # of neurons in the hidden layer.
        output_dim - The dimension of output in the output layer.
        """
      
        super().__init__()

        self.embedding = nn.Embedding(input_dim, embedding_dim)
        self.rnn = nn.LSTM(embedding_dim, hidden_dim, num_layers=2,
              batch_first=False)
        self.fc = nn.Linear(hidden_dim, output_dim)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, text):
        """Runs the predictions of the queryable classifier
        given an input text."""
        embedded_text = self.embedding(text)
        output, hidden = self.rnn(embedded_text)
        logits = self.fc(output[-1, :, :])
        output = self.softmax(logits)
        return logits, output
        

class QIClassifierWrapper():
  """This class is used to wrap the QIClassifier model class."""

  def __init__(self, model_path, device="auto"):
    """
    This class initializes the wrapper for the QI
    classifier.

    PARAMETERS
    model_path - The directory where the QI classifier model
    is stored.
    device - The device to compute the model.
    """
    self.model_path = model_path
    if device == "auto":
      if torch.cuda.is_available():
          self.device = "cuda"
      else:
          self.device = "cpu"
    else:
      if device in ["cuda", "cpu"]:
        self.device = device
      else:
        raise ValueError(device + " is an invalid device parameter.")
  
    
    # Run when allocating data
    self.TEXT = self.model_path + "/vocab.pt"
    self.LABEL = self.model_path + "/label_vocab.pt"
    self.model = torch.load(self.model_path)
    self.model = self.model.to(self.device)
    self.tokenizer = spacy.load("en_core_web_sm")
    self.is_allocated = True
  
  def classify(self, user_input):
    """This function determines whether the user input is queryable.
  
    RETURNS
    '1' if user input is queryable, or '0' if it is not queryable.
  
    PARAMETERS
    user_input - The user input message to classify whether the input
      is queryable.
    """
    
    tokenized_inp = [tok.text for tok in self.tokenizer.tokenizer(user_input)]
    tok_ind = [self.TEXT.vocab.stoi[t] for t in token_sent]
    tensor = torch.LongTensor(tok_index).to(self.device)
    tensor = tensor.unsqueeze(1)
    logit, probas = self.model(tensor)
    output = torch.argmax(probas, dim=1)
    return output.cpu()
  
  def allocate(self):
    """Allocates the model, vocab, and tokenizer into memory."""
    
    self.TEXT = self.model_path + "/vocab.pt"
    self.LABEL = self.model_path + "/label_vocab.pt"
    self.model = torch.load(self.model_path)
    self.model = self.model.to(self.device
    self.tokenizer = spacy.load("en_core_web_sm")
    self.is_allocated = True
  
  def deallocate(self):
    """Deallocates the model, vocab, and tokenizer from memory."""
    
    self.TEXT = None
    self.LABEL = None
    self.model = None
    self.tokenizer = None
    del self.TEXT, self.LABEL, self.model, self.tokenizer
    gc.collect()
    torch.cuda.empty_cache()
