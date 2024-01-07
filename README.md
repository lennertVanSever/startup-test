
# Flask and OpenAI Summary App

This is a simple web app built with Flask. It uses OpenAI's GPT-3.5 to summarize text you put in.

Try it Out:** Check the app online at [https://startup-test.vercel.app/](https://startup-test.vercel.app/).

## What it Does

- **Get Summaries:** The app uses OpenAI to make short summaries of your text.
- **URL Updates:** The text you write gets added to the website's link, so you can share it.

## Automatic Updates

Whenever we change the app's code, it automatically updates the online version.

## Setting Up Locally

If you want to run this app on your computer, do these steps:

1. **Download the Code**

   ```bash
   git clone https://github.com/lennertVanSever/startup-test.git
   cd startup-test
   ```

2. **Install**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Your OpenAI Key**

   Make a `.env` file and write this inside:

   ```
   OPENAI_API_KEY=YourOpenAIKeyHere
   ```

5. **Start the App**

   ```bash
   flask run
   ```

   Then, go to `http://127.0.0.1:5000/` on your web browser to see the app.

## Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **OpenAI API:** GPT-3.5