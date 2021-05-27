# Custom Storage Settings
STATICFILES_STORAGE = "config.storages.StaticStorage"
DEFAULT_FILE_STORAGE = "config.storages.MediaStorage"

# Vultr Storage Settings
AWS_S3_REGION_NAME = "ewr1"
AWS_S3_ENDPOINT_URL = f"https://{AWS_S3_REGION_NAME}.vultrobjects.com/"

# Vultr Object Key Settings
AWS_ACCESS_KEY_ID = "Your Vultr Object Access Key"
AWS_SECRET_ACCESS_KEY = "Your Vultr Object Secret Key"
