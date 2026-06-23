# Clone and setup
git clone <repository-url>
cd <project-directory>

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your database URL, secret key, and AWS credentials

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
