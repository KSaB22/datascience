import kagglehub
import shutil
import os

# Download the dataset
path = kagglehub.dataset_download("emstatsl/csgo-cheating-dataset")

# Desired target location
target_dir = "./CSGO_Cheating_Dataset"

# Move it to your desired location
if not os.path.exists(target_dir):
    shutil.move(path, target_dir)
else:
    print("Target directory already exists. Skipping move.")

print("Dataset is now at:", target_dir)