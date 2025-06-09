import os
import torch
from PIL import Image
from torch.utils.data import Dataset
import torchvision.transforms as transforms

class CaptionDataset(Dataset):
    def __init__(self, image_folder, captions_dict, vocab, transform=None):
        self.image_folder = image_folder
        self.captions_dict = captions_dict
        self.vocab = vocab
        self.transform = transform

        self.image_ids = list(captions_dict.keys())

    def __len__(self):
        return len(self.image_ids)

    def __getitem__(self, idx):
        image_id = self.image_ids[idx]
        image_path = os.path.join(self.image_folder, image_id)
        image = Image.open(image_path).convert("RGB")

        caption = self.captions_dict[image_id]
        tokens = [self.vocab['<start>']] + [self.vocab[word] for word in caption.split()] + [self.vocab['<end>']]

        if self.transform:
            image = self.transform(image)

        return image, torch.tensor(tokens)
