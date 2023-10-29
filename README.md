![AI Dream Whisper](https://i.ibb.co/8NjK3vj/DALL-E-2023-10-29-02-11-58-Illustration-of-a-tranquil-bedroom-setting-with-a-person-in-deep-sleep-un.png)


# AI Dream Whisper

AI Dream Whisper is a groundbreaking application that leverages the power of artificial intelligence to transform passive nighttime hours into a unique learning experience. Drawing inspiration from scientific research on the enhancement of learning through auditory stimuli during REM sleep, this app provides students with calming, educational stories designed for nighttime learning.


## Technologies Used

- **OpenAI**: Used for generating educational stories based on user input.
- **PlayHT**: A text-to-speech API used for converting the generated stories into audio format.
- **Flask**: A lightweight web framework for Python, used to set up the web server and handle requests.
- **Bootstrap**: A popular CSS framework used for styling the web interface.


## How to Run

1. Clone the repository:
   ```
   git clone https://github.com/davicoscarelli/AIDreamWhisper.git
   ```

2. Navigate to the repository directory:
   ```
   cd AIDreamWhisper
   ```

3. Install the required Python dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables by creating a `.env` file in the root directory of the project. Add the following API keys:

   - **PLAYHT_API_KEY & PLAYHT_USER_ID**:
     - Visit the API Access page [play.ht/studio/api-access](https://play.ht/studio/api-access)
     - If you haven't already, sign in to your existing account.
     - Click the "Generate Secret Key" button. Your API Secret Key will be displayed. Make sure to copy and store it securely.
     - Find your User ID on the same page under the "User ID" section. Copy it for future reference.

   - **OPENAI_API_KEY**:
     - The OpenAI API uses API keys for authentication. Visit your [API Keys page](https://platform.openai.com/account/api-keys) to retrieve the API key you'll use in your requests.

   Your `.env` file should look like this:
   ```
   PLAYHT_API_KEY=your_playht_api_key
   PLAYHT_USER_ID=your_playht_user_id
   OPENAI_API_KEY=your_openai_api_key
   ```

5. Run the Flask application:
   ```
   python main.py
   ```

6. Open a web browser and navigate to `http://localhost:5000` to access the application.


---

Developed with ❤️ by [Davi Coscarelli](https://github.com/davicoscarelli). For any queries or feedback, please raise an issue in the [repository](https://github.com/davicoscarelli/AIDreamWhisper/issues).



