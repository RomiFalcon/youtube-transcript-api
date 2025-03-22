from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/api/transcript', methods=['GET'])
def get_transcript():
    video_id = request.args.get('video_id')
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['es', 'es-419', 'es-MX', 'es-ES'])
        text = '\n'.join([entry['text'] for entry in transcript])
        return jsonify({"transcript": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

