import kagglehub

# Download latest version
path = kagglehub.dataset_download("kylegraupe/spy-daily-eod-options-quotes-2020-2022")

print("Path to dataset files:", path)