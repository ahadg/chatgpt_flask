from flask import Flask, request, jsonify
from openai import OpenAI


app = Flask(__name__)

# Set your OpenAI API key
#openai.api_key = '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'
client = OpenAI(
    # This is the default and can be omitted
    api_key='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',
)


@app.route('/ask', methods=['POST'])
def ask_question():
    try:
        # Get data from the frontend
        data = request.get_json()
        print('data00--',data,flush=True)
        file_url = data.get('fileUrl')
        file_type = data.get('fileType')
        prompt = data.get('prompt')

        response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                "type": file_type,
                "image_url": {
                    "url": file_url,
                },
                },
            ],
            }
        ],
        max_tokens=300,
        )

        print(response.choices[0])

        return jsonify({'answer': response.choices[0].message.content})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
