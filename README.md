# CLCS Programme CSV Separator

A web application for separating CSV files by programme applications at the College of Language and Cultural Studies (CLCS).

## Features

- 📄 **CSV File Upload**: Drag-and-drop or click to upload CSV files
- 📊 **Automatic Separation**: Splits students by their applied programmes
- 📁 **Multiple Programme Support**: Handles students applying for multiple programmes
- ⬇️ **File Download**: Download generated CSV files directly
- 🎨 **Modern UI**: Responsive web interface
- 🚀 **Fast Processing**: Efficient pandas-based processing

## Programmes Supported

1. Bachelor of Arts in Language and Heritage Studies
2. Bachelor of Arts in History and Global Affairs
3. Bachelor of Arts in Bhutan Studies and Global Perspectives
4. Bachelor of Arts in Cultural Innovation and Entrepreneurship
5. Bachelor of Arts in Psychology and Mindfulness

## Local Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/dependrabas/Course_Segregator.git
cd Course_Segregator
```

2. Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open in browser:
```
http://localhost:5000
```

## Deployment on Render

### Step-by-Step Deployment Guide

1. **Push to GitHub**:
   - Ensure all files are committed and pushed to GitHub
   ```bash
   git add .
   git commit -m "Prepare for Render deployment"
   git push origin main
   ```

2. **Connect to Render**:
   - Go to [render.com](https://render.com)
   - Sign in with GitHub account
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Configure Render Settings**:
   - **Name**: `clcs-programme-separator` (or your choice)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free (or paid if you want better performance)

4. **Set Environment Variables** (if needed):
   - Add in Render dashboard under "Environment"
   - `FLASK_ENV=production`

5. **Deploy**:
   - Click "Create Web Service"
   - Render will automatically build and deploy
   - Your app will be available at `https://your-app-name.onrender.com`

## Project Structure

```
programme_separator/
├── app.py                    # Flask application server
├── processor.py              # CSV processing logic
├── requirements.txt          # Python dependencies
├── Procfile                  # Render deployment configuration
├── README.md                 # This file
├── templates/
│   └── index.html           # Web interface HTML
├── static/
│   ├── style.css            # Styling
│   └── script.js            # Frontend logic
├── uploads/                 # Temporary upload storage
└── output/                  # Generated CSV files
```

## How It Works

1. User uploads a CSV file with applicant data
2. The app reads the "7. Programme Applied For" column
3. For students with multiple programme choices, each choice is separated into a new row
4. Individual CSV files are created for each programme
5. Only programmes with at least one applicant are included
6. Files are available for download

## CSV Format Requirements

Your input CSV must include a column named `7. Programme Applied For` with values like:
```
Bachelor of Arts in Language and Heritage Studies, Bachelor of Arts in History and Global Affairs
```

## Troubleshooting

### Render Deployment Issues

**Build fails with "ModuleNotFoundError"**:
- Ensure all dependencies are listed in `requirements.txt`
- Run `pip freeze > requirements.txt` locally to update

**App crashes on startup**:
- Check logs in Render dashboard
- Ensure `Procfile` is present and correct
- Make sure Flask runs on `0.0.0.0` (not `localhost`)

**Files not persisting**:
- Render's free tier has ephemeral file systems
- Generated files are temporary
- For persistent storage, consider upgrading or using external storage

### Local Issues

**Port already in use**:
```bash
# Change port in app.py or use environment variable
PORT=8000 python app.py
```

**Permission denied on output folder**:
```bash
mkdir -p output uploads
chmod 755 output uploads
```

## API Endpoints

- `GET /` - Main page
- `POST /api/upload` - Upload and process CSV file
- `GET /api/files` - List generated files
- `GET /api/download/<filename>` - Download CSV file

## Technologies Used

- **Backend**: Flask (Python)
- **Processing**: Pandas
- **Server**: Gunicorn (production)
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Render

## License

This project is licensed under the MIT License.

## Support

For issues or questions, please contact the development team or open an issue on GitHub.
