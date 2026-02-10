import os
import yaml
import dotenv
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load .env config
dotenv.load_dotenv(config_dir / "config.env")

# load yaml config
config_yaml = {}
if (config_dir / "config.yml").exists():
    with open(config_dir / "config.yml", 'r') as f:
        config_yaml = yaml.safe_load(f)

# config parameters
telegram_token = os.environ.get("TELEGRAM_TOKEN", config_yaml.get("telegram_token"))
openai_api_key = os.environ.get("OPENAI_API_KEY", config_yaml.get("openai_api_key"))
openai_api_base = os.environ.get("OPENAI_API_BASE", config_yaml.get("openai_api_base", None))
openai_api_model = os.environ.get("OPENAI_API_MODEL", config_yaml.get("openai_api_model", "gpt-3.5-turbo"))

# allowed_telegram_usernames
allowed_telegram_usernames = os.environ.get("ALLOWED_TELEGRAM_USERNAMES")
if allowed_telegram_usernames is not None:
    if allowed_telegram_usernames == "":
        allowed_telegram_usernames = []
    else:
        allowed_telegram_usernames = [x.strip() for x in allowed_telegram_usernames.split(",")]
else:
    allowed_telegram_usernames = config_yaml.get("allowed_telegram_usernames", [])

new_dialog_timeout = int(os.environ.get("NEW_DIALOG_TIMEOUT", config_yaml.get("new_dialog_timeout", 600)))
enable_message_streaming = os.environ.get("ENABLE_MESSAGE_STREAMING", str(config_yaml.get("enable_message_streaming", True))).lower() == "true"
return_n_generated_images = int(os.environ.get("RETURN_N_GENERATED_IMAGES", config_yaml.get("return_n_generated_images", 1)))
image_size = os.environ.get("IMAGE_SIZE", config_yaml.get("image_size", "512x512"))
n_chat_modes_per_page = int(os.environ.get("N_CHAT_MODES_PER_PAGE", config_yaml.get("n_chat_modes_per_page", 5)))

# mongodb
mongodb_uri = os.environ.get("MONGODB_URL") or os.environ.get("MONGO_URL") or os.environ.get("MONGODB_URI")
if not mongodb_uri:
    mongodb_port = os.environ.get("MONGODB_PORT", 27017)
    mongodb_uri = f"mongodb://mongo:{mongodb_port}"

print(f"MongoDB URI: {mongodb_uri.split('@')[-1] if '@' in mongodb_uri else mongodb_uri}")

# chat_modes
with open(config_dir / "chat_modes.yml", 'r') as f:
    chat_modes = yaml.safe_load(f)

# models
with open(config_dir / "models.yml", 'r') as f:
    models = yaml.safe_load(f)

# files
help_group_chat_video_path = Path(__file__).parent.parent.resolve() / "static" / "help_group_chat.mp4"
