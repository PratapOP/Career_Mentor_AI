from flask import Flask, request, jsonify
import textwrap

app = Flask(__name__)

@app.route('/infer', methods=['POST'])
def infer():
    data = request.get_json(silent=True) or {}
    name = data.get('name', '').strip()
    resume_text = data.get('resumeText', '').strip()
    career_goal = data.get('careerGoal', '').strip()

    if not name or not resume_text or not career_goal:
        return jsonify({
            'success': False,
            'message': 'Missing required input. Please provide name, resumeText, and careerGoal.',
        }), 400

    summary = generate_feedback(name, resume_text, career_goal)
    return jsonify({
        'success': True,
        'message': summary,
    })


def generate_feedback(name: str, resume_text: str, career_goal: str) -> str:
    lines = [
        f'Hello {name}! Here is your quick career feedback:',
        '',
        '1. Resume clarity:',
        f'   - You currently describe your experience as: "{resume_text[:120]}..."',
        '   - Tip: emphasize measurable outcomes and the tools you use most.',
        '',
        '2. Goal alignment:',
        f'   - Target path: {career_goal}',
        '   - Tip: match your resume language to the role and industry keywords.',
        '',
        '3. Skill focus:',
        '   - Highlight transferable strengths, such as teamwork, problem solving, and delivery.',
        '   - Add a short skills section with tools or methods related to the target position.',
        '',
        '4. Next steps:',
        '   - Turn responsibilities into achievements with metrics and impact statements.',
        '   - Add 2–3 learning goals tied to your desired career path.',
        '',
        'If you want more detail, update your summary with concrete results and technology names.',
    ]
    return textwrap.dedent('\n'.join(lines))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
