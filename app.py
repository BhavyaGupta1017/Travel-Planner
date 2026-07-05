from flask import Flask, render_template, request, jsonify
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

app = Flask(__name__)

API_KEY ="t0nPjSiSSrtN1-82982Z-2EPy32PixDZDdElzxO-qmf1"
PROJECT_ID = "afc599a0-4912-4a38-b47d-f6301dd73c7d"
URL = "https://us-south.ml.cloud.ibm.com"

credentials = Credentials(
    url=URL,
    api_key=API_KEY
)

model = ModelInference(
    model_id="ibm/granite-4-h-small",
    credentials=credentials,
    project_id=PROJECT_ID,
    params={
        "max_new_tokens": 1000,
        "temperature": 0.6,
        "top_p": 0.9
    }
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/plan", methods=["POST"])
def plan():

    data = request.get_json()

    prompt = f"""
You are a professional AI Travel Planner.

Create a COMPLETE travel itinerary.

Travel Details

Source City: {data['source']}
Destination: {data['destination']}
Budget: ₹{data['budget']}
Duration: {data['days']} Days
Travellers: {data['travellers']}
Preferred Transport: {data['transport']}
Hotel Type: {data['hotel']}
Travel Interest: {data['interest']}

Generate a detailed travel plan with the following headings:

1. Trip Overview

2. Best Transport

3. Hotel Recommendations

4. Day-wise Itinerary
   - Day 1
   - Day 2
   - Day 3
   (Continue according to the number of days.)

5. Budget Breakdown

6. Tourist Attractions

7. Famous Local Foods

8. Packing Checklist

9. Weather Tips

10. Safety Tips

11. Emergency Contacts

12. Estimated Total Cost

Give a detailed answer under every heading.
"""

    try:
        response = model.generate_text(prompt=prompt)

        # Print full response in terminal
        print("=" * 80)
        print(response)
        print("=" * 80)

        return jsonify({
            "plan": response
        })

    except Exception as e:
        print(e)
        return jsonify({
            "plan": f"Error: {str(e)}"
        })



if __name__ == "__main__":
    app.run(debug=True)