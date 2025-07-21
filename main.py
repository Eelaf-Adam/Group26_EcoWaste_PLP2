from cmd.user import user_prompts
from models.database import initialize_databases

if __name__ == "__main__":
    initialize_databases()
    user_prompts()