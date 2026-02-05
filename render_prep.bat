@echo off
echo ========================================
echo Preparing project for Render Deployment
echo ========================================

echo Activating virtual environment...
call venv\Scripts\activate

echo Upgrading pip...
python -m pip install --upgrade pip

echo Installing dependencies...
pip install -r requirements.txt

echo Freezing requirements...
pip freeze > requirements.txt

echo Creating Render start command file...

echo web: uvicorn app.main:app --host 0.0.0.0 --port 10000 > start.sh

echo Creating Procfile...
echo web: uvicorn app.main:app --host 0.0.0.0 --port 10000 > Procfile

echo Adding files to git...
git add .

echo Committing changes...
git commit -m "Prepare for Render deployment"

echo Pushing to GitHub...
git push origin main

echo ========================================
echo READY FOR RENDER DEPLOYMENT!
echo Now connect this GitHub repo to Render.
echo ========================================

pause
