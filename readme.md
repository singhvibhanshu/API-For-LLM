# API-For-LLM

This project provides an API interface for Large Language Models (LLMs) using FastAPI. It allows users to interact with LLMs through a simple HTTP API.

## Features

- **Prompt Completion**: Send a prompt to the API and receive a completion from the LLM.
- **Customizable Parameters**: Adjust parameters like temperature and maximum tokens to control the output.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/singhvibhanshu/API-For-LLM.git
   cd API-For-LLM
   ```

2. **Install Dependencies**:

   Ensure you have Python 3.7 or higher installed. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:

   Create a `.env` file in the root directory with the following content:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

   Replace `your_openai_api_key_here` with your actual OpenAI API key.

## Usage

1. **Start the API Server**:

   Run the following command:

   ```bash
   uvicorn main:app --reload
   ```

   The API will be accessible at `http://127.0.0.1:8000`.

2. **API Endpoint**:

   - `POST /generate/`

     Send a JSON payload with the following structure:

     ```json
     {
       "prompt": "Your prompt here",
       "temperature": 0.7,
       "max_tokens": 150
     }
     ```

     - `prompt` (string): The input text to be completed by the LLM.
     - `temperature` (float, optional): Controls the randomness of the output. Default is 0.7.
     - `max_tokens` (int, optional): Maximum number of tokens to generate. Default is 150.

     **Response**:

     ```json
     {
       "generated_text": "The completion from the LLM."
     }
     ```

## Example Request

Here's how you can interact with the API using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/generate/" \
     -H "Content-Type: application/json" \
     -d '{
           "prompt": "Once upon a time",
           "temperature": 0.7,
           "max_tokens": 100
         }'
```

**Response**:

```json
{
  "generated_text": "Once upon a time, in a land far, far away..."
}
```

## Dependencies

- `fastapi`: For building the API.
- `openai`: OpenAI's API client.
- `pydantic`: Data validation and settings management.
- `python-dotenv`: For loading environment variables from a `.env` file.

## Notes

- Ensure your OpenAI API key is valid and has sufficient quota.
- Adjust the `temperature` and `max_tokens` parameters as needed to get the desired output.

---

Feel free to modify this `README.md` to better suit your project's specifics. Let me know if you need any more help!

