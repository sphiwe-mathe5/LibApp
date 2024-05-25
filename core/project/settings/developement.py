from core.project.settings import BASE_DIR, ENV, DEBUG

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENV.config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DEBUG

ALLOWED_HOSTS = ENV.config('ALLOWED_HOSTS', cast=ENV.Csv())
